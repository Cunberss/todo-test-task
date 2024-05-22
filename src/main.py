from flask import Flask
from src.routes.tasks_router import tasks_bp


def build_app():
    """
    Инициализирует Flask-приложение и регистрирует роутер
    """
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)
    return app


flask_app = build_app()

if __name__ == '__main__':
    flask_app.run()
