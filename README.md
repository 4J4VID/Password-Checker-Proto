[password_checker.py](https://github.com/user-attachments/files/34125398/password_checker.py)
# Password-Checker-Proto
Small project for expericence
password = input("type a password: ")
print("your password has", len(password), "characters.")

if len(password) < 8:
    print("too short add characters")
else:
    print("perfect")
