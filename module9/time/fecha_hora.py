from datetime import datetime ##agrega una fecha con horas y demas


mi_fecha = datetime(2022,4,15,9,45,45)
print(mi_fecha)

mi_fecha = mi_fecha.replace(year=1996)#cambia el año que quiero
print(mi_fecha)

despierta = datetime(2023,1,2,7,1)
durmio = datetime(2023,1,2,23,59)

despierto = durmio - despierta

print(despierto)