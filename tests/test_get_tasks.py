from src.db.functions import db_get_tasks, db_add_task, db_delete_task
from src.db import Task


def test_get_tasks(app, client):
    with app.app_context():
        task1 = Task(title="Test Task 1", description="This is a test task")
        task2 = Task(title="Test Task 2", description="This is another test task")
        db_add_task(task1)
        db_add_task(task2)
        tasks = db_get_tasks()
        assert len(tasks) >= 2
        db_delete_task(task1.id)
        db_delete_task(task2.id)