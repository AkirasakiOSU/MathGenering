import random
from sympy import *

def generate_function():
    degree = random.randint(1, 5)
    count_vars = random.randint(1, 3)
    result_polynom = ""

    match count_vars:
        case 1:
            vars = ['x', '']
        case 2:
            vars = ['x', 'y', '']
        case 3:
            vars = ['x', 'y', 'z', '']
        case _:
            vars = ['x', 'y', 'z', '']

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

    flag_bad_polinom = 0

    for var in vars:
        if result_polynom.find(var) == -1:
            flag_bad_polinom = 1
            break

    if flag_bad_polinom:
        result_polynom = get_function_for_differential()

    return simplify(result_polynom)

def generate_function_with_fraction():
    return f'({generate_function()}) / ({generate_function()})'

def generate_function_with_nested_functions():
    pass

def get_function_for_differential():
    return generate_function()

def get_function_with_fraction_for_differential():
    return generate_function_with_fraction()

def get_function_with_nested_functions_for_differential():
    pass

def get_solution_function_for_differential(funcion):
    return simplify(diff(funcion, symbols('x')) + diff(funcion, symbols('y')) + diff(funcion, symbols('z')))

def get_solution_function_with_fraction_for_differential(function_with_fraction):
    v = function_with_fraction.split('/')[0]
    u = function_with_fraction.split('/')[1][1:]

    solution = f'({get_solution_function_for_differential(v)} * {u} - {v} * {get_solution_function_for_differential(v)}) / {u}**2'
    return simplify(solution)

def get_solution_function_with_nested_functions_for_differential(function_with_nested_functions):
    pass



function = get_function_for_differential()
function_with_fraction = get_function_with_fraction_for_differential()
solution_function = get_solution_function_for_differential(function)
solution_function_with_fraction = get_solution_function_with_fraction_for_differential(function_with_fraction)

print(f'Func for differential: {function}')
print(f'Solution: {solution_function}')
print(f'Func for differential with fraction: {function_with_fraction}')
print(f'Solution: {solution_function_with_fraction}')