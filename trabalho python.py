def cadastrar_tarefa(lista_tarefas):
    # Solicita a descrição e a data de vencimento da tarefa
    descricao = input("Digite a descrição da tarefa: ")
    data_vencimento = input("Digite a data de vencimento (formato DD/MM/AAAA): ")

    # Solicita o nome do usuário que está cadastrando a tarefa
    nome_usuario = input("Digite o nome do usuário que está cadastrando a tarefa: ")

    # Cria um dicionário para representar a nova tarefa
    nova_tarefa = {"descricao": descricao, "data_vencimento": data_vencimento, "usuario": nome_usuario}
    # Adiciona a tarefa à lista de tarefas
    lista_tarefas.append(nova_tarefa)
    print("Tarefa cadastrada com sucesso!")

def listar_tarefas(lista_tarefas):
    print("\n=== Lista de Tarefas ===")
    for i, tarefa in enumerate(lista_tarefas, start=1):
        # Acessa os valores diretamente do dicionário
        print(f"{i}. Descrição: {tarefa['descricao']}, Vencimento: {tarefa['data_vencimento']}, Nome do usuario : {tarefa['usuario']}")
        # remove a tarefa adicionada acessando o indice 
def remover_tarefa(lista_tarefas, indice):
    try:
        tarefa_removida = lista_tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    except IndexError:
        print("Índice inválido. Verifique a lista de tarefas.")

def alterar_tarefa(lista_tarefas, indice):
    if 1 <= indice <= len(lista_tarefas):
        tarefa = lista_tarefas[indice - 1]
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        nova_data_vencimento = input("Digite a nova data de vencimento (formato DD/MM/AAAA): ")
        tarefa['descricao'] = nova_descricao
        tarefa['data_vencimento'] = nova_data_vencimento
        print(f"Tarefa alterada com sucesso!")
    else:
        print("Índice inválido. Verifique a lista de tarefas.")

def main():
    lista_tarefas = []  # Armazena as tarefas cadastradas

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar uma tarefa")
        print("2. Listar tarefas")
        print("3. Alterar uma tarefa")
        print("4. Remover tarefa")
        print("5. Sair do sistema")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_tarefa(lista_tarefas)
        elif escolha == "2":
            listar_tarefas(lista_tarefas)
        elif escolha == "3":
            indice = int(input("Digite o índice da tarefa que deseja alterar: "))
            alterar_tarefa(lista_tarefas, indice)
        elif escolha == "4":
            indice = int(input("Digite o índice da tarefa que deseja remover: "))
            remover_tarefa(lista_tarefas, indice)
        elif escolha == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
