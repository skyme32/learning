# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.

minutos = int(input("Introduce la cantidad de minutos:"))
res_horas = minutos // 60
res_min = minutos % 60
str = ""

if res_horas == 0 and res_min == 0:
    str = res_min.__str__()+" minutos."
if res_horas == 1 and res_min == 0:
    str = "60 minutos."
if res_horas < 1 and res_min < 60:
    str = res_min.__str__()+" minutos."
if res_horas > 1 and res_min == 0:
    str = res_horas.__str__() + " horas."
if res_horas > 0:
    str = res_horas.__str__()+ " horas y "+res_min.__str__()+" minutos."

print(str)