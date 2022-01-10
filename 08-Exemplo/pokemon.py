#classe pokemon
class Pokemon():
    #construtor da classe
    def __init__(self, nome, especie, peso, altura, tipo_primario):
        self.nome = nome
        self.especie = especie
        self.peso = peso
        self.altura = altura
        self.tipo_primario = tipo_primario
    
    #metodo da classe Pokemon
    def info(self):
        print("\nnome do pokemon: ", self.nome,
            "\nespecie do pokemon: ", self.especie,
            "\npeso do pokemon: ", self.peso,
            "\naltura do pokemon: ", self.altura,
            "\ntipo primario do pokemon: ", self.tipo_primario)