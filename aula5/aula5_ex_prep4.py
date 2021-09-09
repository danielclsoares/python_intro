import turtle
import math

jn = turtle.Screen()

cor_fundo = "lightgreen"
jn.bgcolor(cor_fundo)

def polygon(t,length, n):

  t.color("blue")
  t.pensize(3)

  for i in range(n):
  
    t.forward(length)
    t.left(360/n)

def circle( t , r ):
  
  polygon( t , 6.283185 , r)

joana = turtle.Turtle()
circle(joana, 75)

jn.mainloop()
