# user_info = {
#     "first_name": "mihai",
#     "last_name": "dinu",
#     "address": "bucharest",
#     "country": "ro"
# }

# USER_TEMPLATE = "Nume: {0} Prenume: {1} Country: {2}"
# print(USER_TEMPLATE.format(
#     user_info["last_name"], user_info["first_name"], user_info["country"]))

# auto = {
#     "marca": "Audi",
#     "model": "A4",
#     "usi": 4
# }

# AUTO_TEMPLATE = "Detin o masina marca {} model {} si are {} usi."
# print(AUTO_TEMPLATE.format(auto["marca"], auto["model"], auto["usi"]))

ticket = {
    "s_plecare": "Bucuresti Nord",
    "s_sosire": "Iasi",
    "data_plecare": "27.02.2023",
    "data_sosire": "27.02.2023",
    "ora_plecare": "19:30",
    "ora_sosire": "23:30",
    "pret": 98.4545974,
    "loc": True,
    "vagon": "2",
    "scaun": "34"
}

print("~" * 70)
print("{:-^70}".format(ticket["s_plecare"]))
print("Data plecare:{:>57}".format(ticket["data_plecare"]))
print("Ora plecare:{:>58}".format(ticket["ora_plecare"]))
print("{:-^70}".format(ticket["s_sosire"]))
print("Data sosire:{:>58}".format(ticket["data_sosire"]))
print("Ora sosire:{:>59}".format(ticket["ora_sosire"]))

if ticket["loc"]:
    print("{:*^70}".format(" Detalii loc "))
    print("*{:^68}*".format(f"Vagon: {ticket['vagon']}"))
    print("*{:^68}*".format(f"Scaun: {ticket['scaun']}"))
    print("*" * 70)

print("Pret: {:.4} RON".format(ticket["pret"]))
print("~" * 70)

TEMPLATE_TREN = "Trenul pleaca din {s_plecare} la data de {data_plecare} ora {ora_plecare} si ajunge la {s_sosire} in data de {data_sosire} la ora {ora_sosire}."
print(TEMPLATE_TREN.format(**ticket))
