import random
from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt

class Generate_point:
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    z = random.randint(-10, 10)
class Solution_differential_in_poin:
    def __init__(self, function, solution, point):
        self.function = function
        self.solution = solution
        self.point = point

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
    return get_solution_function_for_differential(function_with_nested_functions).replace("log", "ln")

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
        return '(' + partial_derivative.replace("log", "ln") + ')' + "dx"

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
        return '(' + partial_derivative.replace("log", "ln") + ')' + "dy"

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
        return '(' + partial_derivative.replace("log", "ln") + ')' + "dz"

def get_random_function():
    methods = [get_function_for_differential(), get_function_with_nested_functions_for_differential(), get_function_with_fraction_for_differential()]
    return str(random.choice(methods))

def get_solution_function_with_fraction_in_point_for_differential(function):
    point = Generate_point

    u = function.split('/')[0][:-1]
    v = function.split('/')[1][1:]

    u_solution_partial_derivative_of_x = get_solution_partial_derivative_of_x(u)
    u_solution_partial_derivative_of_y = get_solution_partial_derivative_of_y(u)
    u_solution_partial_derivative_of_z = get_solution_partial_derivative_of_z(u)

    v_solution_partial_derivative_of_x = get_solution_partial_derivative_of_x(v)
    v_solution_partial_derivative_of_y = get_solution_partial_derivative_of_y(v)
    v_solution_partial_derivative_of_z = get_solution_partial_derivative_of_z(v)

    u = str(parse_expr(u).subs([(symbols('x'), point.x), (symbols('y'), point.y), (symbols('z'), point.z)]))
    v = str(parse_expr(v).subs([(symbols('x'), point.x), (symbols('y'), point.y), (symbols('z'), point.z)]))

    if (v == "0"):
        return get_solution_function_with_fraction_in_point_for_differential(get_function_with_fraction_for_differential())

    flag_u_x = false
    flag_u_y = false
    flag_u_z = false

    flag_v_x = false
    flag_v_y = false
    flag_v_z = false

    if (u_solution_partial_derivative_of_x != 0):
        u_solution_partial_derivative_of_x = u_solution_partial_derivative_of_x[:-2]
        u_solution_partial_derivative_of_x = str(parse_expr(u_solution_partial_derivative_of_x).subs([(symbols('x'), point.x),
                                                                                (symbols('y'), point.y),
                                                                                (symbols('z'), point.z)]))
        flag_u_x = true

    if (u_solution_partial_derivative_of_y != 0):
        u_solution_partial_derivative_of_y = u_solution_partial_derivative_of_y[:-2]
        u_solution_partial_derivative_of_y = str(parse_expr(u_solution_partial_derivative_of_y).subs([(symbols('x'), point.x),
                                                                                                      (symbols('y'), point.y),
                                                                                                      (symbols('z'), point.z)]))
        flag_u_y = true

    if (u_solution_partial_derivative_of_z != 0):
        u_solution_partial_derivative_of_z = u_solution_partial_derivative_of_z[:-2]
        u_solution_partial_derivative_of_z = str(parse_expr(u_solution_partial_derivative_of_z).subs([(symbols('x'), point.x),
                                                                                                      (symbols('y'), point.y),
                                                                                                      (symbols('z'), point.z)]))
        flag_u_z = true

    if (v_solution_partial_derivative_of_x != 0):
        v_solution_partial_derivative_of_x = v_solution_partial_derivative_of_x[:-2]
        v_solution_partial_derivative_of_x = str(parse_expr(v_solution_partial_derivative_of_x).subs([(symbols('x'), point.x),
                                                                                                      (symbols('y'), point.y),
                                                                                                      (symbols('z'), point.z)]))
        flag_v_x = true

    if (v_solution_partial_derivative_of_y != 0):
        v_solution_partial_derivative_of_y = v_solution_partial_derivative_of_y[:-2]
        v_solution_partial_derivative_of_y = str(parse_expr(v_solution_partial_derivative_of_y).subs([(symbols('x'), point.x),
                                                                                                      (symbols('y'), point.y),
                                                                                                      (symbols('z'), point.z)]))
        flag_v_y = true

    if (v_solution_partial_derivative_of_z != 0):
        v_solution_partial_derivative_of_z = v_solution_partial_derivative_of_z[:-2]
        v_solution_partial_derivative_of_z = str(parse_expr(v_solution_partial_derivative_of_z).subs([(symbols('x'), point.x),
                                                                                                      (symbols('y'), point.y),
                                                                                                      (symbols('z'), point.z)]))
        flag_v_z = true

    if(flag_u_x == false and flag_u_y == false and flag_u_z == false):
        full_differential_u = 0
    else:
        full_differential_u = 1
    if(flag_v_x == false and flag_v_y == false and flag_v_z == false):
        full_differential_v = 0
    else:
        full_differential_v = 1

    if (full_differential_u == 0 and full_differential_v == 0):
        return 0


    if (full_differential_u != 0 and full_differential_v == 0):
        solution = (f'((({u_solution_partial_derivative_of_x})dx + ({u_solution_partial_derivative_of_y})dy + '
                    f'({u_solution_partial_derivative_of_z})dz) * ({v})) / {str(simplify(v + "**2"))}')

    if (full_differential_u == 0 and full_differential_v != 0):
        solution = (f'(-({u}) * (({v_solution_partial_derivative_of_x})dx + '
                              f'({v_solution_partial_derivative_of_y})dy + '
                              f'({v_solution_partial_derivative_of_z})dz)) / {str(simplify(v + "**2"))}')

    if (full_differential_u != 0 and full_differential_v != 0):
        solution = (f'((({u_solution_partial_derivative_of_x})dx + ({u_solution_partial_derivative_of_y})dy + '
                    f'({u_solution_partial_derivative_of_z})dz) * ({v}) - ({u}) * ('
                    f'({v_solution_partial_derivative_of_x})dx + '
                    f'({v_solution_partial_derivative_of_y})dy + '
                    f'({v_solution_partial_derivative_of_z})dz)) / {str(simplify(v + "**2"))}')

    if ("zoo" in solution or "I" in solution or "nan" in solution):
        return get_solution_function_with_fraction_in_point_for_differential(get_function_with_fraction_for_differential())

    return Solution_differential_in_poin(function, solution, point)

