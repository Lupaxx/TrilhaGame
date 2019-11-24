#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python

#######################  Comandos Sistema Operacional  #########################
import os
        
#################################  Tutorial  ###################################
def Help():
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')
    arquivo = open("tutorial.txt", "r")
    print (arquivo.read())
    input()
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')

###############################  Monta Matriz  #################################
def MontaMatriz(matriz, x, y, p1, p2, instrucoes): #Monta pra colocar no Tabuleiro
    tabuleiro = [" "]*7
    for i in range (7):
	    tabuleiro[i] = [" "]*7
    for i in range (7):
        for j in range (7):
            if((i == x) and (j == y)):
                tabuleiro[i][j] = ">" + matriz[i][j] + "<"
            else:
                tabuleiro[i][j] = "(" + matriz[i][j] + ")"
    MontaTabuleiro(tabuleiro, p1, p2) #PrintMatriz(tabuleiro)
    print(instrucoes)

##############################  Monta Tabuleiro  ###############################
def MontaTabuleiro (matriz, p1, p2):
	#matriz 7x7
	#lugar de peça = 0x0 0x3 0x6 1x1 1x3 1x5 2x2 2x3 2x4 3x0 3x1 3x2 3x4 3x5 3x6 4x2 4x3 4x4 5x1 5x3 5x3 6x0 6x3 6x6
    if (os.name == 'nt'):
        os.system('cls')
    else:	
        os.system('clear')
    
    print("")
    print("                  ",matriz[0][0], "----------------", matriz[0][3], "----------------", matriz[0][6], "", sep="")
    print("                   |                  |                  |")
    print("                   |                  |                  |")
    print("                   |    ", matriz[1][1], "----------", matriz[1][3], "----------", matriz[1][5], "    |", sep="")
    print("       |-----|     |     |            |            |     |     |-----|", )
    print("       |  ", p1[0], "  |     |     |            |            |     |     |  ", p2[0], "  |", sep="")
    print("       |  ", p1[1], "  |     |     |    ", matriz[2][2], "----", matriz[2][3], "----", matriz[2][4], "    |     |     |  ", p2[1], "  |", sep = "")
    for i in range (2,4):
            print("       |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
    print("       |  ", p1[4], "  |    ", matriz[3][0], "---", matriz[3][1], "---", matriz[3][2], "           ", matriz[3][4], "---", matriz[3][5], "---", matriz[3][6], "    |  ", p2[4], "  |", sep="")
    for i in range (5,7):
            print("       |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
    print("       |  ", p1[7], "  |     |     |    ", matriz[4][2], "----", matriz[4][3], "----", matriz[4][4], "    |     |     |  ", p2[7], "  |", sep = "")
    print("       |  ", p1[8], "  |     |     |            |            |     |     |  ", p2[8], "  |", sep="")
    print("       |-----|     |     |            |            |     |     |-----|", )
    print("                   |    ", matriz[5][1], "----------", matriz[5][3], "----------", matriz[5][5], "    |", sep="")
    print("                   |                  |                  |")
    print("                   |                  |                  |")
    print("                  ",matriz[6][0], "----------------", matriz[6][3], "----------------", matriz[6][6], "\n", sep="")

#################################  Move seta  ##################################
def Move(matriz, x, y, p1, p2, instrucoes, c, enter):
    if (ord(c) == 32): #espaço -> enter
        enter = 1
    elif(ord(c) == 119): #w
        if(x != 0):
            if(matriz[x-1][y] == "|"): #Distancia grande entre as casas
                posicionado = 0
                while(posicionado == 0):
                    x = x -1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
            elif((matriz[x-1][y] == " ") or (matriz[x-1][y] == "X") or (matriz[x-1][y] == "O")):
                x = x -1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 97): #a
        if(y != 0):
            if(matriz[x][y-1] == "-"):
                posicionado = 0
                while(posicionado == 0):
                    y = y -1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
            elif((matriz[x][y-1] == " ") or (matriz[x][y-1] == "X") or (matriz[x][y-1] == "O")):
                y = y -1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 115): #s
        if(x != 6):
            if(matriz[x+1][y] == "|"):
                posicionado = 0
                while(posicionado == 0):
                    x += 1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
            elif((matriz[x+1][y] == " ") or (matriz[x+1][y] == "X") or (matriz[x+1][y] == "O")):
                x += 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 100): #d
        if(y != 6):
            if(matriz[x][y+1] == "-"):
                posicionado = 0
                while(posicionado == 0):
                    y = y + 1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
            elif((matriz[x][y+1] == " ") or (matriz[x][y+1] == "X") or (matriz[x][y+1] == "O")):
                y = y + 1
                MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 63): #?
        Help()
        MontaMatriz(matriz, x, y, p1, p2, instrucoes)

    coordenadas = []
    coordenadas.append(x)
    coordenadas.append(y)
    coordenadas.append(enter)
    return coordenadas
                    
