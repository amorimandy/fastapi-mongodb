import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

# mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.teacher

teacher_collection = database.get_collection("teachers_collection")


# helpers


def teacher_helper(teacher) -> dict:
    return {
        "id": str(teacher["_id"]),
        "fullname": teacher["fullname"],
        "email": teacher["email"],
        "dominant_subject": teacher["dominant_subject"],
        "number_of_class": teacher["number_of_class"]
    }


# Retrieve all teachers present in the database
async def retrieve_teachers():
    teachers = []
    async for teacher in teacher_collection.find():
        teachers.append(teacher_helper(teacher))
    return teachers


# Add a new teacher into to the database
async def add_teacher(teacher_data: dict) -> dict:
    teacher = await teacher_collection.insert_one(teacher_data)
    new_teacher = await teacher_collection.find_one({"_id": teacher.inserted_id})
    return teacher_helper(new_teacher)


# Retrieve a teacher with a matching ID
async def retrieve_teacher(id: str) -> dict:
    teacher = await teacher_collection.find_one({"_id": ObjectId(id)})
    if teacher:
        return teacher_helper(teacher)


# Update a teacher with a matching ID
async def update_teacher(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    teacher = await teacher_collection.find_one({"_id": ObjectId(id)})
    if teacher:
        updated_teacher = await teacher_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_teacher:
            return True
        return False


# Delete a teacher from the database
async def delete_teacher(id: str):
    teacher = await teacher_collection.find_one({"_id": ObjectId(id)})
    if teacher:
        await teacher_collection.delete_one({"_id": ObjectId(id)})
        return True
