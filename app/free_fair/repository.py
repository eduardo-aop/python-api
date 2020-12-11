from typing import List

from ..config.config import session
from .model import Fair

import uuid


class FreeFairRepository:

    def filter(self, nome_feira: str, distrito: str, regiao5: str, bairro: str):
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

    def find_by_uuid(self, fair_uuid: uuid.uuid4):
        return session.query(Fair).filter(Fair.uuid == fair_uuid).first()

    def save(self, fair: Fair):
        session.add(fair)
        session.commit()

    def save_all(self, fairs: List[Fair]):
        session.bulk_save_objects(fairs)
        session.commit()

    def delete(self, fair_uuid: uuid.uuid4):
        deleted = session.query(Fair).filter(Fair.uuid == fair_uuid).delete()
        session.commit()
        return deleted if deleted != 0 else None

    def update(self, fair_uuid: uuid.uuid4, fair: Fair):
        updated = session.query(Fair).filter(Fair.uuid == fair_uuid).update(fair)
        session.commit()
        return updated if updated != 0 else None
