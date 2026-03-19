elementos= ["Elemento 1\n", "Elemento 2\n", "Elemento 3\n"]

def escrever_arquivo(elementos):
    with open("Arquivo criado com python.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(elementos);
        
escrever_arquivo(elementos);

def ler_arquivo():
    with open("Arquivo criado com python.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read();
        print(conteudo);
        
ler_arquivo();