import turtle

jn = turtle.Screen()

cor_fundo = "lightgreen"
jn.bgcolor(cor_fundo)

def polygon( t , length , n ):

  t.color("blue")
  t.pensize(3)

  for i in range(n):
  
    t.forward(length)
    t.left(360/n)

joana = turtle.Turtle()
polygon(joana, 50, 7)

jn.mainloop()
