# Python
## _Tipos de associação entre objetos_

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png)](https://nodesource.com/products/nsolid)



## Agregação
Para atender a novas necessidades do sistema de conta corrente do banco, agora é necessário adicionar uma funcionalidade para o gerenciamento de conta conjunta, ou seja, uma conta corrente pode ter um conjunto de clientes associados. Isso pode ser representado como uma agregação, conforme aponta o esquema a seguir. Uma observação: o losango na imagem tem a semântica da agregação.

![](https://stecine.azureedge.net/repositorio/00212ti/00232/img/imagem-013.jpg)


```python
class Cliente
    def__init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
```

Classe cliente.py.

```python
class Conta:
   def__init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
   def depositar(self, valor):
      self.saldo += valor
   def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         return True
   def transfereValor(self,contaDestino,valor):
      if self.saldo < valor:
         return ("Não existe saldo suficiente")
      else:
         contadestino.depositar(valor)
         self.saldo -= valor
         return("Transferencia Realizada")
   def gerarsaldo(self):
      print(f"numero:{self.numero\n saldo: {self.saldo}")
```

Classe contas.py 
##

Um programa testecontas.py deve ser criado para ser usado na instanciação dos objetos das duas classes e gerar as transações realizadas nas contas dos clientes.


```python
from conta import Conta
from cliente import Cliente
cliente1 = Cliente(123, “Joao”, “Rua 1”)
cliente2 = Cliente(345, “Maria”,”Rua 2”)
conta1 = Conta([cliente1,cliente2], 1,0) 
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
```
###Atenção!
- Na linha número 5, é instanciado um objeto conta1 com dois clientes agregados: cliente1 e cliente2. Esses dois objetos são passados como parâmetros.

- Qual é o resultado dessa execução? Qual será o valor final na conta?

- Sugestão: altere o programa do código anterior a fim de criar mais uma conta para dois clientes diferentes. Como desafio, tente, por meio do objeto conta, imprimir o nome e o endereço dos clientes associados às contas.


##Composição
A classe Conta ainda não está completa de acordo com as necessidades do sistema de conta corrente do banco. Isso ocorre porque o banco precisa gerar extratos contendo o histórico de todas as operações realizadas para conta corrente.

Para isso, o sistema precisa ser atualizado para adicionar uma composição de cada conta com o histórico de operações realizadas. O diagrama a seguir representa a composição entre as classes Conta e Extrato. Essa composição representa que uma conta pode ser composta por vários extratos.

Uma observação: o losango preenchido tem a semântica da composição.


![](https://stecine.azureedge.net/repositorio/00212ti/00232/img/imagem-014.jpg)
######Classe Conta composta de 1 ou mais extratos.

A classe Extrato tem as responsabilidades de armazenar todas as transações realizadas na conta e de conseguir imprimir um extrato com a lista dessas transações.

```python
class Extrato:
    def __init__(self):
        self.transacoes = []
    def extrato(self,numeroConta):
            print(f"Extrato da conta {numeroConta}\n")
            for p in self.transacoes:
                print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")
        
        
```

A classe Conta possui todas as transações, como sacar, depositar e transferir_valor. Cada transação realizada deve adicionar uma linha ao extrato da conta.

A composição Conta->Extrato inclusive precisa ser inicializada no construtor da classe Conta, conforme exemplificava a figura anterior. No construtor de Extrato, foi adicionado um atributo transações, o qual foi inicializado para receber um array de valores – transações da conta.

A classe Conta alterada deve ficar da seguinte maneira:

```python
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
        
```


- Adição da linha nº 10 – criação de um atributo extrato, fazendo referência a um objeto Extrato.
- Adição das linhas nºs 14, 21 e 30– adição de linhas ao array de transações do objeto Extrato por meio do atributo extrato.

###Execução no terminal:

```python
from cliente import Cliente
from conta import Conta
from extrato import Extrato
cliente1 = Cliente("123","Joao","Rua X")
cliente2 = Cliente ("456","Maria","Rua W")
conta1 = Conta([cliente1,cliente2],1,2000)
conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)
Extrato : 1
DEPÓSITO 1000.00 Data 13/mar/2024
SAQUE 1500.00 Data13/mar/2024
