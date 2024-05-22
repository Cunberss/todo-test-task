from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """
    Валидация создания таски
    """
    title: str = Field(..., max_length=255)
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    """
    Валидация обновления таски
    """
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None

