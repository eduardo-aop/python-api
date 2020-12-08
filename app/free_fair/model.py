from .config import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String

import uuid


class Fair(Base):
    __tablename__ = 'feira_livre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    long = Column(String)
    lat = Column(String)
    setcent = Column(String)
    area = Column(String)
    coddist = Column(String)
    distrito = Column(String)
    codsubpref = Column(String)
    regiao5 = Column(String)
    regiao8 = Column(String)
    nome_feira = Column(String)
    registro = Column(String)
    logradouro = Column(String)
    numero = Column(Integer)
    bairro = Column(String)
    referencia = Column(String)
