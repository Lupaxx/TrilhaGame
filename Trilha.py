#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python

#######################  Comandos Sistema Operacional  #########################
import os
import CheckSeMove
import Kbhit
import Move
import MenuAbandono
        
#################################  Tutorial  ###################################
def Help():
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')
    arquivo = open("tutorial.txt", "r")
    print (arquivo.read())
    
    kb = Kbhit.KBHit()
    z = 0
    if(os.name == 'nt'):
        while (z == 0):
            if kb.kbhit():
                c = kb.getch()
                z = 1
    else:
        while (z == 0):
            c = getkey()
            z = 1
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')

#################################  Tela de vitória  ###################################
def Vitoria(p):
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')

    if (p=="X"):
        arquivo = open("VitoriaP1.txt", "r", encoding='utf-8')
        print (arquivo.read())
    else:
        arquivo = open("VitoriaP2.txt", "r", encoding='utf-8')
        print (arquivo.read())

    kb = Kbhit.KBHit()
    z = 0
    if(os.name == 'nt'):
        while (z == 0):
            if kb.kbhit():
                c = kb.getch()
                z = 1
    else:
        while (z == 0):
            c = getkey()
            z = 1
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
    MontaTabuleiro(tabuleiro, p1, p2, instrucoes) #PrintMatriz(tabuleiro)

##############################  Hit  ###########################################
def Hit():

    kb = Kbhit.KBHit()
    c = 'q'
    if(os.name == 'nt'):
        while (c == 'q'):
            if kb.kbhit():
                c = kb.getch()
    else:
        while (c == 'q'):
            c = getkey()

    return c

##############################  Monta Tabuleiro  ###############################
def MontaTabuleiro (matriz, p1, p2, instrucoes):
	#matriz 7x7
	#lugar de peça = 0x0 0x3 0x6 1x1 1x3 1x5 2x2 2x3 2x4 3x0 3x1 3x2 3x4 3x5 3x6 4x2 4x3 4x4 5x1 5x3 5x3 6x0 6x3 6x6
    if (os.name == 'nt'):
        os.system('cls')
    else:	
        os.system('clear')
    
    print("|-------------------------------------------------------------------------------|")
    print("|                                                                               |")
    print(instrucoes)
    print("|                                                                               |")
    print("|                  ",matriz[0][0], "----------------", matriz[0][3], "----------------", matriz[0][6], "                    |", sep="")
    print("|                   |                  |                  |                     |")
    print("|                   |                  |                  |                     |")
    print("|                   |    ", matriz[1][1], "----------", matriz[1][3], "----------", matriz[1][5], "    |                     |", sep="")
    print("|       |-----|     |     |            |            |     |     |-----|         |")
    print("|       |  ", p1[0], "  |     |     |            |            |     |     |  ", p2[0], "  |         |", sep="")
    print("|       |  ", p1[1], "  |     |     |    ", matriz[2][2], "----", matriz[2][3], "----", matriz[2][4], "    |     |     |  ", p2[1], "  |         |", sep="")
    for i in range (2,4):
        print("|       |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |         |", sep="")
    print("|       |  ", p1[4], "  |    ", matriz[3][0], "---", matriz[3][1], "---", matriz[3][2], "           ", matriz[3][4], "---", matriz[3][5], "---", matriz[3][6], "    |  ", p2[4], "  |         |", sep="")
    for i in range (5,7):
        print("|       |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |         |", sep="")
    print("|       |  ", p1[7], "  |     |     |    ", matriz[4][2], "----", matriz[4][3], "----", matriz[4][4], "    |     |     |  ", p2[7], "  |         |", sep="")
    print("|       |  ", p1[8], "  |     |     |            |            |     |     |  ", p2[8], "  |         |", sep="")
    print("|       |-----|     |     |            |            |     |     |-----|         |")
    print("|                   |    ", matriz[5][1], "----------", matriz[5][3], "----------", matriz[5][5], "    |                     |", sep="")
    print("|                   |                  |                  |                     |")
    print("|                   |                  |                  |                     |")
    print("|                  ",matriz[6][0], "----------------", matriz[6][3], "----------------", matriz[6][6], "                    |", sep="")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|       Use 'W','A','S','D', para mover, 'ESPAÇO' para confirmar, '?' para      |")
    print("|                 tirar dúvidas e 'F' para abandonar a partida.                 |")
    print("|                                                                               |")
    print("|-------------------------------------------------------------------------------|")

