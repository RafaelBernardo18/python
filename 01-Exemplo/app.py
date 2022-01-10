#as variaveis em python possuem tipagem dinamica e nao precisa ser declarada
#voce pode atribuir se quiser/precisar a tipagem dessa forma
#lemre que cada variavel em python tambem é um objeto

#tipos de variaveis
idade = int(20)
peso = float(45.5)
valor = bool(True)
nome = str("tayso roberta macalister")

print ("nome: ", nome, "peso: ", peso, "valor: ", valor, "idade: ", idade)

#lista
lista = ["lista", "em", "python"]

#printando a lista inteira
for i in lista:
    print(i)

#escolhendo um valor determinado da lista
print(lista[2])

#dicionario
dict = {'codigo1' : 'python', 'codigo2': 'php', 'codigo3': 'java'}

#printando o dicionario inteiro
print(dict)

#valor especifico
print("estamos aprendeno a linguagem: " + dict['codigo1'])

#como cada variavel é um objeto elas podem possuir metodos  
print(dict.values())
print(dict.keys())