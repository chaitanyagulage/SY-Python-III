import re

def find_emails(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
    return re.findall(pattern, text)

text = input()
emails = find_emails(text)

print(emails) 