# Exercitiul 1
numar = int(input("Introdu numarul: "))
if numar % 2 == 0:
    print("Numarul este par!")
else:
    print("Numarul este impar!")

# Exercitiul 2
raza = int(input("Introdu un numar: "))
print("Perimetrul cercului = ", str(2 * 3.14 * raza))

if raza >= 100:
    print("Aria cercului = ", str(3.14 * raza ** raza))

# Exercitiul 3
a = int(input("Introdu o valuare pentru a: "))
b = int(input("Introdu o valuare pentru b: "))
if a > b:
    print("a + b = ", str(a + b))
    print("a - b = ", str(a - b))
elif a == b:
    print("a la puterea b = ", str(pow(base=a, exp=b)))
else:
    print("a + b = ", str(a + b))

# Exercitiul 4
a = int(input("Introdu o valuare pentru a: "))
b = int(input("Introdu o valuare pentru b: "))
if a > b:
    print("a / b = ", str(a/b))
elif a <= b:
    print("b / a = ", str(b/a))

# Exercitiul 5
numar = str(input("Introdu un numar din 3 cifre: "))
if len(numar) != 3 or int(numar) < 0:
    print("Eroare.")
elif len(numar) == 3 and int(numar[-1:]) >= 5:
    print("Suma = ", int(numar) + int(numar[-1]))
else:
    print("Diferenta = ", int(numar) - int(numar[-1]))

