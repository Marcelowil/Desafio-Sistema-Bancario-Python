menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor a ser depositado: "))
        
        if deposito > 0:
            saldo += deposito

        else:
            print("Valor inválido, digite um valor positivo.")
    
    elif opcao == 2:
        print("Saque")

    elif opcao == 3:
        print("Extrato")
        print(saldo)

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")