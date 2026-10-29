password = input("type a password: ")
print("your password has", len(password), "characters.")

if len(password) < 8:
    print("too short add characters")
else:
    print("perfect")
