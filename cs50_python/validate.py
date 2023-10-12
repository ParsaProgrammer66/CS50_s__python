import re

email = input("what is your email? ").strip()

if re.search(r"^(\w|\s)+@\w+\.(com|edu|org)$",email,re.IGNORECASE):
    print("valid")
else:
    print("invalid")