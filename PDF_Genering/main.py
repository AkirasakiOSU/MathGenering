import os
from os import write


def getOutput(string) :
    str = ["\\documentclass{article}\n", "\\begin{document}\n"]
    str.append(string + "\n")
    str.append("\\end{document}")
    return str

tex = open("test.tex", "w")
string = "sasa"
for str in getOutput("sasa"):
    tex.write(str)
tex.close()

os.system("pdflatex test.tex")