import random


for cont_ex in range(1, 6):
    print(f"\nRodada: {cont_ex}")  
    for cont_in in range(5, 0, -1): 
        print(f"Contador Interno: {cont_in}")
    
print("Fim do programa")


for A in range(1, 6):
    print(f"\Conjunto {A}")
    for b in range(5):
        num =random.randint(1, 100)
        print(f"Número sorteado: {num}")
        print("\nFim do sorteio de números")
        
