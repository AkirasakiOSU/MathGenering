import random
from sympy import *

def generate_polinom(degree, count_vars): #(x**2 + 3 * y**3) / (z * y - 120.5)
    result_polynom = ""
    vars = get_vars(count_vars)
    count_elements = random.randint(count_vars, count_vars + 5)

    for i in range(count_elements):
        if i != 0:
            result_polynom += random.choice([" + ", " - ", " * "])

        coefficient = random.randint(1, 10)
        degree_of_element = random.randint(1, degree)
        var = random.choice(vars)

        if var == '':
            result_polynom += f'{coefficient}'
        else:
            if coefficient != 1:
                result_polynom += f'{coefficient} * '
            result_polynom += var
            if degree_of_element != 1:
                result_polynom += f'**{degree_of_element}'

    return result_polynom

def get_fraction(degree, count_vars):
    return f'({generate_polinom(degree, count_vars)}) / ({generate_polinom(degree, count_vars)})'

def get_vars(count_vars):
    match count_vars:
        case 1:
            vars = ['x', '']
        case 2:
            vars = ['x', 'y', '']
        case 3:
            vars = ['x', 'y', 'z', '']
        case _:
            vars = ['x', 'y', 'z', '']

    return vars

def get_polinom(degree, count_vars):
    if degree < 1:
        degree = 1
    if count_vars < 1:
        count_vars = 1

    flag_fraction = random.randint(0, 1)

    if flag_fraction:
        result = get_fraction(degree, count_vars)
    else:
        result = generate_polinom(degree, count_vars)

    flag_bad_polinom = 0
    for var in  get_vars(count_vars):
        if result.find(var) == -1:
            flag_bad_polinom = 1
            break
    if flag_bad_polinom:
        result = get_polinom(degree, count_vars)

    return result

polinom = get_polinom(2, 2)
print(polinom)
print(diff(polinom, symbols('x')) + diff(polinom, symbols('y')) + diff(polinom, symbols('z')))
print(diff(polinom, symbols('x y')))

#x, y = symbols('x y')
#print(diff(polinom, x, y))

# нужен костыль для дробей