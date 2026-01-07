from random import randint;

def gera_codigo():
    return str(randint(0,999));

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"];
codigo_estudantes = [];

for x in range(len(estudantes)):
    codigo_estudantes.append((estudantes[x], estudantes[x][0] + gera_codigo()));
    
print(codigo_estudantes);