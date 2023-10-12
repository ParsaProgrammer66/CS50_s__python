import re

url = input("URL: ").strip()

if matches := re.search(r"^https://(www\.)?twitter\.com/([a-z0-9_]+)$",url,re.IGNORECASE):
    if matches.group(1)=="com":
        print(f"username: ",matches.group(1))