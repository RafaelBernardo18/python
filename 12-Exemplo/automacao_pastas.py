import os
from shutil import move

#caminhos das pasatas
path_downloads = r'c:\Users\rafae\Downloads'
path_txt = r'c:\Users\rafae\Downloads\txt'
path_pdf = r'c:\Users\rafae\Downloads\pdf'
path_zip = r'c:\Users\rafae\Downloads\zip'
path_exe = r'c:\Users\rafae\Downloads\exe'

#variaveis com as extensoes
extensao_txt = '.txt' 
extensao_pdf = '.pdf' 
extensao_zip = '.zip' 
extensao_exe = '.exe'

#metodos para carregar o nome dos arquirvos e verificar se são validos como arquivs
def carregar_arquivos(path_downloads):
    return [f for f in os.listdir(path_downloads) ]

#metodo para mover o aqruivo para sua repectiva pasta
def organizar_pastas(arquivos):
    for arquivo in arquivos:
        
        if arquivo.endswith(extensao_txt):
            move(arquivo, '{}/{}'.format(path_txt, arquivo))
            print('arquivo {} movido para {}'.format(arquivo, path_txt))
        elif arquivo.endswith(extensao_pdf):
            move(arquivo, '{}/{}'.format(path_pdf, arquivo))
            print('arquivo {} movido prar {}'.format(arquivo, path_pdf))
        elif arquivo.endswith(extensao_zip):
            move(arquivo, '{}/{}'.format(path_zip, arquivo))
            print('arquivo {} movido prar {}'.format(arquivo, path_zip))
        elif arquivo.endswith(extensao_exe):
            move(arquivo, '{}/{}'.format(path_exe, arquivo))
            print('arquivo {} movido prar {}'.format(arquivo, path_exe))
        else:
            print("extensao de aquivo nao programada")

if __name__ == "__main__":
    
    #movendo para a pasta de downloads e executando metodos criados anteriormente
    os.chdir('..\..\..\..')
    os.chdir(path_downloads)
    print(os.getcwd())
    arquivos = carregar_arquivos(path_downloads)
    organizar_pastas(arquivos)