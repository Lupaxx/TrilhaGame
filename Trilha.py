#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python

#######################  Comandos Sistema Operacional  #########################
import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import curses
    import sys
    import termios
    TERMIOS = termios
    import atexit
    from select import select
    def getkey():
        fd = sys.stdin.fileno()
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            return (str(c)[2])

class KBHit:

    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''
        
        if os.name == 'nt':
            pass
        
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)



    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        
        s = ''
        
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        
        else:
            return sys.stdin.read(1)
    

    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()
        
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []

#################################  Tutorial  ###################################
def Help():
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')
    print ('''    Tutorial:
                                       Descrição:                                   
    
    O jogo de Trilha tem dois participantes, que usam um tabuleiro para jogar.
    
    Jogadores - 2
    Peças - 18 peças sendo 9 brancas e 9 pretas.
    Tabuleiro - tabuleiro com 24 casa interligados horizontalmente e verticalmente.
    Objetivo - Deixar o adversário com 2 peças no tabuleiro ou deixá-lo sem movimentos.
    
                                     O Jogo Trilha:                                 
    
    O jogo consiste em tres partes principais:
    
        Colocando as peças: Esta é a fase inicial do jogo onde cada jogador coloca
    um peça de cada vez alternando entre jogadores, caso um dos jogadores forme uma
    linha horizontal ou vertical com três peças (um moinho), ele terá o direito de
    remover uma peça de seu adversário do tabuleiro.
        Movendo as peças: Esta fase se inicia quando ambos os jogadores colocarem
    suas nove peças em jogo. Consiste em mover suas peças ao longo de uma das linhas
    do tabuleiro para uma outra casa adjacente. Caso um dos jogadores tenha somente
    3 peças em jogo, ele pode "voar" com suas peças, podendo mover para qualquer
    casa que não esteja ocupada por uma peça do adversário.
        Removendo peças adversárias: Em qualquer uma das fases acima quando um
    jogador forma uma linha horizontal ou vertical com 3 peças ele fará um "moinho",
    isso lhe dá o direito de remover uma peça de seu adversário, contudo você não
    poderá remover uma peça do seu adversário que faz parte de um moinho dele, a não
    ser que não exista outra peça para remover.
    
                                      Estratégia:                                   
                                      
        No começo do jogo, é muito importante colocar as peças nos lugares mais
    versáteis para tentar formar imediatamente moinhos e não cometer o erro de
    concentrar as peças próprias em uma área do tabuleiro.
        Uma posição ideal, que geralmente resulta em uma vitória, é ser capaz de colocar
    uma peça que possa se movimentar entre dois moinhos diferentes. 
    
                                     Fim da Partida:                                 
                                     
    O jogo termina quando 3 situações são alcançadas:
    
        Se um jogador reduzir as peças de seu adversário para 2.
        Se um jogador deixar seu adversário sem nenhuma jogada válida. Caso seu
    adversário tenha somente 3 peças em jogo, ele não poderá ser "trancado".
        Se ambos jogadores estiverem com 3 peças em jogo e, a partir deste momento, se
    em 10 jogadas não houver vencedor, o jogo terminará e será declarado um empate.
    
    ****************** Use enter para voltar ao menu inicial. ******************''')
    input()
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')

###############################  Monta Matriz  #################################
def MontaMatriz(matriz, x, y, p1, p2): #Monta pra colocar no Tabuleiro
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
def Move(matriz, x, y, p1, p2, string, c, enter):
    if (ord(c) == 32): #espaço -> enter
        enter = 1
    elif(ord(c) == 119): #w
        if(x != 0):
            if(matriz[x-1][y] == "|"): #Distancia grande entre as casas
                posicionado = 0
                while(posicionado == 0):
                    x = x -1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")): #Tem que colocar x e o nesses if todo
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
            elif((matriz[x-1][y] == " ") or (matriz[x-1][y] == "X") or (matriz[x-1][y] == "O")):
                x = x -1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
    elif(ord(c) == 97): #a
        if(y != 0):
            if(matriz[x][y-1] == "-"):
                posicionado = 0
                while(posicionado == 0):
                    y = y -1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
            elif((matriz[x][y-1] == " ") or (matriz[x][y-1] == "X") or (matriz[x][y-1] == "O")):
                y = y -1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
    elif(ord(c) == 115): #s
        if(x != 6):
            if(matriz[x+1][y] == "|"):
                posicionado = 0
                while(posicionado == 0):
                    x += 1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
            elif((matriz[x+1][y] == " ") or (matriz[x+1][y] == "X") or (matriz[x+1][y] == "O")):
                x += 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
    elif(ord(c) == 100): #d
        if(y != 6):
            if(matriz[x][y+1] == "-"):
                posicionado = 0
                while(posicionado == 0):
                    y = y + 1
                    if((matriz[x][y] == " ") or (matriz[x][y] == "X") or (matriz[x][y] == "O")):
                        posicionado = 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
            elif((matriz[x][y+1] == " ") or (matriz[x][y+1] == "X") or (matriz[x][y+1] == "O")):
                y = y + 1
                MontaMatriz(matriz, x, y, p1, p2)
                print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
    elif(ord(c) == 63): #?
        Help()
        MontaMatriz(matriz, x, y, p1, p2)
        print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')
    coordenadas = []
    coordenadas.append(x)
    coordenadas.append(y)
    coordenadas.append(enter)
    return coordenadas
                    
#################################  Selected  ###################################
def Selected (matriz, x, y, p1, p2, string): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    if __name__ == "__main__":
        
        kb = KBHit()
        MontaMatriz(matriz, x, y, p1, p2)
        print(string, '\n     Use WASD para mover, espaço para confirmar e ? para tirar as duvidas.')

        hit = 0
        enter = 0
        
        coordenadas = []
        coordenadas.append(x)
        coordenadas.append(y)
        coordenadas.append(0)
        if(os.name == 'nt'):
            while (coordenadas[2] == 0):
                if os.name == 'nt':
                    if kb.kbhit():
                        c = kb.getch()
                        coordenadas = Move(matriz, coordenadas[0], coordenadas[1], p1, p2, string, c, coordenadas[2])
        else:
            while (coordenadas[2] == 0):
                c = getkey()
                coordenadas = Move(matriz, coordenadas[0], coordenadas[1], p1, p2, string, c, coordenadas[2])
                
        return coordenadas

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
    for i in range (9):
            p1.append("X")
            p2.append("O")

    
    Posiciona = []
    Posiciona.append("     É a vez do jogador 1. Sua peça é 'X'. Escolha onde posiciona-la.")
    Posiciona.append("     É a vez do jogador 2. Sua peça é 'O'. Escolha onde posiciona-la.")
        
    for i in range (8, -1, -1):
        jogada_valida = 0
        coordenadas = []
        while(jogada_valida == 0): #jogada do x
            coordenadas = Selected(matriz, x, y, p1, p2, Posiciona[0])
            if(matriz[coordenadas[0]][coordenadas[1]] == " "):
                matriz[coordenadas[0]][coordenadas[1]] = "X"
                jogada_valida = 1
                p1[i] = " "
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
                
    MontaMatriz(matriz, x, y, p1, p2)

###################################  Menu  #####################################

    

###############################  Chama Main  #################################
main()