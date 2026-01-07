import os;

idade_usuario = int(input("Qual é a sua idade: "));

os.system('cls');
if idade_usuario >=0 and idade_usuario <= 12:
    print("Você é uma criança.\n"); 
elif idade_usuario >= 13 and idade_usuario <= 18 :
    print("Você é um adolescente.\n"); 
else:
    print("Você é um adulto.\n"); 
