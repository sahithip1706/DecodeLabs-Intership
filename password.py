import secrets
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password_list = []

for i in range(length):
    char = secrets.choice(all_characters)
    password_list.append(char)

password = ''.join(password_list)

print("\nGenerated Password:")
print(password)