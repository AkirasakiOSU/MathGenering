import importlib.util
import random
import sympy as sp
import os
import glob
file_path = os.path.abspath("..\\Derivative_generation\\Math_func_generation.py")
spec = importlib.util.spec_from_file_location("Math_func_generation", file_path)
mathGen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mathGen)
"""
0 - Дифференциал без деления
1 - Дифференциал с делением
2 - Дифференциал сложной функции
3 - Неопределённый интеграл
4 - Определённый интеграл
5 - Предел
"""

problemFunctions = [
    mathGen.get_function_for_differential,
    mathGen.get_function_with_fraction_for_differential,
    mathGen.get_function_with_nested_functions_for_differential,
    mathGen.generate_function,  # Затычка
    mathGen.generate_function,  # Затычка
    mathGen.generate_function   # Затычка
]

solutionFunctions = [
    mathGen.get_solution_function_for_differential,
    mathGen.get_solution_function_with_fraction_for_differential,
    mathGen.get_solution_function_with_nested_functions_for_differential,
    mathGen.generate_function,
    mathGen.generate_function,
    mathGen.generate_function,
]

problemQuestions = [
    "Вычислите полный дифферинциал функции",
    "Вычислите полный дифферинциал функции",
    "Вычислите полный дифферинциал функции",
    "Решите неопределённый интеграл",
    "Решите определённый интеграл",
    "Найдите предел функции",
]

headerForProblem = [
    "d\\left( ",
    "d\\left( ",
    "d\\left( ",
    "\\int \\left( ",
    "\\int_{{{}}}^{} \\left( ",
    "\\lim _{{x \\to {} }} \\left( ",
]

footerForProblem = [
    " \\right) ?",
    " \\right) ?",
    " \\right) ?",
    " \\right) dx",
    " \\right) dx",
    " \\right)"
]

headerForProblemTex = """
    \\documentclass[20pt, a4paper]{{article}}
    \\usepackage[T2A]{{fontenc}}
    \\usepackage[utf8]{{inputenc}}
    \\usepackage[russian]{{babel}}
    \\usepackage{{geometry}}
    \\usepackage{{enumitem}}
    \\usepackage{{amsmath}}
    \\usepackage{{graphicx}}
    \\usepackage{{fancyhdr}}
    \\geometry{{left=1cm, right=0cm, top=0.5cm, bottom=0cm}}
    \\begin{{document}}
    \\Large{{
    \\begin{{center}}
    {}
    \\end{{center}}
    Кафедра: {}\\\\
    Направление подготовки: {}\\\\
    Профиль: {}\\\\
    Форма обучения: {}\\\\
    Курс: {}\\\\
    Дисциплина: {}\\\\
    }}
    \\begin{{center}}
    {} №{}
    \\end{{center}}
    \\begin{{center}}
    \\LARGE Вариант № {}
    \\end{{center}}
    \\vspace{{2cm}}
"""

headerForAnsverTex = """
    \\documentclass[20pt, a4paper]{{article}}\n
    \\usepackage[T2A]{{fontenc}}\n
    \\usepackage[utf8]{{inputenc}}\n
    \\usepackage[russian]{{babel}}\n
    \\usepackage{{geometry}}\n
    \\usepackage{{enumitem}}\n
    \\usepackage{{amsmath}}\n
    \\usepackage{{graphicx}}\n
    \\usepackage{{fancyhdr}}\n
    \\geometry{{left=1cm, right=0cm, top=0.5cm, bottom=0cm}}\n
    \\begin{{document}}\n
    \\begin{{center}}\n
    \\Large{{Ответы}}
    \\end{{center}}\n
"""

# format(institution, department, direction, profile, formOfEducation, kurs, discipline, nameOfWork, numberOfKR, numberOfVariant)

def deleteFiles(directory, extension):
    search_pattern = os.path.join(directory, f"*.{extension}")
    files_to_delete = glob.glob(search_pattern)
    for file in files_to_delete:
        os.remove(file)

def getProblem(typeOfProblem):
    return problemFunctions[typeOfProblem]()

