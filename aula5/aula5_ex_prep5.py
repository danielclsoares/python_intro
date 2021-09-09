import turtle
import math

jn = turtle.Screen()

cor_fundo = "lightgreen"
jn.bgcolor(cor_fundo)

def polygon_arc(t,length, n , angulo):

  t.color("blue")
  t.pensize(3)

  for i in range(n*angulo//360):
  
    t.forward(length)
    t.left(360/n)

def arc( t , r , angulo):

  polygon_arc( t , 2 * math.pi , r , angulo)

joana = turtle.Turtle()
arc(joana, 60 , 360)

jn.mainloop()
