import math

# Declarando os coeficientes da equação
a = 3
b = -4
c = -10

# Encontrando as raízes através da fórmula de Bhaskara
x1 = (-b + math.sqrt(b**2 -4*a*c))/2*a
x2 = (-b - math.sqrt(b**2 -4*a*c))/2*a

print(x1, x2, sep = ";")
