from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("sad", 3)
restaurante_praca.receber_avaliacao("fgh", 0)


def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()