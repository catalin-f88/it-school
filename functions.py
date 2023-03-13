# def greet(name):
#     """Say formatted message to user."""
#     print("*" * 30)
#     print(f"Hello, {name}!")
#     print("*" * 30)

# greet("Catalin")

# x = int(input("Introdu numar: "))

# def verify_parity(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# for i in range(0, 51):
#     if not verify_parity(i):
#         print(i)


# def range_product(start, stop):
#     """Calculate the product for numbers between start and stop."""
#     prod = 1
#     for i in range(start, stop):
#         prod *= i
#     return prod

# start_in = int(input("Introdu numar: "))
# stop_in = int(input("Introdu numar: "))

# print(f"Produsul numerelor din intervalul {start_in} si {stop_in} este {range_product(start_in, stop_in)}")



inaltime = float(input("Introdu un numar (inaltime): "))
latime = float(input("Introdu un numar (latime): "))
lungime = float(input("Introdu un numar (lungime): "))
grosime = float(input("Introdu un numar (grosime): "))

def pret_cutii(inaltime, latime, lungime, grosime):
    # if not isinstance(latime, float):
    #     return 0
    # if not isinstance(inaltime, float):
    #     return 0
    # if not isinstance(lungime, float):
    #     return 0
    # if not isinstance(grosime, float):
    #     return 1
    
    pret = inaltime * latime * lungime * 25
    if grosime == 2:
        return pret * 1.10
    elif grosime == 3:
        return pret * 1.20
    return pret

print(f"Pretul unei cutii cu inaltime {inaltime}, latime {latime}, lungime {lungime} si grosime {grosime} este {pret_cutii(inaltime,latime,lungime,grosime):.2f} lei.")

