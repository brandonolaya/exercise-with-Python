### solo es pra ver el uso llamando funciones entre paquetes
from pkg1.mod1 import func1,func2
from pkg1.mod2 import func3,func4
## es un llamado debil por que si hay otra funcion con el mismo nombre F
print(func1(),func2())
print(func1(),func2())


import pkg1

##es un llamado fuerte para que no hayan choques con otras funciones
## es buena practica
print(pkg1.mod1.func1())
print(pkg1.mod2.func4())
