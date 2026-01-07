notas = float(input("Digite a nota do(a) estudante: "));

# MODO FUNCAO NORMAL
# def qualitativo(x):
#     return x + 0.5;

# MODO LAMBDA
qualitativo = lambda x: x + 0.5;
qualitativo(notas);

n1 = float(input("Digite a 1º nota do(a) estudante: "));
n2 = float(input("Digite a 2º nota do(a) estudante: "));
n3 = float(input("Digite a 3º nota do(a) estudante: "));

media_ponderada = lambda x, y, z: (x * 2 + y *3 + z *5) / 3;
mensagem = f"O(a) estudande atingiu a média de {round(media_ponderada(n1, n2, n3), 1)}";
print(mensagem);

# MODO LAMBDA COM FUNÇÂO MAP()

notas = [6.0, 7.0, 9.0, 5.5, 8.0];
notas_atualizadas = map(lambda x: x + 0.5, notas);
notas_atualizadas = list(notas_atualizadas);