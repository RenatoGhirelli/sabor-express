from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
  def __init__(self, nome, preco):

      self._nome = nome
      self._preco = preco  



  """
  Esse é um método abstrato, o que significa que ele não terá instância diretamente pela classe item_cardapio.
  
  Esse método será usado pelas classes filhas (prato e bebida), cada uma tem o seu próprio desconto, isso é o polimorfismo
  """
  @abstractclassmethod
  def aplicar_desconto(self):
     pass