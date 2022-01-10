#classe livro
class Livro:
    #construtor da classe livro
    #perceba que o atributo atual não é obrigatorio
    def __init__(self, titulo, autor, genero, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas
        self.atual = 0

    #metodos da clasee livro
    def info(self):
        print("\ntitulo da obra: ", self.titulo,
                "\nseu autor é: ", self.autor,
                "\ngenero da obra: ", self.genero,
                "\ntotal de paginas: ", self.num_paginas)

    def abrir_livro(self):
        print("\nvoce acaba de abrir o livro ", self.titulo, " para começar a sua leitura")
    
    def fechar_livro(self):
        print("\nvoce acaba de fechar o livro ", self.titulo, " para guardalo")
    
    def passar_pagina(self, quantidade):
        print("\navançando pagina")
        self.atual = self.atual + quantidade
        print("\nsua pagina atual é: ", self.atual)

    def voltar_pagina(self, quantidade):
        print("\nvoltando pagina")
        self.atual = self.atual - quantidade
        print("\nsua pagina atual é: ", self.atual)