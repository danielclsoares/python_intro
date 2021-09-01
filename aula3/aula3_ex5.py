import math

def IMC( m , h ):
  """ funcao para calcular o IMC """
  indice = m/(h**2)
  print("seu IMC é" , indice)
  return indice

def volume_esfera(r):
  """funcao para calcular o volume 
  da esfera de raio r """
  v = (4*math.pi*r**3)/3
  print("o volume da esfera é" , v)
  return v

def max_consec( l , dist, esp):
  """funcao para calcular a distancia entre maximos
  consecutivos no padrao de interferência formado no
  experimento de Young-Fresnel, recebendo os valores
  do comprimento de onda l, da distancia entre as fendas
  e o anteparo e da espessura da fenda esp, sendo essas
  tres medidas em m.
  """
  y = l*dist/esp
  print("a distancia entre os maximos consecutivos é" , y, "m")
  return y
