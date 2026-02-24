class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

pessoa1 = Pessoa("Pg", 16)
pessoa1.aniversario()
pessoa1.mensagem()
    