import random
import string

use_uppper_case = input('do you want to use upper case....(y/n)') == 'y'
use_lower_case = input('do you want to use lower case....(y/n)') == 'y'
use_digits = input('do you want to use digits....(y/n)') == 'y'
use_special_chars = input('do you want to use special chars....(y/n)') == 'y'

upper_case = string.ascii_uppercase if use_uppper_case else ''
lower_case = string.ascii_lowercase if use_lower_case else ''
digits = string.digits if use_digits else ''
special_chars = string.punctuation if use_special_chars else ''

all_chars = upper_case+lower_case+digits+special_chars

pass_len = int(input('enter the length of the password....'))

generate_password = random.choices(all_chars,k=pass_len)
show_password = ''.join(generate_password)
print(show_password)
