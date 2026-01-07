# 1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.
# 2. Escreva um código para importar a biblioteca numpy com o alias np.
import numpy as np;
from random import choice, randrange, choices;
from math import pow;

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
print("***** Número Aleatório *****");
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77];
numero_escolhido = choice(lista);
print(f"o número escolhido foi {numero_escolhido}\n");

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
print("***** Sorteiro de número *****");
numero_sorteado = randrange(100);
print(f"O número sorteado foi {numero_sorteado}\n");

# 5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
print("***** Calculadora de Potência *****");
n1 = int(input("Escolha o número base: "));
n2 = int(input("Escolha o número expoente: "));

res_potencia = pow(n1, n2);
print(res_potencia)

# 6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
print("***** Calculadora Ganhador *****");

qtd_participantes = int(input("Quantas pessoas estão participando do sorteio: "));
participante_escolhido = randrange(qtd_participantes);
print(f"O participante sorteado foi o de número {participante_escolhido}\n");

# 7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

print("***** Gerador de Token *****");
nome_user = input("Digite seu nome: ");
token = randrange(1000, 9999);
print(f"Olá, {nome_user}, o seu token de acesso é {token}! Seja bem-vindo(a)!");

# 8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

print("***** Salada de frutas*****");
frutas = ["maçã", "banana", "uva", "pêra", "manga", "coco", "melancia", "mamão",    "laranja", "abacaxi", "kiwi", "ameixa"];
frutas_escolhidas = choices(frutas, k=3);
print(f"As frutas escolhidas foram {frutas_escolhidas[0]}, {frutas_escolhidas[1]}, {frutas_escolhidas[2]}")