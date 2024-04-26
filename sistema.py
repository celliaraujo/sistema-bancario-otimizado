print("""
-----------------------------------------
        Bem-vindo ao nosso Banco""")
menu = """-----------------------------------------

[d] - Depositar
[s] - Sacar
[e] - Exibir Extrato
[f] - Sair

-----------------------------------------
Escolha a opção desejada: """

saldo = 0
valor_limite = 500
extrato = """"""
numero_saques = 0
LIMITE_SAQUES = 3
DEPOSITAR = "d"
SACAR = "s"
EXIBIR_EXTRATO = "e"
SAIR = "f"


while True:

    opcao = input(menu).lower()

    if opcao == DEPOSITAR:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")        
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
           print("Valor do depósito deve ser maior que zero.") 

        print()
        input("Pressione qualquer tecla para continuar...")

    elif opcao == SACAR:

        valor = float(input("Informe o valor do saque: R$ "))

        saldo_insuficiente = valor > saldo
        valor_limite_excedido = valor > valor_limite
        mais_de_tres_saques = numero_saques >= LIMITE_SAQUES

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

            extrato += f"Saque de R$ {valor:.2f}\n"

        print()
        input("Pressione qualquer tecla para continuar...")

    elif opcao == EXIBIR_EXTRATO:
        print("""----------------------------
       Extrato do Dia
----------------------------""")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print()
        print(f"Saldo atual da conta: R$ {saldo:.2f}")
        print("----------------------------")
        input("Pressione qualquer tecla para continuar...")
    
    elif opcao == SAIR:
        break

    else:
        print("Opcao inválida!")
        continue

print("Obrigada por utilizar nosso sistema bancário!")

