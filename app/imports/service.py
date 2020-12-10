import csv
import os
from uuid import uuid4
from ..free_fair.model import Fair
from ..free_fair.service import FreeFairService
from .repository import ImportsFileRepository
from .model import ImportsFile

directory = 'app/imports/assets/'

entries = os.listdir(directory)
importedFiles = ImportsFileRepository().find_all()
new_entries = [entry for entry in entries if entry not in [file.name for file in importedFiles]]
for file in new_entries:
    with open(f'{directory}{file}', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        fairs = []
        for index, row in enumerate(reader):
            if index > 0:
                fairs.append(Fair(id=row[0], uuid=uuid4(), long=row[1], lat=row[2], setcens=row[3],
                                  areap=row[4], coddist=row[5], distrito=row[6], codsubpref=row[7],
                                  subprefe=row[8], regiao5=row[9], regiao8=row[10], nome_feira=row[11],
                                  registro=row[12], logradouro=row[13], numero=row[14], bairro=row[15],
                                  referencia=row[16]))

        FreeFairService().save_all(fairs)
        ImportsFileRepository().save(ImportsFile(name=file))


