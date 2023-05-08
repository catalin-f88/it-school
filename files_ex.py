from pathlib import Path
import os
from datetime import datetime
import sys

ROOT = Path(__file__).parent
file_path = ROOT / "amenzi.txt"
amenzi_dir = ROOT / "amenzi"
AMENDA_TEMPLATE = """
Stimate proprietar,

In data de {data} autovehiculul cu numarul de inmatriculare {numar} a fost
identificat circuland pe drumurile publice fara Rovigneta valabila.

Amenda: {amenda} RON"""

try:
    amenzi_dir.mkdir(exist_ok=True)
except OSError as err:
        sys.exit(1)

def get_plate_numbers(file):
    try:
        with open(file, "r") as fin:
            numbers = fin.readlines()
            for i, v in enumerate(numbers):
                numbers[i] = v.strip("\n\r\t ")
            return numbers
    except OSError as err:
        sys.exit(1)

def gen_text(numar, amenda):
     now = datetime.now().strftime("%d.%m.%Y")
     return AMENDA_TEMPLATE.format(data=now, numar=numar, amenda=amenda)

numere = get_plate_numbers(file_path)

def convert_number(number):
    return number.lower().replace("-", "_")

for i in numere:
    folder_name = i.split("-",)[0]
    folder_path = amenzi_dir / folder_name
    folder_path.mkdir(exist_ok=True)
    file_name = f"amenda_{convert_number(i)}.txt"
    file_path = folder_path / file_name
    with open(file_path, "w") as fout:
         fout.write(gen_text(i, 100))

""" sysargs pentru argumente, amenda sa fie luata din comanda """