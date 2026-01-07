from abc import ABC, abstractmethod;

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome;
        self._preco = preco;
        
    #obriga a todas as outras classes a terem essa função    
    @abstractmethod
    def aplicar_desconto():
        pass;