# employees = [("Andrei", 5700), ("Mihai", 8900), ("Ioana", 5400)]
# employees_dict = {}

# for t in employees:
#     employees_dict[t[0]] = t[1]

# print(employees_dict)


# catalog = {
#     "Mircea": 9,
#     "Andrei": 5,
#     "Oana": 7,
#     "Ionut": 8
# }

# catalog["Gigel"] = 4
# catalog["Oana"] = 10

# print(catalog)

# dict_ages = {
#     "Mihai": 45,
#     "Andrei": 32,
#     "Ioana": 29
# }

# list_ages = list(dict_ages)
# print(sorted(list_ages, reverse = True))

# catalog = [
#     {"nume": "Elena", "note": [4, 8, 6]},
#     {"nume": "Mircea", "note": [7, 9, 5]},
#     {"nume": "Mirela", "note": [8, 9, 10]}
# ]

# def extract(x): 
#     return x[2]

# for i in catalog:
#     i["medie"] = sum(i["note"])/len(i["note"])

# sorted_list = sorted(catalog, key=lambda x: x["medie"])

# for student in sorted_list:
#     print(student["nume"], "note:", student["note"], "medie:", student["medie"])



rezultate_campionat = [
    {"echipa": "CFR Cluj", "meciuri_jucate": 36, "victorii": 22, "egaluri": 9, "infrangeri": 5},
    {"echipa": "FCSB", "meciuri_jucate": 36, "victorii": 21, "egaluri": 7, "infrangeri": 8},
    {"echipa": "Universitatea Craiova", "meciuri_jucate": 36, "victorii": 18, "egaluri": 11, "infrangeri": 7},
    {"echipa": "Sepsi Sfântu Gheorghe", "meciuri_jucate": 36, "victorii": 15, "egaluri": 11, "infrangeri": 10},
    {"echipa": "Astra Giurgiu", "meciuri_jucate": 36, "victorii": 14, "egaluri": 11, "infrangeri": 11},
    {"echipa": "CS Mioveni", "meciuri_jucate": 36, "victorii": 13, "egaluri": 12, "infrangeri": 11},
    {"echipa": "FC Argeș Pitești", "meciuri_jucate": 36, "victorii": 13, "egaluri": 9, "infrangeri": 14},
    {"echipa": "FC Botoșani", "meciuri_jucate": 36, "victorii": 12, "egaluri": 10, "infrangeri": 14},
    {"echipa": "Gaz Metan Mediaș", "meciuri_jucate": 36, "victorii": 11, "egaluri": 12, "infrangeri": 13},
    {"echipa": "FC Voluntari", "meciuri_jucate": 36, "victorii": 12, "egaluri": 8, "infrangeri": 16},
    {"echipa": "Academica Clinceni", "meciuri_jucate": 36, "victorii": 10, "egaluri": 12, "infrangeri": 14},
    {"echipa": "FC Hermannstadt", "meciuri_jucate": 36, "victorii": 10, "egaluri": 11, "infrangeri": 15}
]

for i in rezultate_campionat:
    i["punctaj"] = (i["victorii"]*3) + (i["egaluri"])

# print(rezultate_campionat)
sorted_list = sorted(rezultate_campionat, key=lambda x: x["punctaj"], reverse=True)
print("Echipa castigatoare este", sorted_list[0]["echipa"])
sorted_list_draws = sorted(rezultate_campionat, key=lambda x: x["egaluri"], reverse=True)
print("Echipa cu cele mai multe egaluri este", sorted_list_draws[0]["echipa"])
print("Podiumul campionatului este:", "1.", sorted_list[0]["echipa"], sorted_list[0]["punctaj"], "puncte", "2.", sorted_list[1]["echipa"], sorted_list[1]["punctaj"], "puncte", "3.", sorted_list[2]["echipa"], sorted_list[2]["punctaj"], "puncte")

# avand in vedere ca o victorie valoreaza 3 pct. si un egal 1 pct. 

# a) sa se adauge o cheie noua in fiecare dictionar, numele cheii este 'puncte' 
# iar ca valoare va avea numarul de puncte acumulate
# b) sa se afiseze numele echipei campioane
# c) sa se afiseze numele echipei cu ele mai multe egaluri
# d) sa se afiseze podiumul (nume si numar de pct)
