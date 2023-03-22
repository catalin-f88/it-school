# user_ids = [324, 345, 536, 64, 4]
# print(user_ids[3])
# print(len(user_ids))
# print(user_ids[len(user_ids) - 1])
# print(user_ids[-1])

# for i in range(len(user_ids)):
#     print("Index:", i, " Valoare:", user_ids[i])


# for i in enumerate(user_ids):
#     print("Index:", i[0], " Valoare:", i[1])

# students = []

# students.append("Mihai")

# print(students)
# print(len(students))


# alfabet = []

# for i in range(65, 91):
#     alfabet.append(chr(i))

# print(alfabet)

# temp = [33, 22, 34, 21, 22]
# to_remove = 22

# print(to_remove in temp)
# print(to_remove, "apare de ", temp.count(to_remove), "ori")

# while to_remove in temp:
#     temp.remove(to_remove)
# print(temp)
# temp.reverse()
# temp(min)
# temp(max)


temperaturi = [91, 61, 80, 5, -44, -39, -87, 52, -68, -7, -25, -82, 1, 60, -45, -83, 9, 81, 54, -30, 49, -39, -65, -57, 18, 57, -70, -100, -53, 36, -69, 93, -82, 89, 90, -89, 70, 64, -18, -99, 68, -49, 13, -96, -5, 83, 98, 57,
               26, -27, 31, 54, 45, 7, -62, 56, 66, 82, -79, 50, -54, -79, -75, 30, 43, 81, 23, -44, -15, 3, 9, -67, -80, 77, 10, -22, -18, -47, 57, 21, -98, -37, 83, -62, 25, 65, -69, 15, -75, -9, 66, -79, 15, -32, -54, 32, -3, -89, -33, 28]

# temp_asc = sorted(temperaturi)
# temp_desc = sorted(temperaturi, reverse = True)

# lista_mici = []
# lista_mari = []

# for i in range(len(temperaturi)):
#     if i < 2:
#         lista_mici.append(temp_asc[i])

# for i in range(len(temperaturi)):
#     if i < 2:
#         lista_mari.append(temp_desc[i])

# print("Cele mai mici temperaturi sunt:", lista_mici)
# print("Cele mai mari temperaturi sunt:", lista_mari)
# print("Cea mai mica temperatura este: ", min(temperaturi))
# print("Cea mai mare temperatura este: ", max(temperaturi))


# words = ['Python', 'is', 'an', 'easy', 'to', 'learn', 'powerful', 'programming', 'language', 'It', 'has', 'efficient', 'high-level', 'data', 'structures', 'and', 'a', 'simple', 'but', 'effective', 'approach', 'to', 'object-oriented', 'programming', 'Python’s', 'elegant', 'syntax', 'and', 'dynamic', 'typing', 'together', 'with', 'its', 'interpreted', 'nature', 'make', 'it', 'an', 'ideal', 'language', 'for', 'scripting', 'and', 'rapid', 'application', 'development', 'in', 'many', 'areas', 'on', 'most', 'platforms', 'The', 'Python', 'interpreter', 'and', 'the', 'extensive', 'standard', 'library', 'are', 'freely', 'available', 'in', 'source', 'or', 'binary', 'form', 'for', 'all', 'major', 'platforms', 'from', 'the', 'Python', 'web', 'site', 'https://www.python.org', 'and', 'may', 'be', 'freely', 'distributed', 'The', 'same', 'site', 'also', 'contains', 'distributions', 'of', 'and', 'pointers', 'to', 'many', 'free', 'third', 'party', 'Python', 'modules', 'programs', 'and', 'tools', 'and', 'additional', 'documentation', 'The', 'Python', 'interpreter', 'is', 'easily', 'extended', 'with', 'new', 'functions', 'and', 'data', 'types', 'implemented', 'in', 'C', 'or', 'C++',
#          '(or', 'other', 'languages', 'callable', 'from', 'C)', 'Python', 'is', 'also', 'suitable', 'as', 'an', 'extension', 'language', 'for', 'customizable', 'applications', 'This', 'tutorial', 'introduces', 'the', 'reader', 'informally', 'to', 'the', 'basic', 'concepts', 'and', 'features', 'of', 'the', 'Python', 'language', 'and', 'system', 'It', 'helps', 'to', 'have', 'a', 'Python', 'interpreter', 'handy', 'for', 'hands-on', 'experience', 'but', 'all', 'examples', 'are', 'self-contained', 'so', 'the', 'tutorial', 'can', 'be', 'read', 'off-line', 'as', 'well', 'For', 'a', 'description', 'of', 'standard', 'objects', 'and', 'modules', 'see', 'The', 'Python', 'Standard', 'Library', 'The', 'Python', 'Language', 'Reference', 'gives', 'a', 'more', 'formal', 'definition', 'of', 'the', 'language', 'To', 'write', 'extensions', 'in', 'C', 'or', 'C++', 'read', 'Extending', 'and', 'Embedding', 'the', 'Python', 'Interpreter', 'and', 'Python/C', 'API', 'Reference', 'Manual', 'There', 'are', 'also', 'several', 'books', 'covering', 'Python', 'in', 'depth', 'This', 'tutorial', 'does', 'not', 'attempt', 'to', 'be', 'comprehensive', 'and', 'cover', 'every', 'single', 'feature', 'or', 'even', 'every', 'commonly', 'used', 'feature', 'Instead', 'it', 'introduces', 'many', 'of', 'Python’s', 'most', 'noteworthy', 'features', 'and', 'will', 'give', 'you', 'a', 'good', 'idea', 'of', 'the', 'language’s', 'flavor', 'and', 'style', 'After', 'reading', 'it', 'you', 'will', 'be', 'able', 'to', 'read', 'and', 'write', 'Python', 'modules', 'and', 'programs', 'and', 'you', 'will', 'be', 'ready', 'to', 'learn', 'more', 'about', 'the', 'various', 'Python', 'library', 'modules', 'described', 'in', 'The', 'Python', 'Standard', 'Library']
# result = []

# for word in words:
#     if word not in result:
#         result.append(word)
#         print(word, "...", words.count(word))

# list slicing
# print(len(temperaturi))
# new_temp = temperaturi[-20:]
# # print(len(new_temp))
# print(new_temp)

# list comprehension
new_list1 = [abs(i) for i in temperaturi if i < 0]
print(new_list1)
