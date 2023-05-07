from db import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class ClientModel(db.Model):
    __tablename__ = "clients"

    id = db.Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    app_version = Column(String(10), nullable=False)
    added_date = Column(DateTime, default=datetime.utcnow)
