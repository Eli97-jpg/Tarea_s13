
def suma (matriz):  #Creamos otra función con un parametro
    sumar = 0  # Declaramos la variable suma en cero
    des = 0
    for i in range(len(matriz)): # Cremoas un bucle for para recorrer la longitud de la matriz
        sumar = sumar + matriz[i][3]  #Sumamos la matriz en su posición 3
        des = sumar - (desc * sumar / 100)  # La suma restamos por el porcentaje de descuento

    return  des  #Retornamos el descuento



def calcular_descuento (producto,cantidad,precio,descuento): #Creamos la función con 3 parametros

    subtotal = cantidad * precio  #Realizamos la multiplicacion de la cantidad por el precio
    matriz = [producto,cantidad,precio,subtotal,descuento]  # En la matriz guardamos los elementos
    return matriz # Retornamos la matriz


desc = int(input("Ingrese el descuento: "))  #Declaramos la variable para que ingrese el descuento

matriz_total = []  #Creamos una lista vacia





while True :  #Creamos un bucle while para ingresar los datos
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    matriz_total.append(calcular_descuento(producto, cantidad, precio, desc))
    decision = input("¿ Desea ingresar otro prodcuto ? ") #Preguntamos si deseamos agregar mas prodcutos
    if decision == "no":
        break  #Si coloca no se rompe y queda hasta ahi el programa


for i in matriz_total :  #Imprimimos nuestra tabla
    print(i)
precio_F = suma(matriz_total)  #Llamamos a la función y su parametro
print(f"El precio final de los productos con el descuento del {desc}% es {precio_F}")  #Imprimimos el precio final con el descuento