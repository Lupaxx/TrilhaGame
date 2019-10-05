#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python
import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select

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
        
def PrintMatriz(matriz):
	for i in range (len(matriz[0])):
		for j in range (len(matriz[0])):
			print(matriz[i][j], end = "")
		print("")
        
def MontaTabuleiro (matriz, p1, p2):
	#matriz 7x7
	#lugar de peça = 0x0 0x3 0x6 1x1 1x3 1x5 2x2 2x3 2x4 3x0 3x1 3x2 3x4 3x5 3x6 4x2 4x3 4x4 5x1 5x3 5x3 6x0 6x3 6x6
	print("            ",matriz[0][0], "----------------", matriz[0][3], "----------------", matriz[0][6], "", sep="")
	print("             |                  |                  |")
	print("             |                  |                  |")
	print("             |    ", matriz[1][1], "----------", matriz[1][3], "----------", matriz[1][5], "    |", sep="")
	print(" |-----|     |     |            |            |     |     |-----|", )
	print(" |  ", p1[0], "  |     |     |            |            |     |     |  ", p2[0], "  |", sep="")
	print(" |  ", p1[1], "  |     |     |    ", matriz[2][2], "----", matriz[2][3], "----", matriz[2][4], "    |     |     |  ", p2[2], "  |", sep = "")
	for i in range (2,4):
		print(" |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
	print(" |  ", p1[4], "  |    ", matriz[3][0], "---", matriz[3][1], "---", matriz[3][2], "           ", matriz[3][4], "---", matriz[3][5], "---", matriz[3][6], "    |  ", p2[4], "  |", sep="")
	for i in range (5,7):
		print(" |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
	print(" |  ", p1[7], "  |     |     |    ", matriz[4][2], "----", matriz[4][3], "----", matriz[4][4], "    |     |     |  ", p2[7], "  |", sep = "")
	print(" |  ", p1[8], "  |     |     |            |            |     |     |  ", p2[8], "  |", sep="")
	print(" |-----|     |     |            |            |     |     |-----|", )
	print("             |    ", matriz[5][1], "----------", matriz[5][3], "----------", matriz[5][5], "    |", sep="")
	print("             |                  |                  |")
	print("             |                  |                  |")
	print("            ",matriz[6][0], "----------------", matriz[6][3], "----------------", matriz[6][6], "", sep="")


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
    #PrintMatriz(tabuleiro)
    MontaTabuleiro(tabuleiro, p1, p2)
            

def Selected (matriz, x, y, p1, p2):
    if __name__ == "__main__":
        
        kb = KBHit()

        print('Use WASD para mover')

        hit = 0
        enter = 0
        
        while (enter == 0):

            if kb.kbhit():
                c = kb.getch()
                if (ord(c) == 32): #espaço -> enter
                    enter = 1
                elif(ord(c) == 119): #w
                    if(x != 0):
                        if(matriz[x-1][y] == "|"):
                            posicionado = 0
                            while(posicionado == 0):
                                x = x -1
                                if(matriz[x][y] == " "): #Tem que colocar x e o nesses if todo
                                    posicionado = 1
                            MontaMatriz(matriz, x, y, p1, p2)
                        elif(matriz[x-1][y] == " "):
                            x = x -1
                            MontaMatriz(matriz, x, y, p1, p2)
                elif(ord(c) == 97): #a
                    if(y != 0):
                        if(matriz[x][y-1] == "-"):
                            posicionado = 0
                            while(posicionado == 0):
                                y = y -1
                                if(matriz[x][y] == " "):
                                    posicionado = 1
                            MontaMatriz(matriz, x, y, p1, p2)
                        elif(matriz[x][y - 1] == " "):
                            y = y -1
                            MontaMatriz(matriz, x, y, p1, p2)
                elif(ord(c) == 115): #s
                    if(y != 0):
                        if(matriz[x+1][y] == "|"):
                            posicionado = 0
                            while(posicionado == 0):
                                x += 1
                                if(matriz[x][y] == " "):
                                    posicionado = 1
                            MontaMatriz(matriz, x, y, p1, p2)
                        elif(matriz[x+1][y] == " "):
                            x += 1
                            MontaMatriz(matriz, x, y, p1, p2)
                elif(ord(c) == 100): #d
                    if(y != 0):
                        if(matriz[x][y+1] == "-"):
                            posicionado = 0
                            while(posicionado == 0):
                                y = y + 1
                                if(matriz[x][y] == " "):
                                    posicionado = 1
                            MontaMatriz(matriz, x, y, p1, p2)
                        elif(matriz[x][y+1] == " "):
                            y = y + 1
                            MontaMatriz(matriz, x, y, p1, p2)
                
                    #or (ord(c) == 97) or (ord(c) == 115) or (ord(c) ==100)): # WASD
                  
    
	
	
def main():
	matriz = [" "]*7
	p1 = []
	p2 = []
	for i in range (7):
		matriz[i] = [" "]*7
	
	for i in range (9):
	    p1.append("X")
	    p2.append("O")
	
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
	MontaMatriz(matriz, 2, 3, p1, p2)
	Selected(matriz, 2, 3, p1, p2)
	#MontaTabuleiro(matriz, p1, p2)
	#PrintMatriz(matriz)
	
main()