#################################  Move seta  ##################################
def MoveSelect(matriz, x, y, p1, p2, instrucoes, c, enter): #Recebe uma tecla, retorna coordenadas para > <
    if (ord(c) == 32): #espaço -> enter
        enter = 1
    elif(ord(c) == 119): #w
        if(x != 0):
            x = Move.W(matriz, x, y)
            MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 97): #a
        if(y != 0):
            y = Move.A(matriz, x, y)
            MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 115): #s
        if(x != 6):
            x = Move.S(matriz, x, y)
            MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 100): #d
        if(y != 6):
            y = Move.D(matriz, x, y)
            MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 63): #?
        Help()
        MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    elif(ord(c) == 102): #ff
        if (MenuAbandono.MenuAbandono()):
            enter = 2
        else:
            MontaMatriz(matriz, x, y, p1, p2, instrucoes)
            

    coordenadas = []
    coordenadas.append(x)
    coordenadas.append(y)
    coordenadas.append(enter)
    return coordenadas
                    
#################################  Selected  ###################################
def Selected (matriz, x, y, p1, p2, instrucoes): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    MontaMatriz(matriz, x, y, p1, p2, instrucoes)
    coordenadas = []
    coordenadas.append(x)
    coordenadas.append(y)
    coordenadas.append(0)
    while(coordenadas[2] == 0):
        c = Hit()
        coordenadas = MoveSelect(matriz, coordenadas[0], coordenadas[1], p1, p2, instrucoes, c, coordenadas[2])
    return (coordenadas)

#####################  Checa se há peças a serem movidas  #######################
def Block (matriz, p):
    for i in range (7):
        for j in range(7):
            if((matriz[i][j] == p)):
                if((CheckSeMove.W(matriz, i, j)) or (CheckSeMove.A(matriz, i, j)) or (CheckSeMove.S(matriz, i, j)) or (CheckSeMove.D(matriz, i, j))):
                    return(False)
    return(True)

##################################  Conta  ####################################
def conta(matriz, p):
    cont = 0
    for i in range (7):
        for j in range(7):
            if((matriz[i][j] == p)):
                cont +=1
    return cont

#############################  Checa se o jogador Venceu a partida  ###################################
def CheckSeVitoria(matriz,p)
    n = conta(matriz,p)

    if (n<3):
        if (p=="X"):
            p="O"
            Vitoria(p)
        else:
            p="X"
            Vitoria(p)

###############################  Conta Combo  ###################################
def combos (matriz, p):
    cont = 0
    for i in range (7):
        alinhadas = 0
        for j in range(7):
            if((matriz[i][j] == p)):
                alinhadas += 1
            elif((i == 3) and (j == 3)):
                if (alinhadas == 3):
                   cont += 1
                alinhadas  = 0
        if (alinhadas == 3):
            cont += 1
            
    for i in range (7):
        alinhadas = 0
        for j in range(7):
            if((matriz[j][i] == p)):
                alinhadas += 1
            elif((i == 3) and (j == 3)):
                if (alinhadas == 3):
                    cont += 1
                alinhadas  = 0
        if (alinhadas == 3):
            cont += 1
    return cont
