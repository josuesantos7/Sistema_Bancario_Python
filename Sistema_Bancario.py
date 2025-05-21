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
        print("Depósito")

    elif opcao == "s":
        print("Saque")
    
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")