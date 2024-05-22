import pytest

from src.db.functions import db_add_task, db_update_task, db_get_task, db_delete_task
from src.db import Task


def test_update_task(app, client):
    with app.app_context():
        task = Task(title="Тестовая Таска", description="Это тестовая таска")
        created_task = db_add_task(task)
        created_task.title = "Обновленная Тестовая Таска"
        updated_task = db_update_task(created_task)
        assert updated_task.title == "Обновленная Тестовая Таска"
        db_delete_task(created_task.id)