def get_solution_function_in_point_for_differential():
    function = get_random_function()
    solution = get_solution_function_for_differential(function)
    nested_function_with_solution_in_zero = ["sin", "cos", "tan", "asin", "acos", "atan", "acot", "e**"]
    nested_function_no_solution_in_zero = ["ln", "cot"]

    there_are_functions_with_solution_in_zero = any(nested_functions in solution for nested_functions in
                                                    nested_function_with_solution_in_zero)
    there_are_functions_no_solution_in_zero = any(nested_functions in solution for nested_functions in
                                                  nested_function_no_solution_in_zero)

    while (there_are_functions_with_solution_in_zero and there_are_functions_no_solution_in_zero):
        function = get_random_function()
        solution = get_solution_function_for_differential(function)
        there_are_functions_with_solution_in_zero = any(nested_functions in solution for nested_functions in nested_function_with_solution_in_zero)
        there_are_functions_no_solution_in_zero = any(nested_functions in solution for nested_functions in nested_function_no_solution_in_zero)

    if ('/' in function):
        return get_solution_function_with_fraction_in_point_for_differential(function)

    partial_derivative_of_x = get_solution_partial_derivative_of_x(function)
    partial_derivative_of_y = get_solution_partial_derivative_of_y(function)
    partial_derivative_of_z = get_solution_partial_derivative_of_z(function)

    point = Generate_point

    if (there_are_functions_with_solution_in_zero):
        point.x = point.y = point.z = 0

    if (there_are_functions_no_solution_in_zero):
        if ("cot" in function):
            point.x = point.y = point.z = math.pi/2
        else:
            while (point.x == 0 or point.y == 0 or point.z == 0):
                point = Generate_point

    solution = ""
    flag_sign_x = false
    flag_sign_y = false

    if (partial_derivative_of_x != 0):
        partial_derivative_of_x = partial_derivative_of_x[:-2]
        partial_derivative_of_x = str(parse_expr(partial_derivative_of_x).subs([(symbols('x'), point.x),
                                                                                (symbols('y'), point.y),
                                                                                (symbols('z'), point.z)]))
        solution += f'({partial_derivative_of_x})dx'
        flag_sign_x = true

    if (partial_derivative_of_y != 0):
        partial_derivative_of_y = partial_derivative_of_y[:-2]
        partial_derivative_of_y = str(parse_expr(partial_derivative_of_y).subs([(symbols('x'), point.x),
                                                                                (symbols('y'), point.y),
                                                                                (symbols('z'), point.z)]))
        if (flag_sign_x == true):
            solution += " + "
        solution += f'({partial_derivative_of_y})dy'
        flag_sign_y = true

    if (partial_derivative_of_z != 0):
        partial_derivative_of_z = partial_derivative_of_z[:-2]
        partial_derivative_of_z = str(parse_expr(partial_derivative_of_z).subs([(symbols('x'), point.x),
                                                                                (symbols('y'), point.y),
                                                                                (symbols('z'), point.z)]))
        if (flag_sign_x == true or flag_sign_y == true):
            solution += " + "
        solution += f'({partial_derivative_of_z})dz'

    if point.x == point.y == point.z == math.pi/2:
        point.x = point.y = point.z = "pi/2"

    if ("zoo" in solution or "I" in solution or "nan" in solution):
        return get_solution_function_in_point_for_differential()

    if (solution == ""):
        return Solution_differential_in_poin(function, 0, point)
    return Solution_differential_in_poin(function, solution, point)

