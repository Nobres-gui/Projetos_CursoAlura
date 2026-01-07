import os;

numero_escolhido = int(input("Escolha um número: "));

if numero_escolhido % 2 == 0:
    os.system('cls')
    print(f"O número escolhido foi o {numero_escolhido} e ele é par\n");
else: 
    os.system('cls')
    print(f"O número escolhido foi o {numero_escolhido} e ele é impar\n");