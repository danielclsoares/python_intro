import turtle

jn = turtle.Screen()

cor_fundo = "yellow"
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()

joana.up()
joana. goto(-100,0)
joana.down()
joana.color("blue")
joana.pensize(3)
joana.shape("turtle")
joana.speed(3)

for j in [0, 1, 2, 3]:

  for i in [0, 1, 2, 3, 4]:
  
    joana.forward( 50 )
    joana.right( 180 - 36 )
  
  joana.up()
  joana.forward( 70 )
  joana.down()
  
jn.mainloop()
