""" Lab4 ex 2 """
import math
import sys
def is_prime(p_input):
    """ Checks if input is a prime """
    if p_input == 2:
        return True
    if p_input % 2 == 0:
        return False
    for divis in range(3, p_input, 2):
        if p_input % divis == 0:
            return False
    return True

def process_number(p_input):
    """ Factorizes input """
    dict = {}
    input = int(p_input)
    key = factorize(input)
    while key != 1:
        if key not in dict:
            dict[key] = 0

        counter = dict[key]
        counter = counter + 1
        dict[key] = counter
        input = input / key
        key = factorize(input)
    return dict

def print_result(p_input):
    """ Prints result """
    result = ''
    for key in p_input:
        result += (str(key) + '^' + str(p_input[key]) + ' x ')
    print(result.rstrip(' x'))


def factorize(p_input):
    """ Finds lowest prime factor """
    input = int(p_input)
    if is_prime(input):
        return input
    for factor in range(2, math.floor(input / 2)):
        if (input % factor == 0) & is_prime(factor):
            return factor
    return 1


def run():
    """ Runs the program """
    vary = 0
    vary = int(input('Typ een nummer, 0 is einde: '))
    while vary != 0:
        mydict = process_number(vary)
        print_result(mydict)
        return True
    return False

COUNTER = 0
while run():
    COUNTER = COUNTER + 1
print('Tot ziens!')
sys.exit()
