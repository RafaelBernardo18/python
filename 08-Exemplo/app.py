from evolucao import Evolucao
from pokemon import Pokemon

#instanciando objetos
pokemon1 = Pokemon("Monferno", "Playful", 22, 0.9, "fogo")
pokemon2 = Evolucao("Infernape", "Flame", 55, 1.2, "fogo", "lutador")

#invocando memtodos
pokemon1.info()

pokemon2.info()
pokemon2.outro_secundario()