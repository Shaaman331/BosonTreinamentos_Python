import random

print("Gerar 5 numeros aleatórios entre 1 e 50: \n")
for i in range(5):
    n = random.randint(1, 50)
    print(f"Numero gerado: {n}")


valor01 = random.random()
print(f"Numero gerado: {valor01 * 10}")
print(f"Numero gerado: {round(valor01 * 100, 2)}")

valo02 = random.uniform(1, 1000)
print(f"Numero gerado: {round(valo02, 4)}")

l = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(l)
print(f"Numero sorteado: {n}")
n = random.sample(l, 3)
print(f"Numeros sorteados: {n}")
