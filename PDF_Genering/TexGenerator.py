import importlib.util
import random

import sympy as sp
import os
import glob
file_path = os.path.abspath("..\\Derivative_generation\\Math_func_generation.py")
spec = importlib.util.spec_from_file_location("Math_func_generation", file_path)
mathGen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mathGen)

problem = [
    "Решите неопределённый интеграл",
    "Решите определённый интеграл",
    "Найдите передел функции",
    "Вычислите произвудную функции"
]

headerForProblem = [
    "\\int ",
    "\\int_{{{}}}^{}",
    "\\lim _{{x \\to {} }} "
]

def getTexStrokes(problems, typeOfProblem, author):
    strokes = [
        "\\documentclass[20pt, a4paper]{article}\n",
        "\\usepackage[T2A]{fontenc}\n",
        "\\usepackage[utf8]{inputenc}\n",
        "\\usepackage[russian]{babel}\n",
        "\\usepackage{geometry}\n",
        "\\usepackage{enumitem}\n",
        "\\usepackage{amsmath}\n",
        "\\geometry{left=2cm, right=2cm, top=2cm, bottom=2cm}\n",
        "\\title{Контрольная работа}\n",
        f"\\author{{{author}}}\n",
        "\\date{\\today}\n",
        "\\begin{document}\n",
        "\\maketitle\n",
        "\\vspace{2cm}\n",
        "\\begin{enumerate}[label=\\arabic*., itemsep=10pt, leftmargin=5pt]\n"
    ]

    for problem in problems:
        result = "\\item\n$ \\displaystyle\n"
        if typeOfProblem == 0:
            result += headerForProblem[typeOfProblem]
        elif typeOfProblem == 1:
            result += (headerForProblem[typeOfProblem].format(random.randint(-100, 100), random.randint(-100, 100)))
        elif typeOfProblem == 2:
            result += (headerForProblem[typeOfProblem].format(random.randint(-100, 100)))
        elif typeOfProblem == 3:
            result += "( "
        expression = sp.sympify(problem)
        latex_code = sp.latex(expression)
        result += latex_code

        if typeOfProblem == 3:
            result += " )'"

        result += "\n$\n"
        strokes.append(result)

    strokes.append("\\end{enumerate}\n")
    strokes.append("\\end{document}\n")
    return strokes


def delete_files_with_extension(directory, extension):
    # Формируем шаблон для поиска файлов
    search_pattern = os.path.join(directory, f"*.{extension}")

    # Ищем все файлы с данным расширением
    files_to_delete = glob.glob(search_pattern)

    # Удаляем каждый найденный файл
    for file in files_to_delete:
        os.remove(file)

def generateFiles(path, countOfFiles, countOfProblems, typeOfProblem):
    for i in range(0, countOfFiles):
        tex = open(f"{i+1}.tex", "w", encoding="utf-8")
        problems = []
        for a in range(0, countOfProblems):
            problems.append(mathGen.get_polinom(2, 3))

        for str in getTexStrokes(problems, typeOfProblem, "Романуджан"):
            tex.write(str)
        tex.close()
        os.system(f"pdflatex -output-directory={path} {i+1}.tex")
    delete_files_with_extension(path, "aux")
    delete_files_with_extension(path, "log")
    delete_files_with_extension("./", "tex")