from abc import ABC, abstractmethod
import importlib.util
import os
file_path = os.path.abspath("..\\Derivative_generation\\Math_func_generation.py")
spec = importlib.util.spec_from_file_location("Math_func_generation", file_path)
mathGen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mathGen)

"""
0 - Дифференциал без деления
1 - Дифференциал с делением
2 - Дифференциал сложной функции
3 - Частная производная по х
4 - Частная производная по y
5 - Частная производная по z
6 - Значение дифференциала функции в точке !!!
7 - Неопределённый интеграл
8 - Определённый интеграл
9 - Предел
"""

problemFunctions = [
    mathGen.get_function_for_differential,
    mathGen.get_function_with_fraction_for_differential,
    mathGen.get_function_with_nested_functions_for_differential,
    mathGen.get_random_function,
    mathGen.get_random_function,
    mathGen.get_random_function,
    mathGen.get_solution_function_in_point_for_differential,
    mathGen.generate_function,  # Затычка
    mathGen.generate_function,  # Затычка
    mathGen.generate_function   # Затычка
]

solutionFunctions = [
    mathGen.get_solution_function_for_differential,
    mathGen.get_solution_function_with_fraction_for_differential,
    mathGen.get_solution_function_with_nested_functions_for_differential,
    mathGen.get_solution_partial_derivative_of_x,
    mathGen.get_solution_partial_derivative_of_y,
    mathGen.get_solution_partial_derivative_of_z,
    mathGen.generate_function,  # Вечная затычка тк генератор задачи сразу возвращает всё
    mathGen.generate_function,  # Затычка
    mathGen.generate_function,  # Затычка
    mathGen.generate_function,  # Затычка
]

class Iproblem(ABC):
    @abstractmethod
    def getProblem(self):
        pass
    @abstractmethod
    def getSolution(self):
        pass

class SimpleDifferentialProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 0
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class DifferentialWithFarctionProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 1
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class NestedDifferentialProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 2
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class PartialDerivativeOfXProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 3
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution


class PartialDerivativeOfYProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 4
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution


class PartialDerivativeOfZProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 5
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem](self.problem)

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class SolutionInPointProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 6
        task = problemFunctions[self.typeOfProblem]()
        self.problem = task.function
        self.solution = task.solution
        self.point = task.point

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

    def getPoint(self):
        return self.point

class IntegralProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 7
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem]()

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class RimanIntervalProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 8
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem]()

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

class LimitProblem(Iproblem):
    def __init__(self):
        self.typeOfProblem = 9
        self.problem = problemFunctions[self.typeOfProblem]()
        self.solution = solutionFunctions[self.typeOfProblem]()
        self.point = 0

    def getProblem(self):
        return self.problem

    def getSolution(self):
        return self.solution

    def getPoint(self):
        return self.point
