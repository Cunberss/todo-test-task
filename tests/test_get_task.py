from src.db.functions import db_get_task, db_add_task, db_delete_task
from src.db import Task


def test_get_task(app, client):
    with app.app_context():
        task = Task(title="Тестовая Таска", description="Это тестовая таска")
        created_task = db_add_task(task)
        retrieved_task = db_get_task(created_task.id)
        assert retrieved_task is not None
        assert retrieved_task.id == created_task.id
        assert retrieved_task.title == "Тестовая Таска"
        assert retrieved_task.description == "Это тестовая таска"
        db_delete_task(created_task.id)


def test_get_task_not_found(app, client):
    with app.app_context():
        retrieved_task = db_get_task(99999)
        assert retrieved_task is None
