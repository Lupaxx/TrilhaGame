#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Classe do Trilha em Python: retorna as coordenadas de movimentações

#######################  Comandos Sistema Operacional  #########################
def W(matriz, x, y):
    if(matriz[x-1][y] != "-" and matriz[x-1][y] != "#"):
        posicionado = 0
        while(posicionado == 0):
            x -= 1
            if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                posicionado = 1
    return(x)
def A(matriz, x, y): 
    if(matriz[x][y-1] != "|" and matriz[x][y-1] != "#"):
        posicionado = 0
        while(posicionado == 0):
            y -= 1
            if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                posicionado = 1
    return(y)
def S(matriz, x, y): 
    if(matriz[x+1][y] != "-" and matriz[x+1][y] != "#"):
        posicionado = 0
        while(posicionado == 0):
            x += 1
            if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                posicionado = 1
    return(x)
def D(matriz, x, y):
    if(matriz[x][y+1] != "|" and matriz[x][y+1] != "#"):
        posicionado = 0
        while(posicionado == 0):
            y += 1
            if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                posicionado = 1
    return(y)
