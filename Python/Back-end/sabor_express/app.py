import os;

restaurantes = [{"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": False}, 
                {"nome":"Sushi Dushi", "categoria": "Japonesa", "ativo": True}];

def exibir_nome_Programa():
    """ Exibe o nome estilizado do programa na tela """
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """);

def exibir_opcoes():
    """Exibe as opções disponíveis no menu principal"""
    print('1. Cadastrar restaurante');
    print('2. Listar restaurantes');
    print('3. Alternar estado restaurante');
    print('4. Sair\n');

def finalizar_app():
    """Exibe mensagem de finalização do aplicativo"""
    exibir_subtitulo("App finalizado");

def voltar_menu_principal():
    """ Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """    

    input("\nDigite uma tecla para voltar ao menu inicial: ");
    main();

def opcao_invailda():
    """Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """
    print("opção inválida\n");
    input("digite uma tecla para voltar ao menu principal: ");
    main();

def exibir_subtitulo(texto):
    """Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    """
    os.system('cls');
    linha = "*" * (len(texto)); 
    print(linha);
    print(texto);
    print(linha);
    print();

def cadastrar_restaurante():
    """ Essa função é reponsavel por cadastrar um novo restaurante
    
    Inputs:
    -Nome restaurante
    -Categoria restaurante
    
    Output:
    -Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes");
    nome_restaurante = input("Digite o nome do restaurante para cadastro: ");
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ");
    dados_restaurante = [{"nome": nome_restaurante, "categoria": categoria_restaurante, "ativo": False}]
    restaurantes.append(dados_restaurante);
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso");
    voltar_menu_principal();

def listar_restaurantes():
    """Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela"""
    
    exibir_subtitulo("Restaurantes cadastrados: ");
    print(f"{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"];
        categoria_restaurante = restaurante["categoria"];
        restaurante_ativo = "Ativado" if restaurante["ativo"] else "Desativado";
        print(f"{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {restaurante_ativo}");
    voltar_menu_principal();   

def alternar_estado_restaurante():
    """Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação"""
    
    exibir_subtitulo("Alterar o estado do restaurante");
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ");
    restaurante_encontrado = False;
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True;
            restaurante["ativo"] = not restaurante["ativo"];
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso";
            print(mensagem);
    if not restaurante_encontrado:
        print("O restaurante não foi encotrado");
    voltar_menu_principal();

def escolher_opcoes():
    """Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário"""
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "));

        if opcao_escolhida == 1:
            cadastrar_restaurante();
        elif opcao_escolhida == 2:
            listar_restaurantes();
        elif opcao_escolhida == 3:
            alternar_estado_restaurante();
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            opcao_invailda();
    except:
        opcao_invailda();

def main():
    """Função principal que inicia o programa"""
    
    os.system("cls");
    exibir_nome_Programa();
    exibir_opcoes();
    escolher_opcoes();

if __name__ == "__main__":
    main();