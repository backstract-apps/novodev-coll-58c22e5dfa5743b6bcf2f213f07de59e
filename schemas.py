from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Student(BaseModel):
    user_id: int
    name: str
    email: str
    password: str
    role: str


class ReadStudent(BaseModel):
    user_id: int
    name: str
    email: str
    password: str
    role: str
    class Config:
        from_attributes = True


