lista = [2,6,9,4,0,12,3,7]

for item in lista:
    print(item)

palavra = "informatica"
for letra in palavra:
    print(letra)

for numero in range(1,11):
    print(numero)
    for indice, valor in enumerate(lista):
        print(f"Indice: {indice}, Valor: {valor}")


nome = input("Digite seu nome: ")
for x in range(10):
    print(f"{x + 1} {nome}")

for y in range(2, 20, 2):
    print(y)

for z in range(20, 1, -2):
    print(z)

pedras = ("Rubi", "Esmeralda", "Quartzo", "Safira", "Diamante")
for pedra in pedras:    
    if pedra == "Quartzo":
        continue
    print(pedra)

