import datetime


class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
class Conta:
    def __init__(self,cliente,numero,saldo):
        self.cliente=cliente
        self.numero = numero
        self.saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato=Extrato()
        
    def depositar(self,valor):
        self.saldo += valor
        return self.extrato.transacoes.append([" Deposito",valor,"Data",datetime.datetime.today()])
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) 
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]) 
            self.extrato.extrato(f"PARA {contadestino.cliente.nome}") 
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")
        
        
class Extrato:
    def __init__(self):
        self.transacoes = []
    def extrato(self,numeroConta):
            print(f"Extrato da conta {numeroConta}\n")
            for p in self.transacoes:
                print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")
            

cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
conta1 = Conta([cliente1,cliente2], 1,0) 
conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)
