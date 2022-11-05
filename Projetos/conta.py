
class Account:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}.")

    def deposita(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

