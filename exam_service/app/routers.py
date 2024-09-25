from fastapi import APIRouter, HTTPException
from .models import Exam

router = APIRouter()

exams = []

@router.post("/exams/")
def create_exam(exam: Exam):
    exams.append(exam)
    return exam

@router.get("/exams/")
def get_exams():
    return exams

@router.get("/exams/{exam_id}")
def get_exam(exam_id: int):
    for exam in exams:
        if exam.id == exam_id:
            return exam
    raise HTTPException(status_code=404, detail="Exam not found")
