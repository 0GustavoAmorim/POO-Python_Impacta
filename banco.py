class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    # Método acessor
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor <= 0:
            return 'Você deve depositar um valor positivo'
        self.__saldo += valor
        return f'Deposito com o valor de {valor} realizado com sucesso'

    def sacar(self, valor):
        if valor <= 0:
            return 'Valor para saque deve ser positivo'
        if valor > self.__saldo:
            return f'Saldo insuficiente, seu saldo é de {self.__saldo}'
        
        self.__saldo -= valor
        return f'Saque realizado com sucesso, o seu saldo atual é de {self.__saldo}'


if __name__ == '__main__':
    c1 = Conta(1, 'Gustavo')
