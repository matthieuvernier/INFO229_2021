from typing import Dict, Any, Type
from typing import List, Optional
from datetime import datetime, date


from pydantic import BaseModel, Field


class News(BaseModel):
    id_news: int
    url: str
    title: str
    date: date
    media_outlet: str
    category: str

    class Config:
        orm_mode = True
        allow_mutation = True

