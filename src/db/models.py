from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Text
from src.db.base import Base


class Task(Base):
    """
    Модель для базы данных
    """
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """
        Возвращает экземпляр класса в виде словаря
        """
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
                }
