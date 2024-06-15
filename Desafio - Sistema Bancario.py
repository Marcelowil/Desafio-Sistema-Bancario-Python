class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self):
        pass

    def adicionar_conta(self):
        pass

class Conta:
    _saldo = 0
    _AGENCIA = "0001"
    _historico = None
    _LIMITE = 500
    _numero_saques = 3

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def novo_saldo(self, valor, operacao):
        if operacao == "saque":
            self._saldo -= valor 
        else:
            self._saldo += valor 
    
    @property
    def limite(self):
        return self._LIMITE
    
    @property
    def numero_saques(self):
        return self._numero_saques
    
    @numero_saques.setter
    def atualizando_numero_saques(self):
        self._numero_saques -= 1

    
    def nova_conta(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero

    def sacar(self, valor):
        if self.saldo >= valor and valor > 0:
            if valor <= self.limite() and self.numero_saques() > 0:
                self.novo_saldo(valor, "saque")
                self.atualizando_numero_saques()
                #extrato = f"Saque: R$ {valor:.2f} \n"     
                return True
            else:
                return False
        else:
            print("Limite de saque acima ou numero de saques diários excedidos")

    def depositar(self, valor):
        if valor > 0:
            self.saldo(valor,"depositar")
            #extrato = f"Depósito: R$ {valor:.2f} \n" 
            return True
        
        else:
            return "Valor de depósito inválido, digite um valor positivo."


def exibir_extrato(saldo, /, extrato):
    print("Extrato".center(21,"="))
    if extrato != "":
        print(extrato)

        print(f"Saldo atual da conta: R$ {saldo: .2f}")
    print("".center(21,"="))


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


def lista_contas(numero_conta, conta):
    for cpf in conta[numero_conta]["usuario"]:
       usuario = lista_usuarios(cpf, conta[numero_conta]["usuario"])

    exibir_conta = f'''
    Conta: {numero_conta:04}
    Agencia: {conta[numero_conta]["agencia"]}
    Usuario: {usuario}'''
    return exibir_conta


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuario
[5] Criar Conta
[6] Listar Usuarios
[7] Listar Contas

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
                print(f"Cadastro efetuado")

            else:
                print("CPF já cadastrado")
        
        elif opcao == 5:
            nova_conta = criar_conta(AGENCIA, len(contas)+1, usuarios)

            if nova_conta != None:
                contas.append(nova_conta)
                print(f"Conta criada")

            else:
                print("Usuário inexistente, crie um novo usuário.")

        elif opcao == 6:
            for usuario in usuarios:
                for chave in usuario:
                    print(lista_usuarios(chave, usuario))

        elif opcao == 7:
            for conta in contas:
                for chave in conta:
                    print(lista_contas(chave, conta))

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()