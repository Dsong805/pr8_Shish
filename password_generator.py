import random
import string

def generate_password(length=11):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == __main__:
    print(Generated password:, generate_password()) 
