from ..config.config import session
from .model import ImportsFile


class ImportsFileRepository:
    def find_all(self):
        return session.query(ImportsFile).all()

    def save(self, file):
        session.add(file)
        session.commit()
