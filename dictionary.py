# contact = {
#     "nume": "Radu",
#     "prenume": "Alex",
#     "tel": "08274243353"
# }
# print(contact["nume"], contact["prenume"])

# dict1 = {
#     "key1": 1,
#     "key2": {
#         "key1": 1,
#         "key2": ["elem1", "elem2"]
#     }
# }

# print(dict1["key2"]["key2"][1])

# dict2 = dict1["key2"]
# print(dict2)

# del dict1["key2"]

# students_grades = {
#     'Ana': 9.5,
#     'Ioan': 8.0,
#     'Maria': 7.5,
#     'Andrei': 9.0,
#     'Elena': 10.0
# }
# nota = students_grades.get("Ionut")

# if nota is not None:
#     print(nota)
# else:
#     print("Studentul nu exista")

# for key in students_grades.keys():
#     print(key)

# for value in students_grades.values():
#     print(value)

# for i,j in students_grades.items():
#     print(i, "/", j)

# dict1 = {
#     "Catalin": 34,
#     "Mihai": 29,
#     "Marian": 32
# }

# for k, v in dict1.items():
#     print(k, "/", v)

# students_grades = {
#     "Alex": [7, 8, 9],
#     "Andrei": [4, 9, 5],
#     "Mircea": [10, 8, 5]
# }

# for k, v in students_grades.items():
#     print(k, sum(v) / len(v))

# students_grades = {
#     'Ana': 9.5,
#     'Ioan': 8.0,
#     'Maria': 7.5,
#     'Andrei': 9.0,
#     'Elena': 10.0
# }

# # print(sorted(students_grades.items()))

# # for k, v in sorted(students_grades.items()):
# #     print(k, v)

# def extract(x):
#     return x[1]

# for k, v in sorted(students_grades.items(), key=extract, reverse=True):
#     print(k, v)
dict1 = {
    "Catalin": 34,
    "Mihai": 29,
    "Stefan": 32
}
lista = list(dict1.keys())
print(sorted(lista, reverse=True))

# catalog = [
#     {
#     "nume": "Elena",
#     "matematica": 10,
#     "biologie": 8,
#     "sport": 5,
#     "chimie": 9
#     },
#     {
#     "nume": "Andrei",
#     "matematica": 7,
#     "biologie": 5,
#     "sport": 9,
#     "chimie": 7
#     },
#     {
#     "nume": "Mircea",
#     "matematica": 4,
#     "biologie": 5,
#     "sport": 10,
#     "chimie": 7
#     },
#     {
#     "nume": "Lucian",
#     "matematica": 8,
#     "biologie": 9,
#     "sport": 10,
#     "chimie": 9
#     },
#     {
#     "nume": "Gigel",
#     "matematica": 10,
#     "biologie": 8,
#     "sport": 7,
#     "chimie": 9
#     }
# ]