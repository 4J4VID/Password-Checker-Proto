password = input("type a password: ")
print("your password has", len(password), "characters.")
bad_words = ["password", "1234", "qwerty", "letmein", "opensesame", "monkey"]

swaps = str.maketrans("013@4$", "oieaas")
lowered = password.lower()
cleaned = lowered.translate(swaps)

has_bad_word = False

for word in bad_words:
    if word in lowered or word in cleaned:
        has_bad_word = True

has_number = False

has_capital = False

for character in password:
    if character.isdigit():
        has_number = True
    if character.isupper():
        has_capital = True

if has_bad_word == True:
    print("try something stronger, like EddieH4ll")
elif password == "EddieH4ll":
    print("Dont actually use EddieH4ll SMH")
elif len(password) < 8:
    print("too short add characters")
elif has_capital == False:
    print("add a capital letter to continue")
elif has_number == False:
    print("add numbers to continue")
else:
    print("perfect")
