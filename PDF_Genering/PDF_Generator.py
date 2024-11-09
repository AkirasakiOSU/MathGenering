import importlib.util
import random
import sympy as sp
import os
import glob
import Problems

from mpmath.libmp import to_str



class WriterBuilder:
    def __init__(self):
        self.container = {
            "pathForResult": "//DefaultPath//",
            "institution": "DefaultInstitution",
            "department": "DefaultDepartment",
            "direction": "DefaultDirection",
            "profile": "DefaultProfile",
            "formOfEducation": "DefaultFormOfEducation",
            "kurs": "DefaultKurs",
            "discipline": "DefaultDiscipline",
            "nameOfWork": "DefaultNameOfWork",
            "numberOfKR": "DefaultNumberOfKR"
        }

    def setPathForResult(self, pathForResult):
        self.container["pathForResult"] = pathForResult

    def setInstitution(self, institution):
        self.container["institution"] = institution

    def setDepartment(self, department):
        self.container["department"] = department

    def setDirection(self, direction):
        self.container["direction"] = direction

    def setProfile(self, profile):
        self.container["profile"] = profile

    def setFormOfEducation(self, formOfEducation):
        self.container["formOfEducation"] = formOfEducation

    def setKurs(self, kurs):
        self.container["kurs"] = kurs

    def setDiscipline(self, discipline):
        self.container["discipline"] = discipline

    def setNameOfWork(self, nameOfWork):
        self.container["nameOfWork"] = nameOfWork

    def setNumberOfKR(self, numberOfKR):
        self.container["numberOfKR"] = numberOfKR

    def build(self):
        return Writer(self.container)

    def clear(self):
        self.container = {
            "pathForResult": "//DefaultPath//",
            "institution": "DefaultInstitution",
            "department": "DefaultDepartment",
            "direction": "DefaultDirection",
            "profile": "DefaultProfile",
            "formOfEducation": "DefaultFormOfEducation",
            "kurs": "DefaultKurs",
            "discipline": "DefaultDiscipline",
            "nameOfWork": "DefaultNameOfWork",
            "numberOfKR": "DefaultNumberOfKR"
        }

class Writer:
    def __init__(self, container):
        self.container = container

    def __generateProblemTex(self, numberOfVar, typesOfProblems, countOfProblems, containerForProblems):
        strokes = [
            headerForProblemTex.format(
                self.container["institution"],
                self.container["department"],
                self.container["direction"],
                self.container["profile"],
                self.container["formOfEducation"],
                self.container["kurs"],
                self.container["discipline"],
                self.container["nameOfWork"],
                self.container["numberOfKR"],
                numberOfVar
            ),
            "\\begin{enumerate}\n"
        ]
        if len(typesOfProblems) != len(countOfProblems): raise Exception("Error")
        number = 0
        con = []
        for typeOfProblem in typesOfProblems:
            strokes.append("\\item " + questionsForProblems[typeOfProblem] + "\n")
            strokes.append("\\begin{enumerate}[label=\\alph*)]\n")
            for i in range(countOfProblems[numberOfVar]):
                stroke = "\\item $ "
                problem = classMap[typeOfProblem]()
                con.append(problem)
                stroke += sp.latex(sp.sympify(problem.getProblem()))
                strokes.append(stroke + " $\n")
            number += 1
            containerForProblems.append(con.copy())
            con.clear()
            strokes.append("\\end{enumerate}\n")
        strokes.append("\\end{enumerate}\n")
        strokes.append("\\end{document}")
        return strokes

    def __generateSolutionTex(self, numberOfVar, containerForProblems):
        strokes = [
            headerForAnsverTex.format(numberOfVar),
            "\\begin{enumerate}\n"
        ]
        for problems in containerForProblems:
            strokes.append("\\item " + questionsForProblems[problems[0].typeOfProblem] + "\n")
            strokes.append("\\begin{enumerate}[label=\\alph*]\n")
            for problem in problems:
                stroke = "\\item $ " + sp.latex(sp.sympify(str(problem.getSolution()))) + " $\n"
                strokes.append(stroke)
            strokes.append("\\end{enumerate}\n")
        strokes.append("\\end{enumerate}\n")
        strokes.append("\\end{document}")
        return strokes





    def __getIdOfFile(self):
        # Получаем список всех файлов в директории
        files = os.listdir(self.container["pathForResult"])
        # Инициализируем максимальное значение n
        max_n = 0
        # Перебираем файлы и находим максимальное n для файлов с расширением .pdf
        for filename in files:
            # Проверяем, что файл имеет формат "число.pdf"
            if filename.endswith(".pdf") and filename[:-4].isdigit():
                # Извлекаем число из имени файла и обновляем max_n
                n = int(filename[:-4])
                max_n = max(max_n, n)
        # Возвращаем n+1
        return max_n + 1

    def writeProblemAndSolution(self, numberOfVar, typesOfProblems, countOfProblems):
        nextIdForFile = self.__getIdOfFile()
        problemFile = open(f"{nextIdForFile}.tex", "w", encoding="utf-8")
        solutionFile = open(f"a_{nextIdForFile}.tex", "w", encoding="utf-8")
        problemsForSolution = []
        for stroke in self.__generateProblemTex(numberOfVar, typesOfProblems, countOfProblems, problemsForSolution):
            problemFile.write(stroke)
        for stroke in self.__generateSolutionTex(numberOfVar, problemsForSolution):
            solutionFile.write(stroke)
        problemFile.close()
        solutionFile.close()
        os.system(f"pdflatex -output-directory={self.container["pathForResult"]} {nextIdForFile}.tex")
        os.system(f"pdflatex -output-directory={self.container["pathForResult"]} a_{nextIdForFile}.tex")
        deleteFiles(self.container["pathForResult"], "aux")
        deleteFiles(self.container["pathForResult"], "log")
        deleteFiles("./", "tex")



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

questionsForProblems = [
    "Найдите полный дифференциал.",
    "Найдите полный дифференциал.",
    "Найдите полный дифференциал.",
    "Найдите частную производную по x.",
    "Найдите частную производную по y.",
    "Найдите частную производную по z.",
    "Найдите значение дифференциала функции в заданной точке.",
    "Найдите неопределённый интеграл.",
    "Найдите определённый интеграл.",
    "Найдите предел функции."
]

classMap = {
    0 : Problems.SimpleDifferentialProblem,
    1 : Problems.DifferentialWithFarctionProblem,
    2 : Problems.NestedDifferentialProblem,
    3 : Problems.PartialDerivativeOfXProblem,
    4 : Problems.PartialDerivativeOfYProblem,
    5 : Problems.PartialDerivativeOfZProblem,
    6 : Problems.SolutionInPointProblem,
    7 : Problems.IntegralProblem,
    8 : Problems.RimanIntervalProblem,
    9 : Problems.LimitProblem
}

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
    \\Large{{Ответы}}\n
    \\Large{{Вариант {}}}\n
    \\end{{center}}\n
"""

# format(institution, department, direction, profile, formOfEducation, kurs, discipline, nameOfWork, numberOfKR, numberOfVariant)

def deleteFiles(directory, extension):
    search_pattern = os.path.join(directory, f"*.{extension}")
    files_to_delete = glob.glob(search_pattern)
    for file in files_to_delete:
        os.remove(file)