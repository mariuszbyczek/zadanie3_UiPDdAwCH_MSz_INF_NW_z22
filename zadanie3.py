import secrets
import string
import random

pass_len = 12 # długość hasła
list_chars_type = [string.digits, string.punctuation, string.ascii_letters]
pwd = ''
before_last_char_type = 0
last_char_type = 0
for i in range(pass_len):
                                        # aby zapobiec występywaniu wyrazów słownikowych obok siebie
    char_type_random = 0                # zwyczajnie niedopuścimy do występowania trzech liter obok siebie
    if before_last_char_type == 2 and last_char_type == 2: #jeśli poprzednio były dwie litery
        char_type_random = random.randint(0, 1)             # następna będzie liczbą lub znakiem specjalnym
    else:
        char_type_random = random.randint(0, 2)

    pwd += ''.join(secrets.choice(list_chars_type[char_type_random]))
    before_last_char_type = last_char_type
    last_char_type = char_type_random

print(pwd)
