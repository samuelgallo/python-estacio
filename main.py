class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def imprimir(self):
        print(self.nome, " tem ", self.idade, " anos")
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade

# p = Pessoa("Ana", 25)
# p.imprimir()

"""
class Profissional (Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print("\t e trabalha como ", self.profissao)

p = Profissional("Ana", 25, "balconista")
p.imprimir()
"""

# class Conta:
#     def __init__(self, numero, cpf, nomeTitular, saldo):
#         self.numero = numero
#         self.cpf = cpf
#         self.nomeTitular = nomeTitular
#         self.saldo = saldo

# class Pessoa:
#     _contador = 0
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         Pessoa._contador += 1
#     def imprimir(self):
#         print(self.nome, " tem ", self.idade, " anos")

#     @property
#     def contador(self):
#         return type(self)._contador

# p1 = Pessoa("Carlos", 18)
# print(p1.contador)
# print(Pessoa._contador)

# class Argentina():
#     def capital(self):
#         print("Buenos aires é a capital da Argentina")
#     def lingua_oficial(self):
#         print("O espanol é a lingua oficial da Argentina")

# class Brasil():
#     def capital(self):
#         print("A capital do Brasil e Brasilia")
#     def lingua_oficial(self):
#         print("O português é a lingua oficial do Brasil")

# obj_arg = Argentina()
# obj_bra = Brasil()

# for pais in (obj_arg, obj_bra):
#     pais.capital()
#     pais.lingua_oficial()
#     print("\n")

class Veiculo:
    def rodar(self):
        print("Reduz o consumo de combustível")

class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veiculo utiliza eletricidade")

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()
