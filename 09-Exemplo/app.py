#importando a biblioteca para conecartomos com o banco de dados
import mysql.connector

#funçoes do banco que estou utilizando
#eu utilizo o %s pois quero que o usuario digite os valores 
#existem diversos comandos mas estes são os principais
SQL_SELECT = "SELECT *FROM herois WHERE nome_heroi = %s"
SQL_DELETE = "DELETE FROM herois WHERE nome_heroi = %s"
SQL_INSERT = "INSERT INTO herois(nome_heroi, nome_persona, afiliacao, parceiro, poderes) VALUES (%s, %s, %s, %s, %s)"
SQL_UPDATE = "UPDATE herois SET nome_heroi = %s WHERE nome_heroi = %s"

#conexao com o banco de dados
#este é um banco de dado simples
#possui apenas uma tabela chamada herois e possui os campos nome_heroi, nome_persona, afiliacao, parceiro, poderes
#caso queira utilizados, o banco esta presente no diretorio do projeto
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "banco_heroi"
)

print(db) #verico se o objeto do banco foi criado
meu_cursor = db.cursor() #instancia do banco de dados para chamar as funções

#menu para o usuario
print("1-inserir \n2-ler \n3-deletar \n4-atualizar")
num = int(input("Selecione: "))

if num == 1:
    #insert
    #inserir um novo heroi no banco de dados
    #pede ao usuario para inserir todos os valores do heroi que sera inserido
    heroi = input("nome de heroi: ")
    pessoa = input("nome do personagem: ")
    afi = input("afiliaçao: ")
    parceiro = input("parceiro do heroi: ")
    poderes = input("poderes do heroi: ")
    valores = (heroi, pessoa, afi, parceiro, poderes)

    meu_cursor.execute(SQL_INSERT, valores)
    db.commit()
    print("valor inserido com sucesso")

elif num == 2:
    #select
    #busca os valores contidos no banco
    #pede que o usuario digite o nome do heroi
    nome = input("digite o nome do heroi que esta buscando: ")
    nome = (nome, )

    meu_cursor.execute(SQL_SELECT, nome)
    busca = meu_cursor.fetchall()
    for x in busca:
        print(x)

elif num == 3:
    #delete
    #deleta todos os valores de um heroi
    #pede ao usuario que escolha o heroi que sera excluido
    nome = input("digite o nome do heroi que deseja deletar da tabela: ")
    nome = (nome,)

    meu_cursor.execute(SQL_DELETE, nome)
    db.commit()
    print("valor deletado com successo")

elif num == 4:
    #update
    #atualiza o campo nome_heroi que contem os valores de nomes de herois
    #pede ao usuario que digite o nome do heroi que quer modificar e o novo nome que este vai ter no banco
    nome = input("digite o nome do heroi que quer editar: ")
    novo_nome = input("novo nome: ")

    meu_cursor.execute(SQL_UPDATE, (novo_nome, nome))
    db.commit()
    print("heroi atualizado com sucesso")

else:
    print("nenhum valor selecionado") 