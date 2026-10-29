password = input("type a password: ")
print("your password has", len(password), "characters.")

has_number = False

has_capital = False

for character in password:
    if character.isdigit():
        has_number = True
    if character.isupper():
        has_capital = True
if len(password) < 8:
    print("too short add characters")
elif has_capital == False:
    print("add a capital letter to continue")
elif has_number == False:
    print("add numbers to continue")
else:
    print("perfect")
