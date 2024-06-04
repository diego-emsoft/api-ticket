from pydantic import BaseModel


class StatusBase(BaseModel):
    descricao: str
    finalizacao: str
    padrao: str


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int

    class Config:
        from_attributes = True
