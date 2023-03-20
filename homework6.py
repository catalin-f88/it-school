# number1 = input("Introdu un numar: ")
# number2 = input("Introdu un numar: ")

# def division(number1, number2):
#     try:
#         cat = int(number1) // int(number2)
#         rest = int(number1) % int(number2)
#         print(f"Catul impartirii dintre {number1} si {number2} este {cat}")
#         print(f"Restul impartirii dintre {number1} si {number2} este {rest}")
#     except (ZeroDivisionError, ValueError):
#         print("Introdu numere diferite de 0 la ambele cereri!")

# # division(number1, number2)

# def power(number1):
#     try:
#         pow_res = int(number1) ** int(number1)
#         print(f"{number1} ridicat la puterea {number1} este {pow_res}")
#     except ValueError:
#         print("Valoarea introdusa nu este un numar intreg!")

# # power(number1)

# def sum(number1, number2):
#     try:
#         sum_res = int(number1) + int(number2)
#         print(f"Adunarea dintre {number1} si {number2} este {sum_res}")
#     except ValueError:
#         print("Valoarea introdusa nu este un numar intreg!")

# sum(number1, number2)


list = input("Introdu numere, separate prin virgula: ")
numbers = [x for x in list.split(",")]
try: 
    result = 0
    for x in range(0, len(numbers)):
        result = result + int(numbers[x])
    print(f"Suma elementelor introduse este: {result}")

except ValueError:
    print("Introdu doar numere intregi, separate prin virgula!")
