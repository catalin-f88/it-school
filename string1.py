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

# product_code_list = [
#     "mmf2",
#     "xdfr",
#     "ef3r",
#     "efc2",
#     "sddf"
#     "weee"
# ]

# for i, v in enumerate(product_code_list):
#     product_code_list[i] = v[:-1] + "x"

# # for i in range(len(product_code_list)):
# #     product_code_list[i] = product_code_list[i][:-1] + "x"
# print(product_code_list)

import_numbers = "today we had 280 clients."
# user_name = "mihai.dinu"

# print(import_numbers.capitalize())
# print(import_numbers.upper())
# print(import_numbers.lower())
# print(import_numbers.title())

# new_numbers = import_numbers.replace("clients", "costumers")
# print(new_numbers)

# new_numbers = import_numbers.replace("280", "300")
# print(new_numbers.title())

# for i in new_numbers:
#     print(i)

# template = "Salut <<USER>>! Bine ai venit! <<USER>> nu te-am mai vazut de mult!"
# user = input("Numele tau: ")
# greet_message = template.replace("<<USER>>", user)
# print(greet_message)


# lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# lorem2 = lorem.lower()

# words = lorem2.split(" ")

# for i, v in enumerate(words):
#     words[i] = v.strip(",.!?:;/ ")

# dictionar = {}

# for word in words:
#     dictionar[word] = words.count(word)

# for k, v in dictionar.items():
#     print(k, " --- ", v)


# files = ["mylog.txt", "audio1.mp3", "summer.mov", "notes.txt"]

# for i in files:
#     if i.endswith(".txt")
#         print(i)

# py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
# To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

# text = py_text.split(" ")

# for i in text:
#     if i.startswith("a") or i.startswith("A"):
#         print(i)

# user_code = "44563-mdinu-0001"
# prev = 0

# while prev != -1:
#     prev = user_code.find("-", prev + 1)
#     # print(prev)

# start = user_code.find("-")
# end = user_code.find("-", start + 1)

# print(user_code[start + 1:end])

commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300

    shuffle method"""

lines = commit.split("\n")
commit_id = lines[0].split(" ")[1]
a1 = lines[1].find(":")
a2 = lines[1].find("<")
print(lines[1][a1:a2].strip(": "), commit_id)