#################################  Selected  ###################################
def Selected (matriz, x, y, p1, p2, instrucoes): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    import Kbhit
    kb = Kbhit.KBHit()
    MontaMatriz(matriz, x, y, p1, p2, instrucoes)

    hit = 0
    enter = 0
        
    coordenadas = []
    coordenadas.append(x)
    coordenadas.append(y)
    coordenadas.append(0)
    if(os.name == 'nt'):
        while (coordenadas[2] == 0):
            if kb.kbhit():
                c = kb.getch()
                coordenadas = Move(matriz, coordenadas[0], coordenadas[1], p1, p2, instrucoes, c, coordenadas[2])
    else:
        while (coordenadas[2] == 0):
            c = getkey()
            coordenadas = Move(matriz, coordenadas[0], coordenadas[1], p1, p2, instrucoes, c, coordenadas[2])
    return (coordenadas)

###################################  Main  #####################################
def main():
    matriz = [" "]*7
    for i in range (7):
	    matriz[i] = [" "]*7
	
    matriz[0][1] = "-"
    matriz[0][2] = "-"
    matriz[0][4] = "-"
    matriz[0][5] = "-"
    matriz[1][0] = "|"
    matriz[1][2] = "-"
    matriz[1][4] = "-"
    matriz[1][6] = "|"
    matriz[2][0] = "|"
    matriz[2][1] = "|"
    matriz[2][5] = "|"
    matriz[2][6] = "|"
    matriz[3][3] = "#"
    matriz[6][1] = "-"
    matriz[6][2] = "-"
    matriz[6][4] = "-"
    matriz[6][5] = "-"
    matriz[5][0] = "|"
    matriz[5][2] = "-"
    matriz[5][4] = "-"
    matriz[5][6] = "|"
    matriz[4][0] = "|"
    matriz[4][1] = "|"
    matriz[4][5] = "|"
    matriz[4][6] = "|"
    x = 0
    y = 3

    p1 = []
    p2 = []
    for i in range (9): #peças que faltam paara serem posicionadas
            p1.append("X")
            p2.append("O")

    
    Posiciona = [] #Textinho pra mostras pro jogador
    Posiciona.append("     É a vez do jogador 1. Sua peça é 'X'. Escolha onde posiciona-la. \nUse WASD para mover, espaço para confirmar e ? para tirar as duvidas.")
    Posiciona.append("     É a vez do jogador 2. Sua peça é 'O'. Escolha onde posiciona-la. \nUse WASD para mover, espaço para confirmar e ? para tirar as duvidas.")
    for i in range (7):
        for j in range (7):
            print(matriz[i][j], end ="")
        print(" ")
    for i in range (8, -1, -1):
        jogada_valida = 0
        coordenadas = []
        while(jogada_valida == 0): #jogada do x
            coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[0])
            if(matriz[coordenadas[0]][coordenadas[1]] == " "): #da pra colocar ali?
                matriz[coordenadas[0]][coordenadas[1]] = "X"
                jogada_valida = 1
                p1[i] = " " #tirou uma peça
            x = coordenadas[0]
            y = coordenadas[1]
        x = coordenadas[0]
        y = coordenadas[1]
        jogada_valida = 0
        while(jogada_valida == 0): #jogada do y
            coordenadas = []
            coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[1])
            if(matriz[coordenadas[0]][coordenadas[1]] == " "):
                matriz[coordenadas[0]][coordenadas[1]] = "O"
                jogada_valida = 1
                p2[i] = " "
            x = coordenadas[0]
            y = coordenadas[1]
                
    MontaMatriz(matriz, x, y, p1, p2, 'cabo')

###############################  Chama Main  #################################
