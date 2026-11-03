password = input("type a password: ")
print("your password has", len(password), "characters.")
with open("common_passwords.txt") as file:
    bad_words = file.read().split()
with open("10k-most-common.txt") as file:
    big_list = file.read().split()

swaps = str.maketrans("013@4$", "oieaas")
lowered = password.lower()
cleaned = lowered.translate(swaps)
stripped = lowered.rstrip("0123456789")

has_bad_word = False

for word in bad_words:
    if word in lowered or word in cleaned:
        has_bad_word = True

if lowered in big_list or cleaned in big_list or stripped in big_list:
    has_bad_word = True

has_number = False

has_capital = False

has_symbol = False

has_lower = False

score = 0
if has_number == True:
    score = score + 1
if has_capital == True:
    score = score + 1
if has_lower == True:
    score = score + 1
if has_symbol == True:
    score = score + 1

for character in password:
    if character.isdigit():
        has_number = True
    if character.isupper():
        has_capital = True
    if not character.isalnum():
        has_symbol = True
    if character.islower():
        has_lower = True

if has_number == True:
    score = score + 1
if has_capital == True:
    score = score + 1
if has_lower == True:
    score = score + 1
if has_symbol == True:
    score = score + 1


if has_bad_word == True:
    print("try something stronger, like EddieH4ll#")
elif password == "EddieH4ll#":
    print("Dont actually use EddieH4ll SMH")
elif len(password) < 8:
    print("too short add characters")
elif has_capital == False:
    print("add a capital letter to continue")
elif has_number == False:
    print("add numbers to continue")
elif has_symbol == False:
    print("add a symbol to continue")
elif has_lower == False:
    print("add a lowercase letter to continue")
else:
    print("perfect")

if has_bad_word == True or len(password) <8:
    strength = "weak"
elif score == 4:
    strength = "best"
elif score == 3:
    strength = "decent"
elif score == 2:
    strength = "risky"
elif score == 1:
    strength = "weak"
elif score == 0:
    strength = "weak"

print("strength:", strength)
