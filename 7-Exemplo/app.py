#importtando classes e modulos
from livro import Livro
from time import sleep

#instanciando objeto
obj = Livro("Berserk vol-1", "Kentaro Miura", "Fantasia/Medieval", 219)

#ivocando metodos
obj.info()
sleep(1)

obj.abrir_livro()
sleep(2)

obj.passar_pagina(10)
sleep(2)

obj.voltar_pagina(5)
sleep(2)
obj.fechar_livro()