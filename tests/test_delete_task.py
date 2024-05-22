from src.db.functions import db_add_task, db_delete_task, db_get_task
from src.db import Task


def test_delete_task(app, client):
    with app.app_context():
        task = Task(title="Тестовая таска", description="Это тестовая таска")
        created_task = db_add_task(task)
        db_delete_task(created_task.id)
        deleted_task = db_get_task(created_task.id)
        assert deleted_task is None