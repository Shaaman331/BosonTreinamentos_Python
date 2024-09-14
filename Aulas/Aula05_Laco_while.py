num = 1
while(num <= 1000):
    print(num)
    num += 1
print("Laco encerrado !")


nome = None

while True:
    print("Digite seu nome, ou x para parar o laco")
    nome = input()
    if nome == "x" or nome == "X":
        break
    print(f"Bem-vindo, {nome}!")

print("Até logo !")

