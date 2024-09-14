notas = [5,6,7,8,9]
print(notas)

n1 = [4,5,6,7,8,9]
n2 = [1,2,3,10,11,12]
valores = n1 + n2
print(valores[0])
print(len(valores))
print(sorted(valores))
print(sum(valores))

valores.append(13)
print(valores)
valores.pop(3)
print(valores)
valores.insert(3, 21)
print(valores)
print(12 in valores)

planetas = ["Mercurio", "Venus", "Marte", "Saturno", "Urano","Neturno"]
for planeta in planetas:
    print(planetas)

bebidas = []
for i in range(5):
    print(f"Digite uma bebida favorita: ")
    bebida = input()
    bebidas.append(bebida)
bebidas.sort()

print(f"\nBebidas escolhidas")
for bebida in bebidas:
    print(bebida)

print(f"\nSaude")



