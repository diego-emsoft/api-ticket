from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Status(Base):
    __tablename__ = "STATUS"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    finalizacao = Column(String, index=True)
    padrao = Column(String, index=True)