def get_graf_of_function(function, x_range=(-10, 10), y_range=(-10, 10), filename='graph.png'):
    x = symbols('x')

    func = sympify(function)

    if func.has(symbols('z')):
        return

    if func.has(symbols('y')):

        y = symbols('y')

        if y_range is None:
            return

        x_values = np.linspace(x_range[0], x_range[1], 400)
        y_values = np.linspace(y_range[0], y_range[1], 400)
        X, Y = np.meshgrid(x_values, y_values)

        Z = np.array([[func.evalf(subs={x: x_val, y: y_val}) for x_val in x_values] for y_val in y_values])

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

        ax.set_title(f'График функции {function}')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    else:
        x_values = np.linspace(x_range[0], x_range[1], 400)
        y_values = [func.evalf(subs={x: val}) for val in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label=f'y = {function}')
        plt.title(f'График функции {function}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()

    plt.savefig(filename)
    plt.close()


# DOCUMENTATION:

# class Generate_point
# when creating an object of the class, the coordinates of the point are generated
# usage examples:
# point = Generate_point
# print(f'point ({point.x}; {point.y}; {point.z})

# class Solution_differential_in_point
# using for return information from method get_solution_function_in_point_for_differential()
# have a three fields: function (not her differential), solution (solution differential in point), point (object of class Generate_point)
# usage example:
# task = get_solution_function_in_point_for_differential()
# print(task.function)
# print(task.solution)
# print(f'({task.point.x}; {task.point.y}; {task.point.z})')

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

# get_random_function()
# this method returns random mathematic function, it may be ordinary function, function with fraction or function with nested functions
# usage examples:
# not used by the user, because the function is called from another function

# get_solution_function_with_fraction_in_point_for_differential(function)
# this method return object of class Solution_differential_in_point, which contains function with fraction
# usage examples:
# not used by the user, because the function is called from another function

# get_solution_function_in_point_for_differential()
# this method return object of class Solution_differential_in_point, which contains any function
# usage examples:
# task = get_solution_function_in_point_for_differential()
# print(task.function)
# print(task.solution)
# print(f'({task.point.x}; {task.point.y}; {task.point.z})')

# get_graf_of_function(function, x_range=(-10, 10), y_range=(-10, 10), filename='graph.png')
# this method takes function as input, also there are default arguments as range of x, range of y and filename,
# which can be changed. method returns nothing if function with three vars has been submitted, in the end method make
# .png file whith graf inside
# usage examples:
# get_graf_of_function(get_function_for_differential())