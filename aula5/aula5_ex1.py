import turtle

jn = turtle.Screen()

cor_fundo = str(input("digite a cor do fundo:"))
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()

joana.color("blue")
joana.pensize(3)

for i in [0, 1, 2, 3]:
  
  joana.forward(50)
  joana.left(90)

jn.mainloop()
