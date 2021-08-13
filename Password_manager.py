import random
import string
def random_password(min_characters, max_characters, allowed_characters):
    password = ""
    for char in range(min_characters, max_characters):    
        password += random.choice(allowed_characters)
    return password
