#Sintaxe:
#print(objetos, argumentos)

mensagem = "Funcao print"
print(mensagem)

nome = "Tarcisio"
print("Boson Treinamentos -", nome)

nome01 = input("Digite seu nome: ")
print("Olá " + nome + " Bem-vindo ao curso de python")
msg="Olá  {} Bem-vindo ao curso de python".format(nome01)
print(msg)

nome02 = "Lucca"
idade = "30"    
print(f"Nome: {nome02}\tidade: {idade}")