def generateTexOfProblem(
    arrayForProblem,
    institution,
    department,
    direction,
    profile,
    formOfEducation,
    kurs,
    discipline,
    nameOfWork,
    numberOfKR,
    typesOfProblem,
    countOfProblems,
    numberOfVariant
):
    strokes = [
        headerForProblemTex.format(institution, department, direction, profile, formOfEducation, kurs, discipline, nameOfWork, numberOfKR, numberOfVariant)
    ]
    i = 0
    strokes.append("\\begin{enumerate}[label=\\Alph*., start=1]")
    for numberOfProblem in typesOfProblem:
        if numberOfProblem >= len(problemQuestions):
            raise IndexError(f"Индекс {numberOfProblem} выходит за пределы допустимого диапазона для problemQuestions")
        strokes.append(f"\\item \\Large {problemQuestions[numberOfProblem]}\n")
        strokes.append("\\begin{enumerate}[label=\\arabic*., itemsep=10pt, leftmargin=5pt]")
        for j in range(countOfProblems[i]):
            result = "\\item\n$ \\displaystyle\n"
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            while b < a:
                b = random.randint(-100, 100)
            result += headerForProblem[numberOfProblem].format(a, b)
            problem = getProblem(numberOfProblem)
            arrayForProblem.append([problem, numberOfProblem])
            result += sp.latex(sp.sympify(problem))

            result += footerForProblem[numberOfProblem]
            result += "\n$\n"
            strokes.append(result)
        i += 1
        strokes.append("\\end{enumerate}\n")
    strokes.append("\\end{enumerate}\n")
    strokes.append("\\end{document}\n")
    return strokes

def generateTexOfAnsvers(problems) :
    result = [
        headerForAnsverTex.format()
    ]
    f = -1
    result.append("\\begin{enumerate}[label=\\Alph*., start=1]\n")
    for problem in problems:
        if f != problem[1]:
            if f != -1:
                result.append("\\end{enumerate}\n")
            result.append(f"\\item \\Large {problemQuestions[problem[1]]}\n")
            result.append("\\begin{enumerate}[label=\\arabic*., itemsep=10pt, leftmargin=5pt]\n")
            f = problem[1]
        if problem[1] <= 2:
            ansver = solutionFunctions[problem[1]](problem[0])
        else:
            ansver = solutionFunctions[problem[1]]()
        result.append(f" \\item $ {sp.latex(sp.sympify(ansver))} $ \n")
    result.append("\\end{enumerate}\n")
    result.append("\\end{enumerate}\n")
    result.append("\\end{document}\n")
    return result

def generateProblemsAndAnswers(
        pathForResult,
        countOfFiles,
        typesOfProblem,
        countOfProblems,
        institution,
        department,
        direction,
        profile,
        formOfEducation,
        kurs,
        discipline,
        nameOfWork,
        numberOfKR
):
    if len(typesOfProblem) != len(countOfProblems):
        raise ValueError("Error (я не придумал как подробнее ее описать :3)")
    for fileNumber in range(countOfFiles):
        arrayForProblem = []
        file = open(f"{fileNumber + 1}.tex", "w", encoding="utf-8")
        for stroke in generateTexOfProblem(arrayForProblem, institution, department, direction, profile, formOfEducation, kurs,
                                           discipline, nameOfWork, numberOfKR, typesOfProblem, countOfProblems,
                                           fileNumber + 1):
            file.write(stroke)
        file.close()
        os.system(f"pdflatex -output-directory={pathForResult} {fileNumber + 1}.tex")
        deleteFiles(pathForResult, "aux")
        deleteFiles(pathForResult, "log")
        deleteFiles("./", "tex")
        ansversFile = open(f"ansvers_{fileNumber + 1}.tex", "w", encoding="utf-8")
        for stroke in generateTexOfAnsvers(arrayForProblem):
            ansversFile.write(stroke)
        ansversFile.close()
        os.system(f"pdflatex -output-directory={pathForResult} ansvers_{fileNumber + 1}.tex")
        deleteFiles(pathForResult, "aux")
        deleteFiles(pathForResult, "log")
        deleteFiles("./", "tex")