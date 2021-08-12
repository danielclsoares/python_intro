import math

# Para saber a velocidade final de um corpo em queda livre,
# Usamos a fórmula de Torricelli, com velocidade inicial 0m/s

# Declarando as variáveis:
g = 9.8
h = 3
#onde g é a aceleração da gravidade e h a altura na qual ele se encontra na situação inicial.

v = (math.sqrt(2*g*h))
print(v)

# O tempo decorrido, sai da equação horária da velocidade:

t = v/g
print(t)
