"""
test_checker.py - automatic tester for the Password Checker project.

Runs the checker once per test password and prints PASS or FAIL for each.
See the README ("Run the tests") for how to use it.
"""

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# What the checker prints for each rule.
BAD = "try something stronger"
JOKE = "Dont actually use EddieH4ll SMH"
SHORT = "too short add characters"
NO_CAP = "add a capital letter to continue"
NO_NUM = "add numbers to continue"
NO_SYM = "add a symbol to continue"
NO_LOW = "add a lowercase letter to continue"
GOOD = "perfect"

# (password, which rule is being tested, expected message, expected strength)
TESTS = [
    ("Zebra7Lamp#", "all rules pass",                   GOOD,   "best"),
    ("Zebra7Lamp",  "no symbol",                        NO_SYM, "decent"),
    ("zebra7lamp#", "no capital letter",                NO_CAP, "decent"),
    ("ZEBRA7LAMP#", "no lowercase letter",              NO_LOW, "decent"),
    ("Zebralamps#", "no number",                        NO_NUM, "decent"),
    ("zebra7lamps", "no capital, no symbol",            NO_CAP, "risky"),
    ("zebralamps",  "only lowercase letters",           NO_CAP, "weak"),
    ("Zb7",         "too short",                        SHORT,  "weak"),
    ("Mypassword9", "bad word inside the password",     BAD,    "weak"),
    ("Qwerty123X",  "another bad word",                 BAD,    "weak"),
    ("Zebra1234",   "bad word '1234' (needs lowered)",  BAD,    "weak"),
    ("M0nkeyboy",   "lookalike swap 0 -> o",            BAD,    "weak"),
    ("P@ssw0rd99",  "lookalike swaps @ and 0",          BAD,    "weak"),
    ("L3tm31n7X",   "lookalike swaps 3 -> e, 1 -> i",   BAD,    "weak"),
    ("Sunshine",    "exact match on the big list",      BAD,    "weak"),
    ("Sunshine1",   "big list + number on the end",     BAD,    "weak"),
    ("Sunshine99",  "big list + two numbers on the end", BAD,   "weak"),
    ("EddieH4ll#",  "joke message",                     JOKE,   "best"),
]


def find_checker():
    """Pick the checker file: a name given on the command line, or the newest default."""
    if len(sys.argv) > 1:
        return HERE / sys.argv[1]
    for name in ("password_checker_V10.py", "password_checkerV10.py"):
        if (HERE / name).exists():
            return HERE / name
    return HERE / "password_checker_V10.py"


def run_checker(script, password):
    """Run the checker with `password` typed in. Returns (output, error_text)."""
    result = subprocess.run(
        [sys.executable, str(script)],
        input=password + "\n",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(HERE),          # so open("common_passwords.txt") finds the files
        timeout=20,
    )
    return result.stdout, result.stderr


def get_strength(output):
    match = re.search(r"strength:\s*(\w+)", output)
    return match.group(1) if match else None


def main():
    script = find_checker()
    if not script.exists():
        print("Can't find the checker file:", script.name)
        print("Put test_checker.py in the same folder as your checker, or run:")
        print("    python test_checker.py your_file_name.py")
        return 1

    print("Testing:", script.name)
    print("-" * 78)
    print("%-6s %-13s %-36s %s" % ("RESULT", "PASSWORD", "WHAT IT TESTS", "NOTES"))
    print("-" * 78)

    passed = 0
    failed = 0
    for password, what, want_msg, want_strength in TESTS:
        try:
            output, err = run_checker(script, password)
        except subprocess.TimeoutExpired:
            output, err = "", "timed out"

        if err.strip():
            # Python crashed (missing word list, syntax error, ...). Show the last line.
            problem = err.strip().splitlines()[-1]
            print("%-6s %-13s %-36s %s" % ("FAIL", password, what, problem))
            failed += 1
            continue

        notes = []
        if want_msg not in output:
            notes.append("expected '%s'" % want_msg)

        got_strength = get_strength(output)
        if got_strength is None and "strength:" not in output:
            # Older version with no strength label: skip that check.
            pass
        elif got_strength != want_strength:
            notes.append("expected strength '%s', got '%s'" % (want_strength, got_strength))

        if notes:
            print("%-6s %-13s %-36s %s" % ("FAIL", password, what, "; ".join(notes)))
            failed += 1
        else:
            print("%-6s %-13s %-36s" % ("PASS", password, what))
            passed += 1

    print("-" * 78)
    print("%d passed, %d failed, %d total" % (passed, failed, passed + failed))
    if failed == 0:
        print("All tests passed.")
    else:
        print("Some tests failed. Read the NOTES column, then check that rule in your code.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
