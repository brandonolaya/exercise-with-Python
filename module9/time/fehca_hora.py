import datetime



mi_hora = datetime.time(19,31)

print(mi_hora) #toda la informacion que he puesto
print(mi_hora.minute) #asila solo los minutos
print(mi_hora.hour) #aisla solo las horas

mi_dia = datetime.date(2021,8,29)
print(mi_dia)
print(mi_dia.month)#lo aisla por meses 
print(mi_dia.ctime()) #otro formato para mostrar

print(mi_dia.today())# me mustra la fecha del dia actual

