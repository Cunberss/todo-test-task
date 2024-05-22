import pydantic
from flask import Blueprint, request, jsonify

from src.db import Task
from src.db.functions import db_add_task, db_get_tasks, db_get_task, db_update_task, db_delete_task
from src.db.schemas import TaskCreate, TaskUpdate


tasks_bp = Blueprint(name='tasks', import_name=__name__, url_prefix='/tasks/')


@tasks_bp.post('')
def create_task():
    """
    Создание таски: валидация через pydantic. Обязательные поля: title: str. Опциональные: description: str
    """
    try:
        data = TaskCreate(**request.get_json())
    except pydantic.ValidationError as e:
        return jsonify(e.errors()), 400
    task = db_add_task(Task(title=data.title, description=data.description))
    return task.to_dict(), 200


@tasks_bp.get('')
def get_tasks():
    """
    Возвращает таскс-список или пустой список, если их нет.
    """
    tasks = [task.to_dict() for task in db_get_tasks()]
    return jsonify(tasks), 200


@tasks_bp.get('<int:task_id>')
def get_task(task_id: int):
    """
    Возвращает таску если она существует или возвращает ошибку 404 (not found)
    """
    task = db_get_task(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@tasks_bp.put('<int:task_id>')
def update_task(task_id):
    """
    Апдейт таски: Валидация через pydantic. Опциональные поля: title: str, description: str
    """
    task = db_get_task(task_id)
    if task:
        try:
            data = TaskUpdate(**request.get_json())
        except pydantic.ValidationError as e:
            return jsonify(e.errors()), 400

        if data.title is not None:
            task.title = data.title
        if data.description is not None:
            task.description = data.description

        task = db_update_task(task)

        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@tasks_bp.delete('<int:task_id>')
def delete_task(task_id):
    """
    Удаляет таску если она существует или возвращает 404 (not found)
    """
    task = db_get_task(task_id)
    if task:
        db_delete_task(task_id)
        return jsonify({'success': 'Task delete'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404
