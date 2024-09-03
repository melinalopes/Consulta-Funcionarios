# Mensagem de boas-vindas com o nome completo
print("Bem vindos a empresa da Melina Rafaela Lopes")  

# Lista de funcionários e identificador global inicializado com o meu RU
lista_funcionarios = []
id_global = 4687800

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(id):
    print(f"Id do Funcionário: {id}")
    nome = input("Por favor, digite o nome do Funcionário: ")
    setor = input("Por favor, digite o setor do Funcionário: ")
    salario = float(input("Por favor, entre com o salário do Funcionário: "))
    
    # Criando um dicionário com os dados do funcionário
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    # Adicionando o dicionário à lista de funcionários
    lista_funcionarios.append(funcionario.copy())

# Função para consultar funcionários com diferentes opções
def consultar_funcionarios():
    while True:
        # Menu de opções de consulta
        print("Opções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            # Consulta todos os funcionários cadastrados
            if not lista_funcionarios:
                print("Não há funcionários cadastrados!")
            else:
                for funcionario in lista_funcionarios:
                    print(funcionario)
        
        elif opcao == '2':
            # Consulta por id específico
            id_consulta = int(input("Digite o id do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == '3':
            # Consulta por setor específico
            setor_consulta = input("Digite o setor desejado: ")
            encontrados = [funcionario for funcionario in lista_funcionarios if funcionario['setor'] == setor_consulta]
            if not encontrados:
                print("Nenhum funcionário encontrado neste setor.")
            else:
                for funcionario in encontrados:
                    print(funcionario)
        
        elif opcao == '4':
            # Retorna ao menu principal
            return
        
        else:
            print("Opção inválida")

# Função para remover um funcionário da lista
def remover_funcionario():
    id_remover = int(input("Digite o id do funcionário a ser removido: "))
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remover:
            lista_funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso.")
            return
    print("Id inválido.")

# Menu principal do programa
while True:
    print("------MENU PRINCIPAL------")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    
    opcao_menu = input("Escolha uma opção: ")
    
    if opcao_menu == '1':
        print("------MENU CADASTRO DE FUNCIONÁRIO------")
        # Incrementa o id global e cadastra um novo funcionário
        id_global += 1
        cadastrar_funcionario(id_global)
    
    elif opcao_menu == '2':
        print("------MENU CONSULTAR FUNCIONÁRIO------")
        # Chama a função para consultar funcionários
        consultar_funcionarios()
    
    elif opcao_menu == '3':
        print("------MENU REMOVER FUNCIONÁRIO------")
        # Chama a função para remover um funcionário
        remover_funcionario()
    
    elif opcao_menu == '4':
        # Encerra o programa
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida!")
