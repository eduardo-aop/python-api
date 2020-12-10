from ..config.config import Base
from sqlalchemy import Column, Integer, String


class ImportsFile(Base):
    __tablename__ = 'import_files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
