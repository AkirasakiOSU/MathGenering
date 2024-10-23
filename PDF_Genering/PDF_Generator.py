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
2 - Неопределённый интеграл
3 - Определённый интеграл
4 - Предел
"""

problemFunctions = [
    mathGen.get_function_for_differential,
    mathGen.get_function_with_fraction_for_differential,
    mathGen.generate_function,  # Затычка
    mathGen.generate_function,  # Затычка
    mathGen.generate_function   # Затычка
]

problemQuestions = [
    "Вычислите производную функции",
    "Вычислите производную функции",
    "Решите неопределённый интеграл",
    "Решите определённый интеграл",
    "Найдите предел функции",
]

headerForProblem = [
    "\\left( ",
    "\\left( ",
    "\\int \\left( ",
    "\\int_{{{}}}^{} \\left( ",
    "\\lim _{{x \\to {} }} \\left( ",
]

footerForProblem = [
    " \\right)_{x}'",
    " \\right)_{x}'",
    " \\right) dx",
    " \\right) dx",
    " \\right)"
]

headerForTex = """
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
# format(institution, department, direction, profile, formOfEducation, kurs, discipline, nameOfWork, numberOfKR, numberOfVariant)

def deleteFiles(directory, extension):
    search_pattern = os.path.join(directory, f"*.{extension}")
    files_to_delete = glob.glob(search_pattern)
    for file in files_to_delete:
        os.remove(file)

def getProblem(typeOfProblem):
    return problemFunctions[typeOfProblem]()

def generateTexOfProblem(
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
        headerForTex.format(institution, department, direction, profile, formOfEducation, kurs, discipline, nameOfWork, numberOfKR, numberOfVariant)
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
            result += sp.latex(sp.sympify(getProblem(numberOfProblem)))

            result += footerForProblem[numberOfProblem]
            result += "\n$\n"
            strokes.append(result)
        i += 1
        strokes.append("\\end{enumerate}\n")
    strokes.append("\\end{enumerate}\n")
    strokes.append("\\end{document}\n")
    return strokes

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
        raise ValueError("Ошибка (я не придумал как подробнее ее описать :3)")
    for fileNumber in range(countOfFiles):
        file = open(f"{fileNumber + 1}.tex", "w", encoding="utf-8")
        for stroke in generateTexOfProblem(institution, department, direction, profile, formOfEducation, kurs,
                                           discipline, nameOfWork, numberOfKR, typesOfProblem, countOfProblems,
                                           fileNumber + 1):
            file.write(stroke)
        file.close()
        os.system(f"pdflatex -output-directory={pathForResult} {fileNumber + 1}.tex")
    deleteFiles(pathForResult, "aux")
    deleteFiles(pathForResult, "log")
    deleteFiles("./", "tex")