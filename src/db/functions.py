from typing import List

from sqlalchemy import desc, select, delete

from src.db import Task
from src.db.base import get_session


def db_add_task(task: Task) -> Task:
    """
    Функция добавления таски в бд. Возвращает добавленный объект
    """
    with get_session() as session:
        session.add(task)
        session.commit()
        session.refresh(task)
    return task


def db_get_tasks() -> List[Task]:
    """
    Возвращает все таски из базы данных отсортированные в порядке убывания id
    """
    with get_session() as session:
        query = select(Task).order_by(desc(Task.id))
        result = session.execute(query)
        return result.scalars().all()


def db_get_task(task_id: int) -> Task:
    """
    Возвращает таску по её id или объект None
    """
    with get_session() as session:
        query = select(Task).where(Task.id == task_id)
        result = session.execute(query)
        return result.scalars().one_or_none()


def db_update_task(task: Task) -> Task:
    """
    Функция обновления таски в базе данных. Возвращает обновленную таску
    """
    with get_session() as session:
        session.merge(task)
        session.commit()
    return task


def db_delete_task(task_id: int):
    """
    Функция удаления таски
    """
    with get_session() as session:
        query = delete(Task).where(Task.id == task_id)
        session.execute(query)
        session.commit()
