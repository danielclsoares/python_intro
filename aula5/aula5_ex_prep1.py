import turtle

jn = turtle.Screen()

cor_fundo = str(input("digite a cor do fundo:"))
jn.bgcolor(cor_fundo)

def square(t):

  t.color("blue")
  t.pensize(3)

  for i in [0, 1, 2, 3]:
  
    t.forward(50)
    t.left(90)

joana = turtle.Turtle()
square(joana)

jn.mainloop()
