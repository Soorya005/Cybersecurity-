import string
import random
def password_generator(length):
    characters= string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(length))
    return password
desired_length = int(input("Enter the desired length of the password: "))
password = password_generator(desired_length)
print("Generated Password:", password)


