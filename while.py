# n = int(input("Introdu valoarea pentru n: "))
# c = 1

# while c <= n:
#     print("*" * c)
#     c += 1
# from random import randint

# numar = randint(1, 99)

# print("Incepe jocul!")
# choice = int(input("Introduceti un numar intre 1 si 99: "))
# while choice != numar:
#     if choice < numar:
#         print("+++")
#     else:
#         print("---")
#     choice = int(input("Introduceti un numar intre 1 si 99: "))

# print("Felicitari! Ati ghicit numarul!")
# print("Numarul generat a fost ", numar)

nr_bile = 300
bile_verzi = 0
nr_iteratie = 0
nr_crt = 1

while nr_iteratie < nr_bile:
    nr_iteratie += 1
    if nr_crt % 2 == 0:
        bile_verzi += 1
    nr_crt += 3
print(bile_verzi)


