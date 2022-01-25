import socket
import subprocess
import re

#metodo de varredura dos ips da rede
#escolha o range de ips que quer descobrir 
def varredura_port(primeiro_ip, ultimo_ip):
    lista = [] #array vazio
    
    for i in range(primeiro_ip, ultimo_ip):
        #instancia do ob socket
        socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        #coloque a faixa de ips da sua rede e a porta de acesso
        ip = '192.168.15.'+str(i)
        porta = 445

        socket.setdefaulttimeout(1)            
        result = socket_obj.connect_ex((ip, porta)) #metodo de conexao

        print(result)
        
        if result == 0:
            lista.append(i)

        socket_obj.close()

    print("Lista de ips na faixa 192.168.15 encontrados na rede\n : ", lista)

#outro memtod de varredura de ips 
#mas desta vez utilizando o ping 
def encontra_ips(primeiro_ip, ultimo_ip):
    lista = [] #array vazio

    for i in range(primeiro_ip, ultimo_ip):
        host="192.168.15."+str(i)

        #executa o comando ping no cmd para cara numero no range
        processo = subprocess.getoutput('ping ' + host)

        #com a biblioteca de expressoes regulares, seleciono a string que vou buscar
        expressao = re.compile(r"TTL=") 
        busca = expressao.search(processo) #metodod search para procura-la na variaevel processo com o valor de ping armazenado

        #neste try execpt verifico se os hosts existem
        try:
            if busca.group() == "TTL=":
                print("host pingavel")
                lista.append(host)
        except:
            print("host não pingavel")
    
    #ver resultado
    print("ips encontrados: ",lista)