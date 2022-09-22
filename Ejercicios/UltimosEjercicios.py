#1.- MAPA CARACTERES
#Implementar una funcion llamada mapaDeCaracteres que reciba como paramatro una palabra y devuelva un mapa de caracteres
#unico de una plaabra el mapa de caracteres es una lista numerica en la que el numero 0 se corresponde con el
#primer caracter de la palabra el 1 con el siguiente caracter y asi sucesivamente 
# a b c d
#[0,1,2,3]

# a a b b c b
#[0,0,1,1,2,1]

# z a g z d a a
#[0,1,2,0,3,1,1]

#2.- POBLACION
#IMPLEMENTAR UNA FUNCION LLAMADA ordenaCiudades que  reciba como argumento un diccionario con
# ciudades y su plobacion y devuelva una lista de las ciudades demas de 200 mil habitantes la lista devuleta 
# debe estar ordenada de MAYOR A MENOR 

l=[]
def ordenaCiudades(d1):
    print(d1)
    for a in sorted(d1):
        if dict[a] > 200000:
            l.append[a]
            print(l)
        

d1 = {"MTY":500000,"LAREDO":150000,"VICTORIA":200000}
print(d1)
ordenaCiudades(d1)





#3.- MANTENER POSITIVOS
# #Escribir una funcion llamada ordenaPositivos que dada una lista de numero enteros ... negativos devuelva 
# una nueva lista con los numero positivos ordenados de mayor a menor y mantengan los numero negativos en la 
# misma posicision que la lista original.
#[6,3,-2,5,-8,2,-2]
#RESULTADO [2,3,-2,5,-8,6,-2]

#4.- PALABRAS
# Hacer un programa que reicba como entrada o teclado una secuencia de plaabras separadas por espacios en blanco e 
# imprima las palabras ordenadas alfanumericamente en mayusculas y despues de haber eliminado los duplicados 

#"Lo mejor del lenguaje Python es que es un lenguaje del que no te aburres"
#RESULTADO "ABURRES DEL ES LENGUAJE LO MEJOR NO PYTHON QUE TE UN"
# l = []
# palabras = input("INSERTE LA FRASE: ")
# palabras = palabras.upper()
# palabras = palabras.split()
# print(palabras)
# s = {}
# s = set(palabras)
# print(s)
# l = list(s)
# l.sort()
# print(l)