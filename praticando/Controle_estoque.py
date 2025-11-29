class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco =preco
        self.quantidade = quantidade

    def aumentar_quantidade(self,qtd):
        self.quantidade += qtd

    def remover_estoque(self,qtd):
        if self.quantidade-qtd <0:
            return 'valor ivalido '
        else:
            self.quantidade -= qtd

    def caucular_valor_total (self):
     tot = self.preco*self.quantidade
     return tot


produto1 = Produto("macarrao",3.0,10)
produto1.aumentar_quantidade(10)
produto1.remover_estoque(10)
print(produto1.caucular_valor_total())

print(vars(produto1))



