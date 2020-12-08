from .config import engine
from .model import Fair


class FreeFairRepository:

    def find_all(self):
        return engine.execute('SELECT * FROM feira_livre').all()
