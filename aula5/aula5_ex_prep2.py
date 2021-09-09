import turtle

jn = turtle.Screen()

cor_fundo = "orange"
jn.bgcolor(cor_fundo)

def square(t,length):

  t.color("blue")
  t.pensize(3)

  for i in [0, 1, 2, 3]:
  
    t.forward(length)
    t.left(90)

joana = turtle.Turtle()
square(joana, 75)

jn.mainloop()
