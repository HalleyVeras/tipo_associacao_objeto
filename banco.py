
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
    def inserirCliente(self, cliente):
        self.clientes.append(cliente)
    def inserirConta(self, conta):
        self.contas.append(conta)