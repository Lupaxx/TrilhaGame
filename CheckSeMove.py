def W(matriz, x, y):
    if(x != 0): 
        if(matriz[x-1][y] != "-"):
            casa = 0
            while(casa == 0):
                x -= 1
                if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                    casa = 1
        if(matriz[x][y] == " "):
                return(True)
    return(False)
def A(matriz, x, y):
    if(y != 0):
        if(matriz[x][y-1] != "|"):
            casa = 0
            while(casa == 0):
                y -= 1
                if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                    casa = 1
        if(matriz[x][y] == " "):
            return(True)
    return(False)

def S(matriz, x, y):
    if(x != 6):
        if(matriz[x+1][y] != "-"):
            casa = 0
            while(casa == 0):
                x += 1
                if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                    casa = 1
        elif((matriz[x+1][y] == " ") or (matriz[x+1][y] == "X") or (matriz[x+1][y] == "O")):
            x += 1
        if(matriz[x][y] == " "):
            return(True)
    return(False)
def D(matriz, x, y):
    if(y != 6):
        if(matriz[x][y+1] != "|"):
            casa = 0
            while(casa == 0):
                y += 1
                if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                    casa = 1
        if(matriz[x][y] == " "):
            return(True)
    return(False)
