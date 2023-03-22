# colors = {"red", "brown", "blue", "white"}
# print(colors)


# colors.add("black")
# colors.remove("white")
# print(colors)

list1 = [22, 34, 56, 65, 45]
list2 = [23, 34, 65, 55]
common = set(list1).intersection(set(list2))
print(common)
difference = set(list1).difference(set(list2))
print(difference)
set1 = set(list1)
set1.update(list2)

print(set1)

