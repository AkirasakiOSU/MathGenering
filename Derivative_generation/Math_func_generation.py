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

    flag_bad_polynom = 0

    for var in vars:
        if result_polynom.find(var) == -1:
            flag_bad_polynom = 1
            break

    if flag_bad_polynom:
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


    flag_bad_polynom = 0

    for var in vars:
        if result_polynom.find(var) == -1:
            flag_bad_polynom = 1
            break

    if flag_bad_polynom:
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
    if (derivative_of_x != 0):
        solution += derivative_of_x
        flag_sign_x = true
    if (derivative_of_y != 0):
        if (flag_sign_x == true):
            solution += " + "
        solution += derivative_of_y
        flag_sign_y = true
    if (derivative_of_z != 0):
        if (flag_sign_x == true or flag_sign_y == true):
            solution += " + "
        solution += derivative_of_z
    return solution

def get_solution_function_with_fraction_for_differential(function_with_fraction):
    u = function_with_fraction.split('/')[0][:-1]
    v = function_with_fraction.split('/')[1][1:]

    solution = (f'(({get_solution_function_for_differential(u)}) * {v} - '
                f'{u} * ({get_solution_function_for_differential(v)})) / {v}**2')
    return solution

def get_solution_function_with_nested_functions_for_differential(function_with_nested_functions):
    return get_solution_function_for_differential(function_with_nested_functions)

def get_solution_partial_derivative_of_x(function):
    if ('/' in str(function)):
        u = function.split('/')[0]
        v = function.split('/')[1][1:]
        u_solution_partial_derivative_of_x = get_solution_partial_derivative_of_x(u)
        v_solution_partial_derivative_of_x = get_solution_partial_derivative_of_x(v)
        partial_derivative = ""

        if (u_solution_partial_derivative_of_x == 0 and v_solution_partial_derivative_of_x == 0):
            partial_derivative += "0"
        elif (u_solution_partial_derivative_of_x == 0 and v_solution_partial_derivative_of_x != 0):
            partial_derivative = (f'(-{u} * {v_solution_partial_derivative_of_x}) / {v}**2')
        elif (u_solution_partial_derivative_of_x != 0 and v_solution_partial_derivative_of_x == 0):
            partial_derivative = (f'({u_solution_partial_derivative_of_x} * {v}) / {v}**2')
        else:
            partial_derivative = (f'({u_solution_partial_derivative_of_x} * {v} - '
                                  f'{u} * {v_solution_partial_derivative_of_x}) / {v}**2')
        return partial_derivative
    else:
        partial_derivative = str(simplify(diff(function, symbols('x'))))
        if (partial_derivative.isdigit() or partial_derivative[1:].isdigit()):
            if (partial_derivative == "0"):
                return 0
            return partial_derivative + "dx"
        return '(' + partial_derivative + ')' + "dx"

def get_solution_partial_derivative_of_y(function):
    if ('/' in str(function)):
        u = function.split('/')[0]
        v = function.split('/')[1][1:]
        u_solution_partial_derivative_of_y = get_solution_partial_derivative_of_y(u)
        v_solution_partial_derivative_of_y = get_solution_partial_derivative_of_y(v)
        partial_derivative = ""

        if (u_solution_partial_derivative_of_y == 0 and v_solution_partial_derivative_of_y == 0):
            partial_derivative += "0"
        elif (u_solution_partial_derivative_of_y == 0 and v_solution_partial_derivative_of_y != 0):
            partial_derivative = (f'(-{u} * {v_solution_partial_derivative_of_y}) / {v}**2')
        elif (u_solution_partial_derivative_of_y != 0 and v_solution_partial_derivative_of_y == 0):
            partial_derivative = (f'({u_solution_partial_derivative_of_y} * {v}) / {v}**2')
        else:
            partial_derivative = (f'({u_solution_partial_derivative_of_y} * {v} - '
                                  f'{u} * {v_solution_partial_derivative_of_y}) / {v}**2')
        return partial_derivative
    else:
        partial_derivative = str(simplify(diff(function, symbols('y'))))
        if (partial_derivative.isdigit()):
            if (partial_derivative == "0" or partial_derivative[1:].isdigit()):
                return 0
            return partial_derivative + "dy"
        return '(' + partial_derivative + ')' + "dy"

