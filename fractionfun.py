from fractions import Fraction
import functools
import operator

def mixed_number_to_fraction(raw):
    return functools.reduce(Fraction.__add__, map(Fraction, raw.split('_')))

def fraction_to_mixed_number_string(fraction):
    whole = int(fraction.numerator / fraction.denominator)
    remainder = fraction - whole

    if (whole != 0) and (remainder != 0):
        return_string = "{}_{}".format(whole, remainder)
    elif (remainder != 0):
        return_string = "{}".format(remainder)
    else:
        return_string = "{}".format(whole)

    return return_string

operator_map = {
    '+':    operator.add,
    '-':    operator.sub,
    '*':    operator.mul,
    '/':    operator.truediv
    }

def process_input(input):
    # Split on whitespace into strings
    (operand1, operator, operand2) = input.split()

    # Convert operands to Fraction objects
    (operand1, operand2) = map(mixed_number_to_fraction, (operand1, operand2))

    # Perform calculation
    result = operator_map[operator](operand1, operand2)

    # Return result
    return fraction_to_mixed_number_string(result)

if __name__ == '__main__':
    # Process command line

    # In order to parse input on Python2, if you use "input" it will do
    # unspeakable things to your input, so you need to use "raw_input"
    # and this is fixed in Python3 where they just use "input". So enjoy
    # the following from
    # https://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3
    try: input = raw_input
    except NameError: pass

    print("= {}".format(process_input(input('? '))))
