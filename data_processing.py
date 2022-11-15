import re


symbols = r'[^\.\+\-\*\/\(\)0-9ij]'


def str_check(task):
    if re.search(symbols, task):  # если есть не числа, не арифметические символы, не i и не j
        return False
    else:
        if 'i' in task and 'j' in task:  # если сразу и i, и j
            return False
        else:
            return True
