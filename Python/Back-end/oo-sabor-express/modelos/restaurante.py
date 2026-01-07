from modelos.avaliacao import Avaliacao;
from modelos.cardapio.item_cardapio import ItemCardapio;

class Restaurante:
    restaurantes = [];
    
    def __init__(self, nome, categoria):
        self._nome = nome.title();
        self._categoria = categoria.upper();
        # com o _ ele vira um atributo privado, assim o usuario nao pode colocar um valor nele, apenas o programa pode
        self._ativo = False
        self._avaliacao = [];
        self._cardapio = [];
        Restaurante.restaurantes.append(self);
    
    #pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto, mostraremos determinada informação
    def __str__(self):
        return f"{self._nome} | {self._categoria}";
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | {"AVALIAÇÕES".ljust(25)} | {"STATUS"}");
        
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}");
            
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐';
    
    def alternar_estado(self):
        self._ativo = not self._ativo;
        
    def receber_avaliacao(self, cliente, nota):
        if nota > 5:
            nota = 5;
        elif nota < 0:
            nota = 0;
        else:
            avaliacao = Avaliacao(cliente, nota);
            self._avaliacao.append(avaliacao);
    
    @property  
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-";
        soma_notas = sum( avaliacao._nota for avaliacao in self._avaliacao);
        qtd_notas = len(self._avaliacao);
        media = round(soma_notas / qtd_notas, 1);
        return media

    def adicionar_cardapio(self, item):
        #A isinstance()função retorna Truese o objeto especificado for do tipo especificado, caso contrário False
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item);
    
    @property    
    def exibir_cardapio(self):
        print(f"Cardápio do restaurante {self._nome}\n");
        for i,item in enumerate(self._cardapio, start=1):
            #hasattr(objeto, atributo) pergunta se tal objeto tem determidado produto
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}";
                print(mensagem_prato);
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}";
                print(mensagem_bebida);
                

# vars mostra as informacoes salvas na variavel e nao onde ela esta armazanada na memoria
# print(vars(restaurante_praca));
# print(vars(restaurante_pizza));

# dirs mostra as informacoes salvas na variavel e tambem as funcoes padroes atribuidas
# print(dir(restaurante_praca))