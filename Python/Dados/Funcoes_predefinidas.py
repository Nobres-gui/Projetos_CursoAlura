notas = {
    '1º Trimestre': 9.5,
    '2º Trimestre': 8.5,
    '3º Trimestre': 7,
    
    };

# 1. MODO DE SOMAR OS VALORES
# soma = 0;
# for nota in notas.values():
#     soma += nota;

soma = sum(notas.values());

# 2. VER QTD DE VALORES DENTRO DA LISTA/DICIONARIO
qtd_notas = len(notas);

# 3. EDITAR A QTD DE CARACTERES DEPOIS DA VIRGULA
media = round(soma / qtd_notas, 1);
