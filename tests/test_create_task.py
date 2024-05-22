import pytest
from src.db import Task
from src.db.functions import db_add_task, db_get_task, db_delete_task


def test_create_task(app, client):
    with app.app_context():
        task = Task(title="Тестовая таска", description="Это тестовая таска")
        created_task = db_add_task(task)
        assert created_task.id is not None
        assert created_task.title == "Тестовая таска"
        assert created_task.description == "Это тестовая таска"
        db_delete_task(created_task.id)


def test_create_task_invalid_data(app, client):
    with app.app_context():
        task = Task(title=None, description="Это тестовая таска")
        with pytest.raises(Exception):
            db_add_task(task)