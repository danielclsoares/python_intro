import turtle

jn = turtle.Screen()

cor_fundo = "red"
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()

joana.color("blue")
joana.pensize(3)
joana.shape("turtle")
joana.speed(9)

for i in [0, 1, 2, 3, 4]:
  
  joana.forward( 100)
  joana.right( 180 - 36 )

jn.mainloop()
