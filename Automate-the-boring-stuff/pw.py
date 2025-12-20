#! python3

# pw.py - An insecure password locker program.

PASSWORDS = {
    "email": "This is email password",
    "blog": "And this is blog password",
    "database": "And this is secure password for DB",
}

import sys

import pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account named {account}.")
