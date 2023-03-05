# a = "Titu"
# b = "Maiorescu"
# c = a + " " + b
# print(c)

# school = ["IT", "school", "2023"]
# string_final = " ".join(school)
# print(string_final)

# lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print(lorem[:10])
# print(lorem[-10:])

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf"
    "weee"
]

for i, v in enumerate(product_code_list):
    product_code_list[i] = v[:-1] + "x"

# for i in range(len(product_code_list)):
#     product_code_list[i] = product_code_list[i][:-1] + "x"
print(product_code_list)