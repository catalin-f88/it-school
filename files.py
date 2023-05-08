from pathlib import Path
from datetime import datetime

working_dir = Path('.') # current working directory

# print(working_dir)
# print(type(working_dir))

print(f"Current working directory: {working_dir.absolute()}")

script_path = Path(__file__)

print(f"Script path: {script_path.parent}")

# print(script_path.exists())

start_time_path = script_path.parent / "program_data" / "start_time"

# if not start_time_path.parent.exists():
    # start_time_path.parent.mkdir() # make directory

start_time_path.mkdir(exist_ok=True, parents=True)

print(start_time_path.is_dir())
print(start_time_path.is_file())

# w = write, r = read, a = append, wb = write binary, rb = read binary, ab = add binary
# fis1 = open(start_time_path / "test.txt", "w")

# fis1.close()
now = datetime.now()
now_file_name = now.strftime("%Y%m%d_%H%M%S.txt")

# context manager
with open(start_time_path / now_file_name, "w") as fout:
    fout.write("No errors!\n")

""" un script care citeste de la tastatura numele vostru si creati un fisier in
acelasi folder cu scriptul 
 
un script - un generator care va da numerele lui fibonaci - apelati next de 100 de ori 
pentru primele 100 de numere ale lui fibonacci si creati fisiere cu numere de la 1 la 100
si in fiecare sa punem 1 - primul, 2 - al doilea, toate intr-un folder fibonacci langa .py 

un script care afiseaza cand a fost rulat ultima data (read)"""


