#Creamos el diccionario en donde vamos a colocar cavle - valor
informacion= {"Nombre":"Juan", "Edad":24,"Ciudad": "Quito","Email":"juan@gmail.com","Profesión": "Talento Humano"}

print("Diccionario actual\n",informacion)

#Creamos un menú de opciones

print("\n MENÚ")
print("\n1.Acceder al valor asociado con la clave ciudad y modifícar con una ciudad diferente",
          "\n2. Agregar una nueva clave-valor al diccionario que represente la profesion de la persona.",
          "\n3. Verifica si la clave telefono existe en el diccionario",
          "\n4. Elimina la clave edad del diccionario",
          "\n5. Mostrar diccionario" )


opcion=int(input("\nIngrese la opcion: "))
while opcion :
    #Creamos el menú

    if opcion == 1 :
        print(informacion["Ciudad"])  #Imprimimos la ciudad actual
        informacion.update({"Ciudad": "Cuenca"})  #Modificamos la ciudad
        print(f"Información modificada: {informacion["Ciudad"]}")  #Imprimimos la ciudad modificada






    elif opcion == 2:
       informacion.update({"Profesión": "Ingeniero en Sistemas"})  #Actualizamos la profesion
       print(f"Profesión modificada: {informacion["Profesión"]}") #Imprimimos la porfesion modificada


    elif opcion ==3 :
    #Verificamos si existe la clave de telefono
        if "Telefono" in informacion:
            print("Si existe el telefono")
            print(f"Telefono: {informacion["Telefono"]}")

        else:
            print("Telefono añadido")
            informacion.update({"Telefono": 98405878})
        print(f"Telefono : {informacion["Telefono"]}")


    elif opcion == 4:
        del informacion["Edad"]
        print(f"{"Edad"} eliminada")

    elif opcion == 5 :
        print(f"El diccionario actualizado es: {informacion}")


    elif opcion > 5:
        break

    opcion = int(input("\nIngrese la opcion: "))