import random
from sympy import *

class Generate_point:
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    z = random.randint(-10, 10)

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

    nested_function = ["ln(", "sin(", "cos(", "tan(", "cot(", "asin(", "acos(", "atan(", "acot(", "e**("]

    count_elements = random.randint(1, count_vars)


    for i in range(count_elements):
        if i != 0:
            result_polynom += random.choice([" + ", " - ", " * "])

        function_in_nested_function = ""
        count_elements_in_nested_function = random.randint(1, 3)

        for j in range(count_elements_in_nested_function):
            flag_nested_function = random.randint(0, 1)
            if j != 0:
                function_in_nested_function += random.choice([" + ", " - ", " * "])

            coefficient = random.randint(1, 10)
            degree_of_element = random.randint(1, degree)
            var = random.choice(vars)

            if var == '':
                function_in_nested_function += f'{coefficient}'
            else:
                if flag_nested_function:
                    function_in_nested_function += random.choice(nested_function)
                if coefficient != 1:
                    function_in_nested_function += f'{coefficient} * '
                function_in_nested_function += var
                if degree_of_element != 1:
                    function_in_nested_function += f'**{degree_of_element}'
                if flag_nested_function:
                    function_in_nested_function += ')'

        simplify(function_in_nested_function)
        result_polynom += random.choice(nested_function) + function_in_nested_function + ')'


    flag_bad_polinom = 0

    for var in vars:
        if result_polynom.find(var) == -1:
            flag_bad_polinom = 1
            break

    if flag_bad_polinom:
        result_polynom = get_function_with_nested_functions_for_differential()

    return result_polynom

def get_function_for_differential():
    return generate_function()

def get_function_with_fraction_for_differential():
    return generate_function_with_fraction()

def get_function_with_nested_functions_for_differential():
    return generate_function_with_nested_functions()

def get_solution_function_for_differential(function):
    solution = ""
    flag_sign_x = false
    flag_sign_y = false
    derivative_of_x = get_solution_partial_derivative_of_x(function)
    derivative_of_y = get_solution_partial_derivative_of_y(function)
    derivative_of_z = get_solution_partial_derivative_of_z(function)
    if (derivative_of_x != ""):
        solution += derivative_of_x
        flag_sign_x = true
    if (derivative_of_y != ""):
        if (flag_sign_x == true):
            solution += " + "
        solution += derivative_of_y
        flag_sign_y = true
    if (derivative_of_z != ""):
        if (flag_sign_x == true or flag_sign_y == true):
            solution += " + "
        solution += derivative_of_z
    return solution

def get_solution_function_with_fraction_for_differential(function_with_fraction):
    v = function_with_fraction.split('/')[0]
    u = function_with_fraction.split('/')[1][1:]

    solution = f'({get_solution_function_for_differential(v)} * {u} - {v} * {get_solution_function_for_differential(v)}) / {u}**2'
    return solution

def get_solution_function_with_nested_functions_for_differential(function_with_nested_functions):
    return get_solution_function_for_differential(function_with_nested_functions)

def get_solution_function_in_point(point, function):
    return function.subs([(symbols('x'), point.x), (symbols('y'), point.y), (symbols('z'), point.z)])

def get_solution_partial_derivative_of_x(function):
    partial_derivative = str(simplify(diff(function, symbols('x'))))
    if (partial_derivative.isdigit()):
        if (partial_derivative == "0"):
            return ""
        return partial_derivative + "dx"
    return '(' + partial_derivative + ')' + "dx"

def get_solution_partial_derivative_of_y(function):
    partial_derivative = str(simplify(diff(function, symbols('y'))))
    if (partial_derivative.isdigit()):
        if (partial_derivative == "0"):
            return ""
        return partial_derivative + "dy"
    return '(' + partial_derivative + ')' + "dy"

def get_solution_partial_derivative_of_z(function):
    partial_derivative = str(simplify(diff(function, symbols('z'))))
    if (partial_derivative.isdigit()):
        if (partial_derivative == "0"):
            return ""
        return partial_derivative + "dz"
    return '(' + partial_derivative + ')' + "dz"

function = get_function_with_nested_functions_for_differential()
solution = get_solution_function_with_nested_functions_for_differential(function)
solution_derivative_of_x = get_solution_partial_derivative_of_x(function)
solution_derivative_of_y = get_solution_partial_derivative_of_y(function)
solution_derivative_of_z = get_solution_partial_derivative_of_z(function)
print(f'Func for differential: {function}')
print(f'Solution: {solution}')
print(f'Solution_x: {solution_derivative_of_x}')
print(f'Solution_y: {solution_derivative_of_y}')
print(f'Solution_z: {solution_derivative_of_z}')

# function = get_function_for_differential()
# solution_function = get_solution_function_for_differential(function)
# print(f'Func for differential: {function}')
# print(f'Solution: {solution_function}')
#
# print("--------------------------------------------------------------------------------------------")
#
# function_with_fraction = get_function_with_fraction_for_differential()
# solution_function_with_fraction = get_solution_function_with_fraction_for_differential(function_with_fraction)
# print(f'Func for differential with fraction: {function_with_fraction}')
# print(f'Solution: {solution_function_with_fraction}')
#
# print("--------------------------------------------------------------------------------------------")
#
# function_with_nested_functions = get_function_with_nested_functions_for_differential()
# solution_function_with_nested_functions = get_solution_function_with_nested_functions_for_differential(function_with_nested_functions)
# print(f'Func for differential with nested functions: {function_with_nested_functions}')
# print(f'Solution: {solution_function_with_nested_functions}')
#
# print("--------------------------------------------------------------------------------------------")
#
# point = Generate_point
# solution_function_in_point = get_solution_function_in_point(point, solution_function)
# print(f'differential {solution_function} in point ({point.x};{point.y};{point.z}) = {solution_function_in_point}')