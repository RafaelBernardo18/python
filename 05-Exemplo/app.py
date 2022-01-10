from time import sleep
from random import randint

#criando um dicionario/simulando batalha de um rpg comun
vida = 30
mana = 6
vida_inimigo = 20
num_pocoes = 2
acao = {1: "ataque", 2: "magia", 3: "utilizar pocao de cura", 4: "fugir"}

#funçao para mostra o status da batalha apos uma acao
def status(vida, mana, num_pocoes, vida_inimigo):
    sleep(1)
    print("\nvida atual: ", vida)
    print("mana atual: ", mana)
    print("numero de poções: " , num_pocoes)
    print("\nvida do inimigo: " , vida_inimigo ,"\n")
    sleep(1)

def inimigo_turno():
        sleep(1)
        print("inimigo atacou seu pergonagem")
        sleep(1)


print("parece que uma batalha comceçou")

#utilizando while para um laco infinito
while True:
    print("\nseu personagem está esperando por uma ação")
    print(acao)
    valor = int(input("o que ele fará ?..."))
    
    if valor == 1:
        print("seu personagem atacou!")
        vida_inimigo = vida_inimigo - 5
        inimigo_turno()
        vida = vida - 8
        status(vida, mana, num_pocoes, vida_inimigo)

        if vida <= 0:
            print("seu personagem morreu")
            break
        elif vida_inimigo <= 0:
            print("seu inimigo morreu")
            break
        else:
            print("...")

    elif valor == 2 :
        if mana >= 3:
            print("seu persogame usou magia")
            vida_inimigo = vida_inimigo - 7
            mana = mana - 3
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)
            
            if vida <= 0:
                print("seu personagem morreu")
                break
            elif vida_inimigo <= 0:
                print("seu inimigo morreu")
                break
            else:
                print("...")

        else:
            print("seu personagem nao tem mana suficiente")
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)
            
            if vida <= 0:
                print("seu personagem morreu")
                break
            elif vida_inimigo <= 0:
                print("seu inimigo morreu")
                break
            else:
                print("...")

    elif valor == 3:
        if  15 <= vida < 30 and num_pocoes > 0:
            print("seu personagem tomou uma pocao de cura")
            num_pocoes = num_pocoes - 1
            vida = 30
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)
            

        elif vida < 15 and num_pocoes > 0:
            print("seu personagem tomou uma pocao de cura")
            num_pocoes = num_pocoes -1
            vida = vida + 15
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)   

        elif vida == 30 or num_pocoes == 0:
            print("você não tem poções ou sua vida já esta cheia")
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)

            if vida <= 0:
                print("seu personagem morreu")
                break
            else:
                print("...")

    elif valor == 4 :
        print("seu personagem esta tentando fugir...")
        sleep(1)
        randomico = randint(0,100)
        if randomico >= 90:
            print("seu personagem consegui fugir")
            break
        elif randomico <= 90:
            print("falhou")
            inimigo_turno()
            vida = vida - 8
            status(vida, mana, num_pocoes, vida_inimigo)

            if vida <= 0:
                print("seu personagem morreu")
                break
            else:
                print("...")

    else :
        print("tente novamente")