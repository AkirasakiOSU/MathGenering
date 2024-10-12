import os
import TexGenerator
import ProblemGenerator

from os import write

from ProblemGenerator import generate_polinom
from TexGenerator import getTexStrokes

tex = open("test.tex", "w")
problems = []
for i in range(1,11):
    problems.append(ProblemGenerator.get_polinom(2, 3))

for str in getTexStrokes(problems):
    tex.write(str)
tex.close()

os.system("pdflatex test.tex")
