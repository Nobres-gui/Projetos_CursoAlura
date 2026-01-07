notas = [6, 7, 8, 9];

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista);
    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas");
    
    return calculo;

try:
    resultado = media(notas);
except TypeError:
    print("Não foi possivel calcular a média do estudante");
except ValueError as e:
    print(e);
else:
    print(resultado);
finally:
    print("A consulta foi encerrada");
    