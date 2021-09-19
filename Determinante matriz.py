#busca la determinante de una matrix
#agradecimiento a Jehova , el unico Dios verdadero 



def Matriz_2x2():


    matriz = [
    
    [-1,4],
    [-9,4],

    ]


    diagonal_Principal = 0
    diagonal_Secundaria = 0

    diagonal_Principal = matriz[0][0] * matriz[1][0] 
    diagonal_Secundaria =  matriz[0][1] * matriz[1][1]

    determinante = diagonal_Principal - diagonal_Secundaria

    print(determinante + " este numero significa que la matriz de 2x2 funciona")

def Matriz_3x3(matriz):


    #ruler of sarrus
    surrus = matriz[3 :]

    #this var , to change the diagonal 

    diagonal_Principal = matriz[0] * matriz[4] * matriz[8] 
    diagonal_Principal += matriz[3] * matriz[7] * matriz[0]
    diagonal_Principal += matriz[6] * matriz[4] * matriz[8]

    diagonal_Secundaria =  matriz[2] * matriz[4] * matriz[6]
    diagonal_Secundaria +=  matriz[5] * matriz[7] * matriz[0]
    diagonal_Secundaria +=  matriz[8] * matriz[1] * matriz[3]

    determinante = diagonal_Principal - diagonal_Secundaria
    print(determinante)
    print( "este texto comprueba que la matriz 3x3 funciona")


#Matriz_2x2()

Matriz_3x3([1,0,4,3,8,7,7,-4,-8])