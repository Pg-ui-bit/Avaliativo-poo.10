class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        return f"O produto {self.nome} custa R$ {self.preco:.2f}"

produto1 = Produto("Notebook", 3500)
print(produto1.mostrar_preco())