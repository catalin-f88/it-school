# template = "This product is: %s $"

# name = "Mihai"
# print("Name: %s %s" % (name, name))

user_info = {
    "first_name": "mihai",
    "last_name": "dinu",
    "address": "bucharest",
    "country": "ro"
}

doc1 = (f"Subsemnatul, {user_info['first_name'].capitalize()} "
        f"{user_info['last_name'].capitalize()}, ")

print(doc1)