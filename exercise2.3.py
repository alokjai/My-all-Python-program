name, search = input("Enter your name  and character to find ").split(",")
# print(f"name length is {len(name)}")
# name = name.upper()
# search = search.upper()
# print(f"character count {name.count(search)}")

print(f"name length is {len(name)}")
print(f"character count {name.strip().lower().count(search.strip().lower())}")
