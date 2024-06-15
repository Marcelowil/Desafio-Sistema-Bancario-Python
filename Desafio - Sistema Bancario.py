from abc import ABC, abstractmethod, abstractproperty
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
    @abstractproperty
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

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)