###############################  Pode Retirar ##################################
def poderetirar (matriz, x, y, p):
    combo = 0

    #Faz combo?
    for i in range (7):
        if(matriz[i][y] == p):
            combo += 1
        if((i == 3) and (y ==3)):
            break
    if (combo != 3):
        combo = 0
        for i in range (7):
            if(matriz[x][i] == p):
                combo += 1
            if((i == 3) and (y ==3)):
                break
            
    #Faz! Tem outra fora de combo?
    if(combo == 3):
        for i in range(7):
            for j in range(7):
                for l in range (7):
                    if(matriz[l][j] == p):
                        combo += 1
                    if((i == 3) and (y ==3)):
                        break
                if (combo != 3):
                    combo = 0
                    for l in range (7):
                        if(matriz[i][l] == p):
                            combo += 1
                        if((i == 3) and (y ==3)):
                            break
                #Tem sim, tira essa não
                if(combo != 3):
                    return False
    #Faz não, pode tirar
    else:
        return True

    #Não tem nada fora de combo, como assim... tira essa peça então
    return True

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
    Posiciona.append("|        É a vez do jogador 1. Sua peça é 'X'. Escolha onde posiciona-la.       |\n|                                                                               |") 
    Posiciona.append("|        É a vez do jogador 2. Sua peça é 'O'. Escolha onde posiciona-la.       |\n|                                                                               |")
    coordenadas = []
    combo1 = 0
    combo2 = 0
    status = 0
    ### 1ª parte do jogo - posicionamento de peças
    for i in range (8, -1, -1):
        jogada_valida = 0
        if (status == 2):
            break
        ###jogada do P1 X
        while(jogada_valida == 0):
            coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[0])
            if (coordenadas[2] == 2):
                status = 2
                break
            if(matriz[coordenadas[0]][coordenadas[1]] == " "): #da pra colocar ali?
                matriz[coordenadas[0]][coordenadas[1]] = "X"
                jogada_valida = 1
                p1[i] = " " #tirou uma peça
            x = coordenadas[0]
            y = coordenadas[1]
            #Cheka o combo
            anterior = combo1
            combo1 = combos(matriz, 'X')
            if(anterior < combo1):
                retirou = 0
                while(retirou == 0):
                    coordenadas = Selected (matriz, x, y, p1, p2, '|      Boa! Você pontuou! Agora escolha uma peça do jogador 2 para retirar      |')
                    if((matriz[coordenadas[0]][coordenadas[1]] == 'O') and (poderetirar (matriz, coordenadas[0], coordenadas[1], 'O'))):
                        matriz[coordenadas[0]][coordenadas[1]] = ' '
                        retirou += 1
                    x = coordenadas[0]
                    y = coordenadas[1]
        jogada_valida = 0
        if (status == 2):
            break
        ###Jogada do P2 O
        while(jogada_valida == 0): 
            coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[1])
            if (coordenadas[2] == 2):
                status = 2
                break
            if(matriz[coordenadas[0]][coordenadas[1]] == " "):
                matriz[coordenadas[0]][coordenadas[1]] = "O"
                jogada_valida = 1
                p2[i] = " "
            x = coordenadas[0]
            y = coordenadas[1]
            #Cheka o combo
            anterior = combo2
            combo2 = combos(matriz, 'O')
            if(anterior < combo2):
                retirou = 0
                while(retirou == 0):
                    coordenadas = Selected (matriz, x, y, p1, p2, '|      Boa! Você pontuou! Agora escolha uma peça do jogador 1 para retirar      |')
                    if((matriz[coordenadas[0]][coordenadas[1]] == 'X') and (poderetirar (matriz, coordenadas[0], coordenadas[1], 'X'))):
                        matriz[coordenadas[0]][coordenadas[1]] = ' '
                        retirou += 1
                    x = coordenadas[0]
                    y = coordenadas[1]
                
    MontaMatriz(matriz, x, y, p1, p2, 'cabo')



    ### 2ª parte do jogo - movimentação de peças

    Posiciona[0] = "|       É a vez do jogador 1. Sua peça é 'X'. Escolha qual deseja mover.        |\n|                                                                               |"
    Posiciona[1] = "|       É a vez do jogador 2. Sua peça é 'O'. Escolha qual deseja mover.        |\n|                                                                               |"
    selecionada = "|                 Peça selecioanada! Escolha para onde movê-la.                 |\n|                       Use 'C' para cancelar a seleção.                        |"
    kb = Kbhit.KBHit()
    while (status == 0):
        c = 'a'
        jogada_valida = 0
        ###jogada do P1 X
        if(Block(matriz, "X")):
            status = 2
            break
        else:
            while(jogada_valida == 0):
                coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[0])
                if (coordenadas[2] == 2):
                    jogada_valida == 1
                    status = 2
                    break
                x = coordenadas[0]
                y = coordenadas[1]
                if(matriz[coordenadas[0]][coordenadas[1]] == "X"): #da pra mover?
                    if(conta(matriz, 'X') > 3):
                        if((CheckSeMove.W(matriz, x, y)) or (CheckSeMove.A(matriz, x, y)) or (CheckSeMove.S(matriz, x, y)) or (CheckSeMove.D(matriz, x, y))):
                            MontaMatriz(matriz, x, y, p1, p2, selecionada)
                            while(jogada_valida == 0):
                                c = Hit()
                                #W
                                if((ord(c) == 119) and (CheckSeMove.W(matriz, x, y))):
                                    matriz[x][y] = " "
                                    x = Move.W(matriz, x, y)
                                    matriz[x][y] = "X"
                                    jogada_valida = 1
                                #A
                                elif((ord(c) == 97) and (CheckSeMove.A(matriz, x, y))):
                                    matriz[x][y] = " "
                                    y = Move.A(matriz, x, y)
                                    matriz[x][y] = "X"
                                    jogada_valida = 1
                                #S
                                elif((ord(c) == 115) and (CheckSeMove.S(matriz, x, y))):
                                    matriz[x][y] = " "
                                    x = Move.S(matriz, x, y)
                                    matriz[x][y] = "X"
                                    jogada_valida = 1
                                #D
                                elif((ord(c) == 100) and (CheckSeMove.D(matriz, x, y))):
                                    matriz[x][y] = " "
                                    y = Move.D(matriz, x, y)
                                    matriz[x][y] = "X"
                                    jogada_valida = 1
                                elif(ord(c) == 63): #?
                                    Help()
                                    MontaMatriz(matriz, x, y, p1, p2, instrucoes)
                                elif(ord(c) == 102): #ff
                                    if (MenuAbandono.MenuAbandono()):
                                        status = 2
                                        jogada_valida = 2
                                        break
                                    else:
                                        MontaMatriz(matriz, x, y, p1, p2, instrucoes)
                                elif(ord(c) == 99):
                                    break
                            anterior = combo1
                            combo1 = combos(matriz, 'X')
                            if(anterior < combo1):
                                retirou = 0
                                while(retirou == 0):
                                    coordenadas = Selected (matriz, x, y, p1, p2, '|      Boa! Você pontuou! Agora escolha uma peça do jogador 2 para retirar      |')
                                    if((matriz[coordenadas[0]][coordenadas[1]] == 'O') and (poderetirar (matriz, coordenadas[0], coordenadas[1], 'O'))):
                                        matriz[coordenadas[0]][coordenadas[1]] = ' '
                                        retirou += 1
                                    x = coordenadas[0]
                                    y = coordenadas[1]
                                       
                                
                            
        if(ord(c) == 99):
            break
        jogada_valida = 0
        ###Jogada do P2 O
        if(Block(matriz, "O") and (status == 0)):
            status = 1
            break
        elif(status == 0):
            while(jogada_valida == 0):
                coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[1])
                if (coordenadas[2] == 2):
                    jogada_valida == 1
                    status = 2
                    break
                x = coordenadas[0]
                y = coordenadas[1]
                if(matriz[coordenadas[0]][coordenadas[1]] == "O"): #da pra mover?
                    if(conta(matriz, 'O') > 3):
                        if((CheckSeMove.W(matriz, x, y)) or (CheckSeMove.A(matriz, x, y)) or (CheckSeMove.S(matriz, x, y)) or (CheckSeMove.D(matriz, x, y))):
                            MontaMatriz(matriz, x, y, p1, p2, selecionada)
                            while(jogada_valida == 0):
                                c = Hit()
                                #W
                                if((ord(c) == 119) and (CheckSeMove.W(matriz, x, y))):
                                    matriz[x][y] = " "
                                    x = Move.W(matriz, x, y)
                                    matriz[x][y] = "O"
                                    jogada_valida = 1
                                #A
                                elif((ord(c) == 97) and (CheckSeMove.A(matriz, x, y))):
                                    matriz[x][y] = " "
                                    y = Move.A(matriz, x, y)
                                    matriz[x][y] = "O"
                                    jogada_valida = 1
                                #S
                                elif((ord(c) == 115) and (CheckSeMove.S(matriz, x, y))):
                                    matriz[x][y] = " "
                                    x = Move.S(matriz, x, y)
                                    matriz[x][y] = "O"
                                    jogada_valida = 1
                                #D
                                elif((ord(c) == 100) and (CheckSeMove.D(matriz, x, y))):
                                    matriz[x][y] = " "
                                    y = Move.D(matriz, x, y)
                                    matriz[x][y] = "O"
                                    jogada_valida = 1
                                elif(ord(c) == 63): #?
                                    Help()
                                    MontaMatriz(matriz, x, y, p1, p2, instrucoes)
                                elif(ord(c) == 102): #ff
                                    if (MenuAbandono.MenuAbandono()):
                                        status = 2
                                        jogada_valida = 2
                                        break
                                    else:
                                        MontaMatriz(matriz, x, y, p1, p2, instrucoes)
                                elif(ord(c) == 99):
                                    break
                            anterior = combo2
                            combo2 = combos(matriz, 'O')
                            if(anterior < combo2):
                                retirou = 0
                                while(retirou == 0):
                                    coordenadas = Selected (matriz, x, y, p1, p2, '|      Boa! Você pontuou! Agora escolha uma peça do jogador 1 para retirar      |')
                                    if(matriz[coordenadas[0]][coordenadas[1]] == 'X' and (poderetirar (matriz, coordenadas[0], coordenadas[1], 'O'))):
                                        matriz[coordenadas[0]][coordenadas[1]] = ' '
                                        retirou += 1
                                    x = coordenadas[0]
                                    y = coordenadas[1]




                                
