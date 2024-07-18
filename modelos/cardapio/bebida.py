from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
  def __init__(self, nome, preco, tamanho):
      
      super().__init__(nome, preco) #super() indica que está puxando o construtor da classe pai (ItemCardapio)
      self.tamanho = tamanho


  def __str__(self):
        return self._nome
  

  """
  Esse método é obrigatório, caso não tenha desconto deve-se usar o pass
  """
  def aplicar_desconto(self):
      self._preco -= (self._preco * 0.08)