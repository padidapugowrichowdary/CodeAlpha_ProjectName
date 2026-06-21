import re

with open("email.txt", "r") as file:
    data = file.read()

emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)

with open("output.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")