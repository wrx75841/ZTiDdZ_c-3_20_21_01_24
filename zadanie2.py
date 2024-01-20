import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(characters) for i in range(8))

        if any(c.islower() for c in password) and \
           any(c.isupper() for c in password) and \
           any(c.isdigit() for c in password) and \
           any(c in string.punctuation for c in password) and \
           not any(word in password.lower() for word in ["słowo1", "słowo2"]): # wyborażmy sobie ze tu jest słownik z encykolpedii
            return password

password_result = generate_password()
print(password_result)
