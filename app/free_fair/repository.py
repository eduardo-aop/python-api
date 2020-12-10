from ..config.config import session
from .model import Fair


class FreeFairRepository:

    def filter(self, nome_feira: str, distrito: str, regiao5: str, bairro: str):
        print('locura ====================')
        print(nome_feira)
        print(distrito)
        query_filter = []
        if nome_feira is not None:
            print(nome_feira)
            query_filter.append(Fair.nome_feira == nome_feira)

        if distrito is not None:
            query_filter.append(Fair.distrito == distrito)

        if regiao5 is not None:
            query_filter.append(Fair.regiao5 == regiao5)

        if bairro is not None:
            query_filter.append(Fair.bairro == bairro)

        return session.query(Fair).filter(*query_filter).all()

    def find_all(self):
        return session.query(Fair).all()

    def save(self, fair):
        session.add(fair)
        session.commit()

    def save_all(self, fairs):
        session.bulk_save_objects(fairs)
        session.commit()
