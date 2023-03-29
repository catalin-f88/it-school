import string
import random

alphabet = string.ascii_letters

pass_length = 8
pass_digits = True
pass_symbols = True

def generate_password(length, digits, symbols):
    length = 0
    password = []
    numbers = set()
    symbol = set()
    chars = set()

    if digits:
        num_digits = random.randint(1, pass_length - 3)
    else:
        num_digits = 0
    if symbols:
        sym_digits = random.randint(1, (pass_length - num_digits))
    else:
        sym_digits = 0
    while length < pass_length:
        while len(numbers) < num_digits:
            numbers.add(random.randint(0, 9))
            length += 1
        while len(symbol) < (sym_digits + num_digits) and length < pass_length:
            symbol.add(chr(random.randint(33, 47)))
            length += 1
        try:
            while len(chars) < (pass_length - sym_digits - num_digits):
                password.append(alphabet[random.randint(0, len(alphabet))])
        except IndexError:
            break
        length += 1
    random.shuffle(password)
    print(password)
    result = "".join(str(x) for x in password)
    result1 = "".join(str(x) for x in numbers)
    result2 = "".join(str(x) for x in symbol)
    # duplicate = [ch for i, ch in enumerate(result) if ch not in result[:i]]
    # if len(duplicate) < length:
    #     duplicate.append(alphabet[random.randint(0, len(alphabet))])
        # random.shuffle(duplicate)
    # result_no_duplicate = "".join(str(x) for x in duplicate)
    # final_password = list(result_no_duplicate + result1 + result2)
    # shuffled_pwd = random.shuffle(final_password)
    # print(shuffled_pwd)

generate_password(pass_length, pass_digits, pass_symbols)

