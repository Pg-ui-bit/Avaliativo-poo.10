class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        return f"{self.nome} disse auau e tem {self.idade} idade"

cachorro1 = Cachorro("Rex", 3)
cachorro2 = Cachorro("Luna", 5)

print(cachorro1.latir())
print(cachorro2.nome)