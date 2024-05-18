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

def exibir_extrato(saldo, /, extrato):
    print("Extrato".center(21,"="))
    if extrato != "":
        print(extrato)

        print(f"Saldo atual da conta: R$ {saldo: .2f}")
    print("".center(21,"="))

def cadastrar_usuario(lista):
    cpf = int(input("Digite seu CPF (somente os numeros): "))
    cadastro_existente = filtrar_usuarios(cpf, lista)

    if cadastro_existente:
        nome = input("Informe o nome completo: ")
        data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        lista_usuarios = {cpf: {"nome":nome, "data_nascimento":data_nasc, "endereco": endereco}}

        return lista_usuarios
    
    return

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Digite seu CPF (somente os numeros): "))
    cadastro_existente = selecionar_usuario(cpf, usuarios)

    if cadastro_existente != None:
        conta = {numero_conta:{"agencia":agencia, "usuario":cadastro_existente}}

        return conta
    
    return

def selecionar_usuario(cpf, lista):
    for cadastro in lista:
        if cpf in cadastro:
            return cadastro

def filtrar_usuarios(cpf, lista):
    for cadastro in lista:
        if cpf in cadastro:
            return False
    return True

def lista_usuarios(cpf, usuario):
    exibir_usuarios = f'''
    Nome: {usuario[cpf]["nome"]}
    CPF: {cpf}
    Data de Nascimento: {usuario[cpf]["data_nascimento"]}
    Endereço: {usuario[cpf]["endereco"]}'''
    print(exibir_usuarios)

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuario
[5] Criar Conta
[6] Listar Usuarios
[7] Lista Contas

[0] Sair

=> """

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

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
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            novo_usuario = cadastrar_usuario(usuarios)

            if novo_usuario != None:
                usuarios.append(novo_usuario)
                print(f"Cadastro efetuado: {novo_usuario}")

            else:
                print("CPF já cadastrado")
        
        elif opcao == 5:
            nova_conta = criar_conta(AGENCIA, len(contas)+1, usuarios)

            if nova_conta != None:
                contas.append(nova_conta)
                print(f"Conta criada: {nova_conta}")

            else:
                print("Usuário inexistente, crie um novo usuário.")

        elif opcao == 6:
            for usuario in usuarios:
                for chave in usuario:
                    lista_usuarios(chave, usuario)

        elif opcao == 7:
            for conta in contas:
                print(contas)

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()