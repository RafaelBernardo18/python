#estrutura de dados
#listas em geral
livros = ["o chamado de cthulhu", "a piada mortal", "cavaleiro das treavas", "o reino do amanha"]

while True:   #forma de criar um laço infinito
    acao = int(input("escolha uma ação para realizar na lista: "))

    if acao == 1:
        print("visualizando lista")
        print(livros)

    elif acao == 2:
        print("adicionar livro na lista")
        novo_livro = input("digite o nome do novo livro: ")
        livros.append(novo_livro)

    elif acao == 3:
        print("adicionar livro na lista e sua posição")
        novo_livro = input("digite o nome do novo livro: ")
        posicao = int(input("digite a posicao referente ao livro:"))
        livros.insert(posicao, novo_livro)

    elif acao == 4:
        print("removento um livro da lista")
        livro_removido = str(input("digite o nome do livro que quer remover: "))
        livros.remove(livro_removido)
    
    elif acao == 5:
        print("removento um livro da lista")
        livro_removido = int(input("digite o valor da posicao da lista"))
        livros.pop([livro_removido])
    
    elif acao == 6:
        print("organizando livros")
        livros.sort(key=None, reverse=False)
    
    elif acao == 7:
        print("invertendo ordem do livros")
        livros.reverse()
    
    else:
        break  ##saindo do laço infinito