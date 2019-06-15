# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
# desea saber cuanto deberá pagar finalmente por su compra.

precio = float(input("Dime el precio:"))
desc = float(input("Descuento:"))
print("Descuento",precio * (desc/100))
print("Precio final:",precio - precio * (desc/100))