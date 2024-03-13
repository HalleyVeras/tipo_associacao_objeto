

from conta import Conta
from cliente import Cliente
from extrato import Extrato
from banco import Banco

# Criando clientes
cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

# Criando contas
conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 3000)

# Criando Banco
banco = Banco()
banco.inserirCliente(cliente1)
banco.inserirCliente(cliente2)
banco.inserirConta(conta1)
banco.inserirConta(conta2)
conta1.depositar(1000)
conta1.sacar(1500)
conta1.transfereValor(conta2, 500)
conta1.extrato.extrato(conta1.numero)