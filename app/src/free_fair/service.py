from typing import List

from .repository import FreeFairRepository
from .model import Fair

import uuid


class FreeFairService:

    def filter(self, nome_feira: str, distrito: str, regiao5: str, bairro: str):
        return FreeFairRepository().filter(nome_feira=nome_feira,
                                           distrito=distrito,
                                           regiao5=regiao5,
                                           bairro=bairro)

    def find_by_uuid(self, fair_uuid: uuid.uuid4):
        return FreeFairRepository().find_by_uuid(fair_uuid=fair_uuid)

    def save_all(self, fairs: List[Fair]):
        FreeFairRepository().save_all(fairs)

    def save(self, fair: Fair):
        FreeFairRepository().save(fair)

    def delete(self, fair_uuid: uuid.uuid4):
        FreeFairRepository().delete(fair_uuid)

    def update(self, fair_uuid: uuid.uuid4, fair: Fair):
        FreeFairRepository().update(fair_uuid, fair)
