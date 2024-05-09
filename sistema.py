print("""
==========================================
        Bem-vindo ao nosso Banco""")
menu = """==========================================

[1] - Cadastrar Cliente
[2] - Cadastrar Conta
[3] - Depositar
[4] - Sacar
[5] - Exibir Extrato
[6] - Exibir Clientes
[7] - Sair

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
EXIBIR_CLIENTES = "6"
SAIR = "7"

def cadastrar_cliente(cpf, nome, data_nascimento, endereco):
    novo_cliente = {}
    novo_cliente["cpf"] = cpf
    novo_cliente["nome"] = nome
    novo_cliente["data_nascimento"] = data_nascimento
    novo_cliente["endereco"] = endereco

    return novo_cliente

def exibir_clientes():
    print(clientes)


def cadastrar_conta(conta, cpf, deposito_inicial):
    nova_conta = {"agencia": "0001"}
    nova_conta["conta"] = conta
    nova_conta["cpf"] = cpf
    nova_conta["saldo"] = deposito_inicial
    nova_conta["limite_saques"] = 3
    nova_conta["limite_diario_saque"] = 500 

    return nova_conta


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

    



while True:

    opcao = input(menu).lower()
    if opcao == CADASTRAR_CLIENTE:
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento: ")
        endereco = input("Digite o endereço do cliente: ")
        clientes.append(cadastrar_cliente(cpf, nome, data_nascimento, endereco))
        print("Cliente cadastrado com sucesso!")
        input("Pressione qualquer tecla para continuar...")
    if opcao == DEPOSITAR:
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
        

    elif opcao == EXIBIR_CLIENTES:
        exibir_clientes()
    
    elif opcao == SAIR:
        break

    else:
        print("Opcao inválida!")
        continue

print("Obrigada por utilizar nosso sistema bancário!")

