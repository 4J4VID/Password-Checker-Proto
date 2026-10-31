# Password Checker

A beginner Python program that checks how strong a password is. I'm building it one version at a time while I learn Python and cybersecurity fundamentals.

## What it does

You type in a password and the program tells you what's wrong with it, or says "perfect" if it passes every check. It looks for:

- Passwords that are too short (under 8 characters)
- Missing numbers
- Missing capital letters
- Common bad passwords like `password`, `1234`, and `qwerty`
- Lookalike tricks, like `M0nkeyBoy` (a zero instead of an "o")

## How to run it

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Download `password_checker_V5.py` from this repo
3. Open Command Prompt in the folder where you saved it
4. Type: `python password_checker_V5.py`

Example:

```
type a password: M0nkeyBoy
your password has 9 characters.
try something stronger, like EddieH4ll
```

## Version history

| Version | What I added | What I learned |
|---------|--------------|----------------|
| V1 | Length check (must be 8+ characters) | `input()`, `print()`, `len()`, `if/else` |
| V2 | Number check using a `for` loop | Looping through characters, `isdigit()` |
| V3 | Capital letter check | `isupper()`, flags (`True`/`False` variables) |
| V4 | Bad word list (`password`, `1234`, `qwerty`, and more) plus a joke message for `EddieH4ll` | Lists, `in`, `.lower()`, why the order of `if/elif` matters |
| V5 | Lookalike swap detection (`0`→`o`, `1`→`i`, `3`→`e`, `@`→`a`, `4`→`a`, `$`→`s`) | `str.maketrans()`, `.translate()`, debugging a variable that was built but never used |

## How the lookalike check works

Before searching the bad word list, the program makes a "cleaned" copy of the password: all lowercase, with
