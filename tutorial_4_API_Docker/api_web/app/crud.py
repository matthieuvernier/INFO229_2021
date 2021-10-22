from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas

def get_news(db: Session, from_: str = '2021-10-20', to_: str = '2021-10-21', limit: int = 100):
    return db.query(models.News).filter(and_(models.News.date >= from_, models.News.date < to_)).limit(limit).all()
