#importando a classe
from livro import Livro 

#instanciando objetos
obj1 = Livro("A piada mortal", "historias em quadrinhos", 60)
obj2 = Livro("Asilo Arkham", "historias em quadrinhos", 216)
obj3 = Livro("Berserk vol-1", "mangá", 219)

#chamando metodos
obj1.status()
obj2.status()
obj3.status()