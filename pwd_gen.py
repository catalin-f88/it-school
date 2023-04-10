import string
import random
import argparse

parser = argparse.ArgumentParser(description='Generate a random password.')
parser.add_argument("-l", "--length", type=int)
parser.add_argument("-d", "--digits", action="store_true")
parser.add_argument("-s", "--symbols", action="store_true")
args = parser.parse_args()
# print(args)


def generate_numbers(length):
    current = 0
    num_gen = []
    while current < length:
        num_gen.append(random.randint(0, 9))
        current += 1
    return num_gen

def generate_letters(length):
    alphabet = string.ascii_letters
    current = 0
    let_gen = []
    while current < length:
        let_gen.append(alphabet[random.randint(0, len(alphabet))])
        current += 1
    dupl_let = list(dict.fromkeys(let_gen))
    while len(dupl_let) < length:
        dupl_let.append(alphabet[random.randint(0, len(alphabet))])
        dupl_let = list(dict.fromkeys(dupl_let))
    return dupl_let

def generate_symbols(length):
    current = 0
    sym_gen = []
    while current < length:
        sym_gen.append(chr(random.randint(33, 47)))
        current += 1
    dupl_sym = list(dict.fromkeys(sym_gen))
    while len(dupl_sym) < length:
        dupl_sym.append(chr(random.randint(33, 47)))
        dupl_sym = list(dict.fromkeys(dupl_sym))
    return dupl_sym

def generate_password(length, num_digits, num_symbols):
    num_digits = 0
    num_symbols = 0
    if args.digits:
        num_digits = random.randint(1, length - 3)
    if args.symbols:
        num_symbols = random.randint(1, length - num_digits - 2)
    num_letters = length - num_digits - num_symbols
    numbers_gen = generate_numbers(num_digits)
    symbols_gen = generate_symbols(num_symbols)
    letters_gen = generate_letters(num_letters)
    result = [*numbers_gen, *symbols_gen, *letters_gen]
    random.shuffle(result)
    # print(result)
    
    for i in range(len(result)):
        if result[i] == result[i-1]:
            random.shuffle(result)
    password = "".join(str(x) for x in result)
    return password

print(f"Your randomly generated password is: {generate_password(args.length, args.digits, args.symbols)}")
