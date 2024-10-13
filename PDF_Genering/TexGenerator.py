import sympy as sp
import os
import ProblemGenerator
import glob

def getTexStrokes(problems, typeOfProblem):
    strokes = ["\\documentclass{article}\n",
               "\\begin{document}\n"
               ]
    for problem in problems:
        result = "$$ "
        if typeOfProblem == 0:
            result += "\\int "
        elif typeOfProblem == 1:
            result += "\\int_0^\\infty "
        elif typeOfProblem == 2:
            result += "\\lim _{x \\to \\infty } "
        elif typeOfProblem == 3:
            result += "( "
        problem = problem.replace('^', '**')
        x, y, z = sp.symbols('x y z')
        expression = sp.sympify(problem)
        latex_code = sp.latex(expression)
        result += latex_code
        if typeOfProblem == 3:
            result += " )'"
        result += " $$ "
        strokes.append(result)
    strokes.append("\\end{document}")
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
        tex = open(f"{i+1}.tex", "w")
        problems = []
        for a in range(0, countOfProblems):
            problems.append(ProblemGenerator.get_polinom(2, 3))

        for str in getTexStrokes(problems, typeOfProblem):
            tex.write(str)
        tex.close()
        os.system(f"pdflatex -output-directory={path} {i+1}.tex")
    delete_files_with_extension(path, "aux")
    delete_files_with_extension(path, "log")
    delete_files_with_extension("./", "tex")