
import random

upper_case_letters = [chr(i) for i in range(65, 91)]
lower_case_letters = [chr(i) for i in range(97, 123)]

letters = upper_case_letters + lower_case_letters
numbers = [chr(i) for i in range(48, 58)]
special_symbols = [
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', 
    ';', '"', '\'', '<', ',' ,'>', '.', '?', '/'
    ]
numbers = [chr(i) for i in range(48, 58)]
chars = [letters, numbers, special_symbols]


'''
This function uses pseudo-random number generator which is not good for security because one can predict it.
To make this password generator, one needs to use the python's secrets module.
'''
def generate_password():
    letters_num = int(input('How many letters would you like in your password?\n'))
    digits_num = int(input('How many digits would you like in your password?\n'))
    special_num = int(input('How many special symbols would you like in your password?\n'))

    char_nums = [letters_num, digits_num, special_num]

    gen_password = []

    while any(char_nums):
        i = random.randint(0, len(chars) - 1)
        
        if not char_nums[i]:
            continue

        gen_password.append(random.choice(chars[i]))
        char_nums[i] -= 1

    random.shuffle(gen_password)
    return ''.join(gen_password)
        

def main():
    print('*****************Welcome to the PyPassword Generator!*****************')
    new_pass = generate_password()
    print(new_pass)

main()