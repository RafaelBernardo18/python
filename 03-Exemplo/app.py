#importando bibliotecas
#para saber todas as funcionalidade desta biblioteca pode consultar: 
# https://docs.python.org/3/library/math.html
import math

#criando um conversor de potenca
#teremos a potencia em Watts e em dBm
#utilizando funçoes para facilitar o processo
def converteParaWatts():
    valor = float(input("insira um valor em Watts: "))
    dbm = float(10 * math.log10(valor/0.001))
    return print("o valor convertido para dbm é: ", dbm)

def converteParaDbm():
    valor = float(input("insira um valor em dbm: "))
    watt = (math.pow(10, ((valor)/10)))*0.001
    return print("o valor convertido para watt é ", watt)

converteParaWatts()
converteParaDbm()