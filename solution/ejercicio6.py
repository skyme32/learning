# Calcular la media de tres números pedidos por teclado
import stats as stats

num1 = float(input("Introduce el número 1:"))
num2 = float(input("Introduce el número 2:"))
num3 = float(input("Introduce el número 3:"))
media = (num1 + num2 +num3) / 3
print("La media es:", media)

media2 = stats.mean([num1,num2,num3])
print("La media es:", media2)
