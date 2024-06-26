# Creating functions for different operations
def calc_sum(a, b):
    sums = a + b
    return sums

def calc_diff(a, b):
    diff = a - b
    return diff

def calc_div(a, b):
    div = a / b
    return div

def calc_product(a, b):
    product = a * b
    return product

def calc_expont(a, b):
    expo = a ** b
    return expo

# Take input from the user for numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Take input from the user for operation
opr = input('''List:
              1. + for addition
              2. - for subtraction
              3. / for division
              4. * for multiplication
              5. ** for exponentiation
              Enter the operation symbol: ''')

# Defining conditions
if opr == '+':
    result = calc_sum(a, b)

elif opr == '-':
    result = calc_diff(a, b)

elif opr == '/':
    result = calc_div(a, b)

elif opr == '*':
    result = calc_product(a, b)

elif opr == '**':
    result = calc_expont(a, b)

else:
    print("Invalid Operation......")
    result = None


#will print the result if it is not None
if result is not None:
    print("Result:", result)
