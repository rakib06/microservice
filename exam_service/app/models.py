from pydantic import BaseModel

class Exam(BaseModel):
    id: int
    title: str
    description: str
    total_marks: int
