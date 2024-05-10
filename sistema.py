print("""
==========================================
        Bem-vindo ao nosso Banco""")
menu = """==========================================

[1] - Cadastrar Cliente
[2] - Cadastrar Conta
[3] - Depositar
[4] - Sacar
[5] - Exibir Extrato
[6] - Listar Clientes
[7] - Listar Contas
[0] - Sair

==========================================
Escolha a opção desejada: """

saldo = 0
valor_limite = 500
extrato = """"""
numero_saques = 0

clientes = []
contas = []

LIMITE_SAQUES = 3
CADASTRAR_CLIENTE = "1"
CADASTRAR_CONTA = "2"
DEPOSITAR = "3"
SACAR = "4"
EXIBIR_EXTRATO = "5"
LISTAR_CLIENTES = "6"
LISTAR_CONTAS = "7"
SAIR = "0"

def cadastrar_cliente(clientes):   
    cpf = False
    novo_cliente = {}
    novo_cliente["cpf"] = input("Digite o CPF do cliente (somente números): ")

    for cliente in clientes:
        if cliente["cpf"] == novo_cliente["cpf"]:
            cpf = True
        else:
            cpf = False

    if cpf == False:
        novo_cliente["nome"] = input("Digite o nome completo: ")
        novo_cliente["data_nascimento"] = input("Digite a data de nascimento (dd/mm/aaaa): ")
        novo_cliente["endereco"] = input("Digite o endereço do cliente (logradouro, nº - bairro - cidade/sigla estado): ")
        clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!")
    else:
        print("\nCPF já consta no sistema")

    print()        
    input("Pressione qualquer tecla para continuar...")

    

def listar_clientes(clientes):

    print("CLIENTES DO BANCO".center(100))
    print("----------------------------------------------------------------------------------------------------")

    for cliente in clientes:
        print(f"{cliente['cpf']}\t{cliente['nome']}\t{cliente['data_nascimento']}\t{cliente['endereco']}\t")
        
    print("----------------------------------------------------------------------------------------------------")

    print()        
    input("Pressione qualquer tecla para continuar...")


def cadastrar_conta(contas, clientes):
    nova_conta = {}
    nova_conta["cpf"] = input("Insira o CPF para o qual deseja criar a conta: ")

    for cliente in clientes:
        if cliente["cpf"] == nova_conta["cpf"]:
            cliente_existe = True
            break
    else:
        cliente_existe = False

    if not cliente_existe:
        print("\nO CPF não foi encontrado no banco de dados.")
    else:
        nova_conta["agencia"] = "0001"
        nova_conta["conta"] = len(contas) + 1
        contas.append(nova_conta)
        print ("Nova conta cadastrada com sucesso!")

    print()        
    input("Pressione qualquer tecla para continuar...")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falou! Valor informado inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    saldo_insuficiente = valor > saldo
    valor_limite_excedido = valor > limite
    mais_de_tres_saques = numero_saques >= limite_saques

    if saldo_insuficiente:
            print("Não foi possível realizar o saque, saldo insuficiente.")

    elif valor_limite_excedido:
        print(f"Valor ultrapassa o limite de R$ {valor_limite:.2f} permitido por saque.")

    elif mais_de_tres_saques:
        print("Você já realizou os três saques permitidos do dia.")

    elif valor <= 0:
        print("Valor do saque deve ser maior que zero.")

    else:
        
        saldo -= valor
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        extrato += f"Saque:\tR$ {valor:.2f}\n"
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("""==================================
       Extrato do Dia
==================================""")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print()
    print(f"Saldo atual da conta: R$ {saldo:.2f}")
    print("==================================")
    input("Pressione qualquer tecla para continuar...")

    return extrato

def listar_contas(contas):
    print("CONTAS CADASTRADAS".center(80))
    print("--------------------------------------------------------------------------------")

    for conta in contas:
        print(f"Agência: {conta["agencia"]}\tConta: {conta["conta"]}\tCliente: {conta["cpf"]}\t".center(80))

    print("--------------------------------------------------------------------------------")
    print()
    input("Pressione qualquer tecla para continuar...")
    

cliente = {
    "cpf" : "12345678985", 
    "nome" : "André Silva Nascimento", 
    "data_nascimento" : "25/01/1985", 
    "endereco" : "Rua São Vicente, 65 - Cruz - Rio de Janeiro/RJ"}
clientes.append(cliente)
cliente = {
    "cpf" : "25874196356", 
    "nome" : "Carolina de Jesus", 
    "data_nascimento" : "10/05/1991", 
    "endereco" : "Rua Clarinete, 05 - Moema - Rio de Janeiro/RJ"}
clientes.append(cliente)
cliente = {
    "cpf" : "98745632152", 
    "nome" : "Isidoro José Cavalcante", 
    "data_nascimento" : "30/04/1998", 
    "endereco" : "Rua Joelma Nunes, 83 - Vila Roma - Rio de Janeiro/RJ"}
clientes.append(cliente)

while True:

    opcao = input(menu).lower()
    if opcao == CADASTRAR_CLIENTE:

        cadastrar_cliente(clientes)

    elif opcao == CADASTRAR_CONTA:

        cadastrar_conta(contas, clientes)        

    elif opcao == DEPOSITAR:
        valor = float(input("Informe o valor do depósito: R$ "))
        
        saldo, extrato = depositar(saldo, valor, extrato) 

        print()
        input("Pressione qualquer tecla para continuar...")

    elif opcao == SACAR:

        valor = float(input("Informe o valor do saque: R$ "))

        saldo, extrato = sacar(
            saldo = saldo, 
            valor = valor, 
            extrato = extrato,
            limite = valor_limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
            )        

        print()
        input("Pressione qualquer tecla para continuar...")

    elif opcao == EXIBIR_EXTRATO:
        extrato = exibir_extrato(saldo, extrato=extrato)
        

    elif opcao == LISTAR_CLIENTES:
        listar_clientes(clientes)

    elif opcao == LISTAR_CONTAS:
        listar_contas(contas)
    
    elif opcao == SAIR:
        break

    else:
        print("Opcao inválida!")
        continue

print("Obrigada por utilizar nosso sistema bancário!")

