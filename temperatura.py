# Declaramos nuestra lista 3D actualizada
# 3x7x3
temperatura_semana = [
    [  # Ciudad 1
        [30, 28, 29, 31, 33, 32, 34], # Semana
        [35, 34, 33, 36, 37, 38, 39], # Semana
        [40, 42, 43, 41, 45, 46, 47], # Semana
        [48, 49, 50, 51, 52, 53, 54]  # Semana
    ],
    [  # Ciudad 2
        [20, 21, 22, 23, 24, 25, 26], # Semana
        [27, 28, 29, 30, 31, 32, 33], # Semana
        [34, 35, 36, 37, 38, 39, 40], # Semana
        [41, 42, 43, 44, 45, 46, 47]  # Semana
    ],
    [  # Ciudad 3
        [15, 16, 17, 18, 19, 20, 21], # Semana
        [22, 23, 24, 25, 26, 27, 28], # Semana
        [29, 30, 31, 32, 33, 34, 35], # Semana
        [36, 37, 38, 39, 40, 41, 42]  # Semana
    ]
]

def promedio (c,s): #Creamos nuestra funcion, la cual le damos 2 argumentos que son de ciudades y semanas


    # Inicializamos variables en cero
    suma_total = 0
    cantidad_total = 0


    # Utilizamos bucles for anidados para recorrer la estructura
    for ciudades in  range(len(temperatura_semana)):  #El bucle ciudades va a recorrer toda la lista
     if ciudades == c: #Comparamos si al recorrer la lista nuestro numero es igual al de ciudad que declaramos
            for semanas in range (len(temperatura_semana[ciudades])):  # Bucle semanas va a recorrer dentro de nuestro bucle ciudades
                if semanas == s : #Comparamos si al recorrer la lista nuestro numero es igual al de semanas que declaramos
                    for temp in range (len(temperatura_semana[ciudades][semanas])):  # Este bucle temp va a recorrer las temperaturas
                        suma_total += temperatura_semana[ciudades][semanas][temp] # Sumamos las temperaturas de nuestra lista
                        cantidad_total += 1 #Sumamos en 1 nuestro contador

    # Calculamos el promedio
    promedio = suma_total / cantidad_total   # Calculamos el promedio y dividimos para nuestro contador
    return f"El promedio de la temperatura de la ciudad {c} de la semana {s} es: {promedio: }°C"  #Retornamos  un mensaje en el cual nos dara el promedio


ciudad = int(input("Ingrese la ciudad (1 a 3): "))   #Creamos la variable ciudad para que el usuario ingrese que ciudad desea
semana = int(input("Ingrese la semana (1 a 4 ): "))   #Creamos la variable semana para que el usuario ingrese la semana que desea el promedio

#Llamamos a nuestra funcion y colocamos los argumentos en este caso las varaibles ciudad y semana
print(promedio(ciudad,semana))