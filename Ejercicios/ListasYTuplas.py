#Listas y tuplas
#Escribir un programa que almacene las matrices,
# haga el producto entre ellas dos y muestre el resultado en una lista.
#Para almacenar las matrices utilice tuplas anidadas,
# y para mostrar resultados use listas anidadas.
MatrizA = ((1, 2, 3), (4, 5, 6))
MatrizB = ((-1, 0), (0, 1), (1, 1))

Resultados = [[0, 0], [0, 0]]
varSum = 0

for i in range(2):
    for k in range(2):
        varSum = 0
        for j in range(3):
            print("A "+str(MatrizA[k][j]))
            print("B "+str(MatrizB[j][i]))
            print("R "+str(MatrizA[k][j]*MatrizB[j][i]))
            print("  ")
            varSum += MatrizA[k][j]*MatrizB[j][i]
        print(varSum)
        Resultados[k][i] = varSum
print(Resultados)
