from fractions import Fraction

def mixed_number_to_fraction(raw):
    args = raw.split('_')
    if len(args) > 1:
        whole = args[0]
        fractional = args[1]
    else:
        whole = 0
        fractional = args[0]
    
    return Fraction(fractional) + Fraction(whole)

def process_input(input):
    # Split on whitespace
    args = input.split()

    # First argument is operand1
    operand1 = mixed_number_to_fraction(args[0])

    # Second is operator
    operator = args[1]

    # Third is operand2
    operand2 = mixed_number_to_fraction(args[2])

    # Perform calculation

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '/':
        result = operand1 / operand2
    elif operator == '*':
        result = operand1 * operand2

    # Return result
    return str(result)
