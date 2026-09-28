"""
Password policy strength checker (defensive/educational tool — not a cracker).
Usage: python password_checker.py
"""
import re
import getpass

def check_password(pw):
    issues = []
    if len(pw) < 12:
        issues.append("Too short (use 12+ characters)")
    if not re.search(r"[a-z]", pw):
        issues.append("Add lowercase letters")
    if not re.search(r"[A-Z]", pw):
        issues.append("Add uppercase letters")
    if not re.search(r"\d", pw):
        issues.append("Add digits")
    if not re.search(r"[^\w\s]", pw):
        issues.append("Add special characters")

    common = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}
    if pw.lower() in common:
        issues.append("This is a commonly used/leaked password")

    return issues

def main():
    pw = getpass.getpass("Enter a password to check (not stored/logged): ")
    issues = check_password(pw)
    if not issues:
        print("Looks strong by basic checks.")
    else:
        print("Issues found:")
        for i in issues:
            print(f" - {i}")

if __name__ == "__main__":
    main()
