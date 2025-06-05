class Pessoa:  #criando a classe pessoa para atuilizar como 'molde'
    def __init__(self, nome, idade, endereco, cpf, sexo): #construtores das variaveis a serem adicionadas
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo

    def apresentar(self): #função de apresentar a pessoa
        print(f"\nOlá! Meu nome é {self.nome} e tenho {self.idade} anos.")

    def mostrar_endereco(self):
        print(f"\nO {self.nome} mora em {self.endereco}")

    def mostrar_informacoes(self):
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nSexo: {self.sexo}")


def menu_principal():
    print("\nMenu Principal:")
    print("1 - Adicionar nova pessoa")
    print("2 - Listar pessoas ja cadastradas")
    print("3 - Interação com pessoa")
    print("4 - Sair do programa")


def menu_pessoa():
    print("\nEscolha uma ação:")
    print("1 - Apresentar")
    print("2 - Mostrar endereço")
    print("3 - Mostrar todos os dados")
    print("4 - Voltar ao menu principal")


# Lista para armazenar várias pessoas que forem cadastadas
pessoas = []

while True: #um loop para sempre estar o menu interativo
    menu_principal() # ta chamando o menu_principal pra dentro do loop
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        endereco = input("Endereço: ")
        cpf = input("CPF: ")
        sexo = input("Sexo: ")
        nova_pessoa = Pessoa(nome, idade, endereco, cpf, sexo)
        pessoas.append(nova_pessoa)
        print(f"\nPessoa {nome} adicionada com sucesso!")

    elif opcao == "2":
        if not pessoas:
            print("\nNenhuma pessoa cadastrada.")
        else:
            print("\nPessoas cadastradas:")
            for i, p in enumerate(pessoas): #um pequeno loop para mostrar tds as pessoas
                print(f"{i + 1} - {p.nome}")

        escolha = int(input("Número da pessoa: ")) - 1
    elif opcao=='3':
        if 0 <= escolha < len(pessoas):
            pessoa = pessoas[escolha]
            while True: # outro loop de menu
                menu_pessoa()  # ta chamando o menu_pessoa para dentro do loop
                acao = input("Ação: ")
                if acao == "1":
                    pessoa.apresentar()
                elif acao == "2":
                    pessoa.mostrar_endereco()
                elif acao == "3":
                    pessoa.mostrar_informacoes()
                elif acao == "4":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        print("\nEncerrando o programa. Até mais!")
        break # encerrado o loop de menu

    else:
        print("Opção inválida. Tente novamente.") # poderia mudar para um try ou except se quiser