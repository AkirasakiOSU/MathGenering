import TexGenerator
from ProblemGenerator import generate_polinom
from TexGenerator import getTexStrokes


"""
0 - Неопр интеграл
1 - Опр интеграл
2 - Предел
3 - Дифф
"""

TexGenerator.generateFiles(".\\Result\\", 10, 10, 3)