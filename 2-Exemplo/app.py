#armazenar valor de variaveis
nome = input("digite o seu nome: ")
altura = float(input("digite quanto voce tem de altura: "))
massa = float(input("digite o seu peso: "))

imc = float(massa/(altura*altura))

#estrutura condificonal if
if imc <= 18.5:
    print("parece que %s esta abaixo do peso" % nome)
    print("seu imc é de: %.2f" % imc)
elif 18.5 < imc <= 24.9:
    print("parece que %s esta com o peso normal" % nome)
    print("seu imc é de: %.2f" % imc)
elif 25 < imc <= 29.9:
    print("parece que %s esta com sobrepeso" % nome)
    print("seu imc é de: %.2f" % imc)
elif 30 < imc <= 40:
    print("parece que %s esta obeso" % nome)
    print("seu imc é de: %2f" % imc)   
else:
    print("parece que não foi possivel calcular seu imc")
    print("voce deve estar muito pesado")