def get_solution_partial_derivative_of_z(function):
    if ('/' in str(function)):
        u = function.split('/')[0]
        v = function.split('/')[1][1:]
        u_solution_partial_derivative_of_z = get_solution_partial_derivative_of_z(u)
        v_solution_partial_derivative_of_z = get_solution_partial_derivative_of_z(v)
        partial_derivative = ""

        if (u_solution_partial_derivative_of_z == 0 and v_solution_partial_derivative_of_z == 0):
            partial_derivative += "0"
        elif (u_solution_partial_derivative_of_z == 0 and v_solution_partial_derivative_of_z != 0):
            partial_derivative = (f'(-{u} * {v_solution_partial_derivative_of_z}) / {v}**2')
        elif (u_solution_partial_derivative_of_z != 0 and v_solution_partial_derivative_of_z == 0):
            partial_derivative = (f'({u_solution_partial_derivative_of_z} * {v}) / {v}**2')
        else:
            partial_derivative = (f'({u_solution_partial_derivative_of_z} * {v} - '
                                  f'{u} * {v_solution_partial_derivative_of_z}) / {v}**2')
        return partial_derivative
    else:
        partial_derivative = str(simplify(diff(function, symbols('z'))))
        if (partial_derivative.isdigit() or partial_derivative[1:].isdigit()):
            if (partial_derivative == "0"):
                return 0
            return partial_derivative + "dz"
        return '(' + partial_derivative + ')' + "dz"

def get_solution_function_in_point(point, function):
    return function.subs([(symbols('x'), point.x), (symbols('y'), point.y), (symbols('z'), point.z)])


# class Generate_point
# when creating an object of the class, the coordinates of the point are generated
# usage examples:
# point = Generate_point
# print(f'point ({point.x}; {point.y}; {point.z})

# generate_function()
# this function generates polynom of varying difficulties
# example: -5*x - 6*y + z**2
# usage examples:
# not used by the user, because the function is called from another function

# generate_function_with_fraction()
# this function generates function with fraction of varying difficulties
# example: (x**2 + 7*x - 27) / (11*x + 18*y - 8*z + 6)
# usage examples:
# not used by the user, because the function is called from another function

# generate_function_with_nested_functions()
# this function generates function with nested functions of varying difficulties
# example: e**(cot(4 * x**3) * 2 * x)
# usage examples:
# not used by the user, because the function is called from another function

# get_function_for_differential()
# this function return the generated polynom from method generate_function()
# usage examples:
# function = get_function_for_differential()
# print(f'Func for differential: {function}')

# get_function_with_fraction_for_differential()
# this function return the generated function with fraction from method generate_function_with_fraction()
# usage examples:
# function = get_function_with_fraction_for_differential()
# print(f'Func for differential: {function}')

# get_function_with_nested_functions_for_differential()
# this function return the generated function with nested functions from method generate_function_with_nested_functions()
# usage examples:
# function = get_function_with_nested_functions_for_differential()
# print(f'Func for differential: {function}')

# get_solution_function_for_differential(function)
# this method takes a polynom as input, from which you need to find the differential, returns the differential
# example: (x*(-45*x*y**2 - 34))dx + (-30*x**3*y - 7)dy
# usage examples:
# function = get_function_for_differential()
# solution_function = get_solution_function_for_differential(function)

# get_solution_function_with_fraction_for_differential(function_with_fraction)
# this method takes a function with fraction as input, from which you need to find the differential, returns the differential
# example: (((56*y)dx + (56*x)dy) * (2 - 8*x) - (56*x*y) * (-8dx)) / (56*x*y)**2
# usage examples:
# function_with_fraction = get_function_with_fraction_for_differential()
# solution_function_with_fraction = get_solution_function_with_fraction_for_differential(function_with_fraction)

# get_solution_function_with_nested_functions_for_differential(function_with_nested_functions)
# this method takes a function with nested functions as input, from which you need to find the differential, returns the differential
# example: (-9*sin(9*x))dx
# usage examples:
# function_with_nested_functions = get_function_with_nested_functions_for_differential()
# solution_function_with_nested_functions = get_solution_function_with_nested_functions_for_differential(function_with_nested_functions)

# get_solution_partial_derivative_of_x(function)
# this method takes any function as input, from which you need to find the partial derivative of x, returns partial derivative of x
# example: ((32*x**3 + 12*y)dx * (27*x) - (8*x**4 + 12*x*y - 2)  * 27dx) / (27*x)**2
# usage examples:
# function = get_function_with_fraction_for_differential()
# solution_function = get_solution_partial_derivative_of_x(function)

# get_solution_partial_derivative_of_y(function)
# this method takes any function as input, from which you need to find the partial derivative of y, returns partial derivative of y
# example: (24*y**3)dy
# usage examples:
# function = get_function_for_differential()
# solution_function = get_solution_partial_derivative_of_y(function)

# get_solution_partial_derivative_of_z(function)
# this method takes any function as input, from which you need to find the partial derivative of z, returns partial derivative of z
# example: (2*cot(6*x**2 + 3*y**2)/((4*z**2 + 1)*atan(2*z)))dz
# usage examples:
# function = get_function_with_nested_functions_for_differential()
# solution_function = get_solution_partial_derivative_of_z(function)