# map
init_lst = [4, 56, 7, 5, 45]
new_lst = map(lambda x: x ** 2, init_lst)
new_list1 = [x ** 2 for x in init_lst]

for i in new_lst:
    print(i)

print(new_list1)

# enumerate
for i in enumerate(new_list1):
    print(f"Index: {i[0]} ... valoare {i[1]}")

# divmod
cat, rest = divmod(10, 3)
print(f"Catul = {cat} si restul = {rest}")

# zip
names = ["Alex", "Elena", "Victor"]
ids = ["23244", "23456", "74534"]

zp = zip(names, ids)
for i in zp:
    print(i)
