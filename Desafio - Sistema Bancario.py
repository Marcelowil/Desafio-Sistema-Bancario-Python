from abc import ABC, abstractmethod
from datetime import datetime

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
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._AGENCIA = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def limite(self):
        return self._LIMITE
    
    @property
    def agencia(self):
        return self._AGENCIA
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def sacar(self, valor):
        if self.saldo < valor:
            print("Operação falhou! Saldo insuficiente")
            
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizando com sucesso !")
            return True
        else:
            print("Operação falhou! O valor informado é inválido")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico._transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        
        else:
            return super().sacar(valor)

        return False
    
class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })



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