#escribir un programa que guarde en un diccionario los precios de las frutas en la tabla pregunte al usuario por una frutas

# un numero de kilos y muestre en pantalla el precio el numero de kilos

# si la fruta no esta en el diccionario debe mostrar un mensaje acerca de ello


diccionario = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}


frutaElegida = input("Ingrese la fruta deseada: ")

kilos = int(input("Ingrese los kilos deseados: "))


print(diccionario.get(frutaElegida, "No existe!!"))


precioFrutaSeleccionada = diccionario[frutaElegida]

precioTotal = (kilos) * precioFrutaSeleccionada


print("El precio total es " + str(precioTotal) +
      " y " + " los kilos fueron " + str(kilos))
