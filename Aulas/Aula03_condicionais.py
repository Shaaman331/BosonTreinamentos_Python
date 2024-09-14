n1 = n2 = 0.0 
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#Calcular a média das notas 
media = (n1 + n2) / 2.0

if (media >= 7.0):
    print("Aluno Aprovado com nota:", media)
    print("Parabéns!")
elif (media >= 5.0):
    print("Aluno está em recuperacao:", media)
else:
    print("Aluno reprovado...")

print("Sua média é {}".format(media))

