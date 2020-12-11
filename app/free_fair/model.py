from ..config.config import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String

import uuid


class Fair(Base):
    __tablename__ = 'feira_livre'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, key='uuid_')
    id = Column(Integer)
    long = Column(String)
    lat = Column(String)
    setcens = Column(String)
    areap = Column(String)
    coddist = Column(String)
    distrito = Column(String)
    codsubpref = Column(String)
    subprefe = Column(String)
    regiao5 = Column(String)
    regiao8 = Column(String)
    nome_feira = Column(String)
    registro = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    referencia = Column(String)
