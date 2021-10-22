from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi_pagination import Page, add_pagination, paginate


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

from .security import (
    verify_token
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/news/", response_model=Page[schemas.News])
def get_news(from_:str = "2021-01-01", to_: str = "2021-01-08", db: Session = Depends(get_db),
                         user_entity: str = Depends(verify_token)):
    news = crud.get_news(db, from_=from_, to_=to_)
    return paginate(news)

add_pagination(app)