#classe em python
class Livro:
    #seu metodo construtor 
    #passamaos os atributos que a classe tera aqui
    def __init__(self, nome, genero, num_paginas):
        self.nome = nome
        self.genero = genero
        self.num_paginas = num_paginas
    
    #metodos da classe
    def status(self):
        print("o nome do livro é: " , self.nome)
        print("o genero do livro é: " , self.genero)
        print("a quantidade de paginas: " , self.num_paginas)