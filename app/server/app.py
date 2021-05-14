from fastapi import FastAPI

from app.server.routes.student import student_router as student_router
from app.server.routes.teacher import teacher_router

app = FastAPI()

app.include_router(student_router, tags=['Student'], prefix='/student')
app.include_router(teacher_router, tags=['Teacher'], prefix='/teacher')


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
