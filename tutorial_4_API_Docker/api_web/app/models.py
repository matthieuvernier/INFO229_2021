from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
import ast
from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id_news = Column(Integer, primary_key=True, index=True)
    url = Column(Text(), unique=False, index=False)
    title = Column(Text(), unique=False, index=False)
    date = Column(Date(), unique=False, index=True)
    media_outlet = Column(String(), unique=False, index=False)
    category = Column(String(), unique=False, index=False)