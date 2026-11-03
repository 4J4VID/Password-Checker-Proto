# Password Checker

A Python program that checks how strong a password is, built one version at a time while I learn Python and cybersecurity fundamentals. It now has 11 versions, an automatic test file, and a real list of common passwords.

## What it does

You type a password (the screen shows nothing while you type, like a PIN pad) and the program tells you the first problem it finds, or says "perfect". It checks for:

- Passwords that are too short (under 8 characters)
- Missing number, capital letter, lowercase letter, or symbol
- Common bad passwords, from a small list plus the 10,000 most common passwords
- Lookalike tricks, like `M0nkeyBoy` (a zero instead of an "o")
- Common passwords with numbers added on the end, like `Sunshine1`

It also gives a strength level:

| Level | When |
|-------|------|
| weak | Bad password, shorter than 8 characters, or 0 to 1 points |
| risky | 2 points |
| decent | 3 points |
| best | 4 points |

A password earns 1 point each for having a number, a capital letter, a lowercase letter, and a symbol.

Example run (typing is hidden, so the password never appears on screen):

```
type a password:
your password has 11 characters.
perfect
strength: best
```

## How to run it

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Download these files into one folder:
   - `password_checker_V11.py`
   - `common_passwords.txt`
   - `10k-most-common.txt`
3. Open Command Prompt in that folder
4. Type: `python password_checker_V11.py`

## Run the tests

`test_checker.py` runs 18 test passwords through the checker and prints PASS or FAIL for each one. It needs only Python, with nothing to install.

1. Put `test_checker.py` in the same folder as the files above.
2. Open Command Prompt in that folder.
3. Run:

```
python test_checker.py
```

Real output from my computer:

```
Testing: password_checker_V11.py
------------------------------------------------------------------------------
RESULT PASSWORD      WHAT IT TESTS                        NOTES
------------------------------------------------------------------------------
PASS   Zebra7Lamp#   all rules pass
PASS   Zebra7Lamp    no symbol
PASS   zebra7lamp#   no capital letter
PASS   ZEBRA7LAMP#   no lowercase letter
PASS   Zebralamps#   no number
PASS   zebra7lamps   no capital, no symbol
PASS   zebralamps    only lowercase letters
PASS   Zb7           too short
PASS   Mypassword9   bad word inside the password
PASS   Qwerty123X    another bad word
PASS   Zebra1234     bad word '1234' (needs lowered)
PASS   M0nkeyboy     lookalike swap 0 -> o
PASS   P@ssw0rd99    lookalike swaps @ and 0
PASS   L3tm31n7X     lookalike swaps 3 -> e, 1 -> i
PASS   Sunshine      exact match on the big list
PASS   Sunshine1     big list + number on the end
PASS   Sunshine99    big list + two numbers on the end
PASS   EddieH4ll#    joke message
------------------------------------------------------------------------------
18 passed, 0 failed, 18 total
All tests passed.
```

If a test fails, the NOTES column says what was expected. To test an older version, give its file name, like `python test_checker.py password_checker_V9.py`. Older versions don't print a strength level, so that check is skipped for them.

## How it works

The program makes three cleaned-up copies of the password before checking the lists:

| Copy | What it does | Example |
|------|--------------|---------|
| `lowered` | all lowercase | `Sunshine1` becomes `sunshine1` |
| `cleaned` | lowercase, with lookalikes swapped back to letters | `M0nkeyBoy` becomes `monkeyboy` |
| `stripped` | lowercase, with numbers removed from the end | `sunshine99` becomes `sunshine` |

It checks the small list by asking "is a bad word hiding *inside* the password?", and the 10,000-password list by asking "is the password *exactly* on the list?" Exact matching is used for the big list because it has tiny entries, and a "hiding inside" check would block almost everything.

Then a loop looks at each character and sets flags for number, capital, lowercase, and symbol. The flags become a score, and the score becomes a strength level.

The password is typed with Python's `getpass`, so it's hidden. When the tests run, nobody is at the keyboard, so the program checks `sys.stdin.isatty()` and uses normal `input()` instead.

## Version history

| Version | What I added | What I learned |
|---------|--------------|----------------|
| V1 | Length check (must be 8+ characters) | `input()`, `print()`, `len()`, `if/else` |
| V2 | Number check using a `for` loop | Looping through characters, `isdigit()` |
| V3 | Capital letter check | `isupper()`, flags (`True`/`False` variables) |
| V4 | Bad word list plus a joke message for `EddieH4ll` | Lists, `in`, `.lower()`, why the order of `if/elif` matters |
| V5 | Lookalike swap detection (`0`→`o`, `1`→`i`, `3`→`e`, `@`→`a`, `4`→`a`, `$`→`s`) | `str.maketrans()`, `.translate()`, debugging a variable that was built but never used |
| V6 | Bad words load from a text file | `open()`, `with`, `.read()`, `.split()` |
| V7 | 10,000 common passwords with an exact-match check | `in` on a list, why exact match beats "hiding inside" for big lists, piping text into a program |
| V8 | Strips numbers from the end, so `Sunshine1` is caught | `.rstrip()`, finding and removing a duplicate check |
| V9 | Lowercase and symbol checks | `islower()`, `not` with `isalnum()`, `==` vs `=` |
| V10 | Point score and strength levels | Counters (`score = score + 1`), where a line sits decides whether it runs |
| V11 | Hidden password entry | `import`, `getpass`, `sys.stdin.isatty()` |

I also wrote `test_checker.py`, an automatic tester that runs all 18 cases.

Older versions are kept in this repo as history.

## Credits

`10k-most-common.txt` comes from [SecLists](https://github.com/danielmiessler/SecLists) by Daniel Miessler and contributors, used under its MIT license.

## Known limitations

This is a learning project, not a real security tool.

- The lists only know common passwords, not every weak one. A password that isn't on them can still say "best".
- It only knows a few lookalike swaps (`7`→`t` isn't included, for example).
- It only strips numbers from the **end** of a password, not the front.
- It doesn't measure randomness (entropy), so a long passphrase and a short complex password aren't compared fairly.
- Never type a password you actually use into any practice program.

## Next steps

- Add an entropy estimate, to explain why a long passphrase can beat a short complex password
- Move the checks into a function so they can be tested directly
- Try a small project in another area of security, like a log file analyzer

## Skills practiced

Python basics, `for` loops, `if/elif/else`, string methods, lists, reading files, debugging, reading error messages, writing automated tests, and using Git/GitHub.

Built by 4J4VID.
