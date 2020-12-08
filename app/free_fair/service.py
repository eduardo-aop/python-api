from .repository import FreeFairRepository


class FreeFairService:

    def find_all(self):
        return FreeFairRepository().find_all()
