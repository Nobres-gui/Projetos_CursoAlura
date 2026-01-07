notas = [8.5 , 9.0, 6.0, 10.0];


def boletim(notas):
    media = sum(notas)/len(notas);
    if(media < 6):
        situacao = "Reprovado";
    else:
        situacao = "Aprovado";
    return media, situacao;
        
        

media, situacao = boletim(notas);
print(f"O aluno ficou com a média de {media} e está {situacao.upper()}!!!!!!");
