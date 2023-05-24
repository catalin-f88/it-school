import csv

with open("salarii.csv") as fin:
    # reader = csv.reader(fin.readlines(), delimiter=",", )
    reader = csv.DictReader(fin.readlines(), delimiter=",")
    reader_cp = list(reader)

# for line in reader:
#     # print(f"Full name: {line[0]} {line[1]}, net salary: {int(line[3]) * 0.45:.2f} RON")
#     print(f"Salariu brut: {line['salariu']}")
    
with open("salarii_nete.csv", "w") as fout:
    writer = csv.writer(fout)
    for line in reader_cp:
        writer.writerow([line[0], line[1]])

""" Creati un CSV nou care scrie doar nume, prenume, salariu net """