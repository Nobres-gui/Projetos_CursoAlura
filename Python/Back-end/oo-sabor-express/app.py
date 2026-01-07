from modelos.restaurante import Restaurante;
from modelos.cardapio.bebida import Bebida;
from modelos.cardapio.prato import Prato;

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana');
restaurante_mexicano.alternar_estado();
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande');
bebida_suco.aplicar_desconto();
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade');
prato_paozinho.aplicar_desconto();
restaurante_mexicano.adicionar_cardapio(bebida_suco);
restaurante_mexicano.adicionar_cardapio(prato_paozinho);



def main():
    restaurante_mexicano.exibir_cardapio;

if __name__ == '__main__':
    main();