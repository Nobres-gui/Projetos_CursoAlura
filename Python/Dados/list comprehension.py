notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]];

def media(lista: list=[0]) -> float :
    calculo = sum(lista) / len(lista);
    # return calculo: float (-> float)
    return calculo;

medias =  [ round(media(nota), 1) for nota in notas];
nomes = [('João', 'J610'), ('Maria', 'M281'), ('José', 'J381'), ('Cláudia', 'C146'), ('Ana', 'A75')];

# LIST COMPREHENSION COM IF
nomes = [nome[0] for nome in nomes];

# Zip junta duas ou mais lista e a transforma em uma tupla | List pega o que os elementos passados a ela e transforma numa lista
estudantes = list(zip(nomes, medias));

candidatos = [estudantes[0] for estudante in estudantes if estudante[1] > 8.0];

# LIST COMPREHENSION COM IF ELSE
situacao = ["Aprovado(a)" if media >= 6 else "Reprovado(a)" for media in medias];
lista_completa = [nomes, notas, medias, situacao];

# Nesse exemplo a função zip é usada de forma inversa pegando uma lista de tuplas e a dividindo em duas listas distintas
# tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
# ids, nomes  = zip(*tupla_iteravel)

# ids = list(ids)
# nomes = list(nomes)

# print("IDs = ", ids)
# print("Nomes = ", nomes)

# DICT COMPREHENSION
coluna = ["Notas", "Médias", "Situação"];

cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))};

# cadastro["Estudante"] =[lista_completa[0][i] for i in range(len(lista_completa[0]))];
cadastro["Estudante"] =[nomes[0] for nome in nomes];

print(cadastro);
