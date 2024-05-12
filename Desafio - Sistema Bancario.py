def sacar(*,saldo, valor, limite, numero_saques, limite_saques):
    extrato = ""

    if saldo >= valor:
            if valor <= limite and limite_saques > numero_saques:
                saldo -= valor
                numero_saques += 1
                extrato = f"Saque: R$ {valor:.2f} \n"
                print(f"Saque de R$ {valor:.2f} realizado.")
                
            else:
                print("Limite de saque acima ou numero de saques diários excedidos")

    else:
        print("Saldo insuficiente!")

    
    return saldo, extrato, numero_saques

def deposito(saldo, valor):
    extrato = ""
    
    if valor > 0:
        saldo += valor
        extrato = f"Depósito: R$ {valor:.2f} \n" 
        print(f"Depósito de R$ {valor:.2f} realizado.")

    else:
        print("Valor de depósito inválido, digite um valor positivo.")

    
    return saldo, extrato
    

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = int(input(menu))

        if opcao == 1:
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            saldo_atualizado_dep, extrato_atualizado_dep = deposito(saldo, valor_depositado)

            saldo = saldo_atualizado_dep
            extrato = extrato + extrato_atualizado_dep
            
        
        elif opcao == 2:
            saque = float(input("Digite o valor a ser sacado: "))

            saldo_atualizado, extrato_atualizado, numero_saques_atualizado = sacar(saldo=saldo, valor=saque, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)

            saldo = saldo_atualizado
            extrato = extrato + extrato_atualizado
            numero_saques = numero_saques_atualizado
            

        elif opcao == 3:
            print("Extrato".center(21,"="))
            if extrato != "":
                print(extrato)

            print(f"Saldo atual da conta: R$ {saldo: .2f}")
            print("".center(21,"="))

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()