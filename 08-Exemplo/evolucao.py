from pokemon import Pokemon

#herança da classe pokemon
#assim a classe Evolucao tem accesso a todos os atributos e metodos da classe Pokemon
class Evolucao(Pokemon):
    def __init__(self, nome, especie, peso, altura, tipo_primario, tipo_secundario):
        Pokemon.__init__(self, nome, especie, peso, altura, tipo_primario)
        self.tipo_secundario = tipo_secundario
        

    def outro_secundario(self):
        print("este pokemon possui uma tipagem secundaria: ", self.tipo_secundario)