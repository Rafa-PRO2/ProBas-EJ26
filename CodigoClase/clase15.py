# Problema 30: Análisis de beneficios

precio,cantidad,egresos = None,None,None

precio = float(input("Ingrese el valor del producto:\n"))
cantidad = float(input("Ingrese la cantidad de producto:\n"))
egresos = float(input("Ingrese el costo de compra:\n"))

ingreso_total = precio * cantidad

if ingreso_total < egresos:
    print("Estamos en pérdida")
elif ingreso_total == egresos:
    print("Estamos en equilibrio")
else:
    print("Estamos en ganancia")
    
