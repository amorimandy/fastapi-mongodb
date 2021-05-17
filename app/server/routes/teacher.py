from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.teacher_db import (
    add_teacher,
    delete_teacher,
    retrieve_teacher,
    retrieve_teachers,
    update_teacher,
)
from app.server.models.teacher import (
    error_response_model,
    response_model,
    TeacherSchema,
    UpdateTeacherModel,
)

teacher_router = APIRouter()


@teacher_router.post("/", response_description="Teacher data added into the database")
async def add_teacher_data(teacher: TeacherSchema = Body(...)):
    teacher = jsonable_encoder(teacher)
    new_teacher = await add_teacher(teacher)
    return response_model(new_teacher, "Teacher added successfully.")


@teacher_router.get("/", response_description="Teachers retrieved")
async def get_teachers():
    teachers = await retrieve_teachers()
    if teachers:
        return response_model(teachers, "Teachers data retrieved successfully")
    return response_model(teachers, "Empty list returned")


@teacher_router.get("/{id}", response_description="Teacher data retrieved")
async def get_teacher_data(id):
    teacher = await retrieve_teacher(id)
    if teacher:
        return response_model(teacher, "Teacher data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Teacher doesn't exist.")


@teacher_router.put("/{id}")
async def update_teacher_data(id: str, req: UpdateTeacherModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_teacher = await update_teacher(id, req)
    if updated_teacher:
        return response_model(
            "Teacher with ID: {} name update is successful".format(id),
            "Teacher name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the teacher data.",
    )


@teacher_router.delete("/{id}", response_description="Teacher data deleted from the database")
async def delete_teacher_data(id: str):
    deleted_teacher = await delete_teacher(id)
    if deleted_teacher:
        return response_model(
            "Teacher with ID: {} removed".format(id), "Teacher deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Teacher with id {0} doesn't exist".format(id)
    )
