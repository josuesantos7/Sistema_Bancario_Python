print("\n===================================================")
print(" JS Unibank - Sistema de Gerenciamento Bancário")
print("===================================================")
print("Seja bem-vindo(a) ao JS Unibank!")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        print("Saque")
    
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")