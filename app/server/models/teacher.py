from typing import Optional

from pydantic import BaseModel, EmailStr, Field  # import at requirements.txt


class TeacherSchema(BaseModel):
    fullname: str = Field(...)  # In Pydantic, the ellipsis, ..., indicates that a Field is required.
    email: EmailStr = Field(...)
    dominant_subject: str = Field(...)
    number_of_class: int = Field(..., gt=0, le=5)  # validators greaterthan, lessthanorequal

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "dominant_subject": "Engineering",
                "number_of_class": 2
            }
        }


class UpdateTeacherModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    dominant_subject: Optional[str]
    number_of_class: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "dominant_subject": "Engineering",
                "number_of_class": 2
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
