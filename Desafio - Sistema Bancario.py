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
        saque = float(input("Digite o valor a ser sacado: "))

        if saldo >= saque:
            if saque <= limite and LIMITE_SAQUES > numero_saques:
                saldo -= saque
                numero_saques += 1

            else:
                print("Limite de saque acima ou numero de saques diários execidos")

        else:
            print("Saldo insuficiente!")

    elif opcao == 3:
        print("Extrato")
        print(saldo)
        print(numero_saques) # Teste

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")