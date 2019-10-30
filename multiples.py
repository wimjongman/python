""" Lab4 ex 1 """
def multiples(p_input):
    """ Prints multiples of input """
    for outer in range(1, p_input+1):
        print(outer, end=" ")
        for inner in range(1, outer):
            print(outer*(inner+1), end=" ")
        print("")

INPUT = input('Typ een nummer ')
multiples(int(INPUT))
