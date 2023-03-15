list1 = [
    [1, 2],
    [3, 4, 2, 4],
    [2, 3, 3, 4]
]
for i in list1:
    try:
        val = i[2]
    except IndexError:
        print(f"Nu am gasit indexul 2 in lista {i}.")
    else:
        print(val)
    finally:
        print("--------------------")

print("END")