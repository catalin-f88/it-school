# Exercitiul 7
# numar = int(input("Introdu un numar: "))
# temp = numar
# rev=0
# while(numar > 0):
#     dig = numar%10
#     rev = rev*10+dig
#     numar = numar//10
# if(temp == rev):
#     print("Numarul este un palidrom!")
# else:
#     print("Numarul nu este un palindrom!")

# Exercitiul 1

# lista_prime = []

# for num in range(1, 100):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            lista_prime.append(num)

# print("Numerele prime in intervalul 1 - 100 sunt:", lista_prime)

# Exercitiul 2
# numar = range(1, 1000, 2)

# for i in numar:
#     print(i)

# Exercitiul 9
from random import randint

numar = randint(1, 300)

print("Incepe jocul!")
choice = int(input("Introduceti un numar intre 1 si 300: "))
while choice != numar:
    if (numar - choice) >= 50:
        print("Gheata")
    if (numar - choice) < 40:
        print("Frig")
    if (numar - choice) < 30:
        print("Rece")
    if (numar - choice) < 20:
        print("Caldut")
    if (numar - choice) < 10:
        print("Cald")
    if (numar - choice) < 5:
        print("Frige")
    if (numar - choice) < 2:
        print("Arde")
    choice = int(input("Introduceti un numar intre 1 si 300: "))

print("Felicitari! Ati ghicit numarul!")
print("Numarul generat a fost", numar)