livro = 24.95 # Preço do livro
desconto = livro - 0.4*livro # Preço do livro com desconto

custo_de_envio = 0.75 
n_livros = 60 #Número de livros pedidos
custo_total = n_livros*(desconto + custo_de_envio)+ (3- .75)

print(custo_total)
