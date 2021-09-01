import turtle

jn = turtle.Screen()

cor_fundo = str(input("digite a cor do fundo:"))
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()

cor_tartaruga = str(input("digite a cor da tartaruga:"))
joana.color("blue")
espessura = int(input("digite a espessura da caneta"))
joana.pensize(3)

for i in [0, 1, 2, 3]:
  
  joana.forward(50)
  joana.left(90)

jn.mainloop()
