from .repository import FreeFairRepository


class FreeFairService:

    def filter(self, nome_feira: str, distrito: str, regiao5: str, bairro: str):
        return FreeFairRepository().filter(nome_feira=nome_feira,
                                           distrito=distrito,
                                           regiao5=regiao5,
                                           bairro=bairro)

    def find_all(self):
        return FreeFairRepository().find_all()

    def save_all(self, fairs):
        FreeFairRepository().save_all(fairs)

    def save(self, fair):
        FreeFairRepository().save(fair)
