import sympy as sp
def getTexStrokes(problems):
    strokes = ["\\documentclass{article}\n",
               "\\begin{document}\n"
               ]
    for problem in problems:
        result = "$$ "
        problem = problem.replace('^', '**')
        x, y, z = sp.symbols('x y z')
        expression = sp.sympify(problem)
        latex_code = sp.latex(expression)
        result += latex_code + " $$ \n"
        strokes.append(result)
    strokes.append("\\end{document}")
    return strokes