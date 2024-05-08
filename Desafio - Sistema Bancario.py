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
            extrato = extrato + f"Depósito: R$ {deposito:.2f} \n" 
            print(f"Depósito de R$ {deposito:.2f} realizado.")

        else:
            print("Valor inválido, digite um valor positivo.")
    
    elif opcao == 2:
        saque = float(input("Digite o valor a ser sacado: "))

        if saldo >= saque:
            if saque <= limite and LIMITE_SAQUES > numero_saques:
                saldo -= saque
                numero_saques += 1
                extrato = extrato + f"Saque: R$ {saque:.2f} \n"
                print(f"Saque de R$ {saque:.2f} realizado.")

            else:
                print("Limite de saque acima ou numero de saques diários excedidos")

        else:
            print("Saldo insuficiente!")

    elif opcao == 3:
        print("Extrato".center(21,"="))
        if extrato != "":
            print(extrato)

        print(f"Saldo da conta: R$ {saldo: .2f}")
        print("".center(21,"="))

    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")