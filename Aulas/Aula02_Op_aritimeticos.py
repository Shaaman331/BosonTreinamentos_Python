print("Operadores Aritiméticos")
x = y = z = 0

#fazendo casting
x = int(input("Digite um número: "))
y = int(input("Digite outro número: ")) 
z = x + y 
print("O valor da soma é:", z)


#Operadodes de comparaçao

a= b= c= False
n1 = n2 = 0

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

a = n1 == n2
print("São iguais? ", a, "\n") #concatenado

c = n1 > n2
print(n1,"é maior que ",n2, "?", c , "\n")

b = n1 != n2
print("São diferentes ?" +  str(b)) #Convertendo a var b em string


#Operadores Lógicos

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.75)
msg = "Pode participar do evento? " + str(resultado)
print(msg)

#Programa de disparo de alarmes

porta = "f"
janela = "f"

alarme = (porta == "a") or (janela == "a")
msg= "O alarme foi disparado? ", + str(alarme)
print(msg)

tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
msg = "Tem dinheiro? ", str(tem_dinheiro)
print(msg)
