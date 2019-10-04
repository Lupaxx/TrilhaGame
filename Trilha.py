#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python



def MontaTabuleiro (matriz, p1, p2):
	#matriz 7x7
	#lugar de peça = 0x0 0x3 0x6 1x1 1x3 1x5 2x2 2x3 2x4 3x0 3x1 3x2 3x4 3x5 3x6 4x2 4x3 4x4 5x1 5x3 5x3 6x0 6x3 6x6
	print("            (",matriz[0][0], ")----------------(", matriz[0][3], ")----------------(", matriz[0][6], ")", sep="")
	print("             |                  |                  |")
	print("             |                  |                  |")
	print("             |    (", matriz[1][1], ")----------(", matriz[1][3], ")----------(", matriz[1][5], ")    |", sep="")
	print(" |-----|     |     |            |            |     |     |-----|", )
	print(" |  ", p1[0], "  |     |     |            |            |     |     |  ", p2[0], "  |", sep="")
	print(" |  ", p1[1], "  |     |     |    (", matriz[2][2], ")----(", matriz[2][3], ")----(", matriz[2][4], ")    |     |     |  ", p2[2], "  |", sep = "")
	for i in range (2,4):
		print(" |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
	
	print(" |  ", p1[4], "  |    (", matriz[3][0], ")---(", matriz[3][1], ")---(", matriz[3][2], ")           (", matriz[3][4], ")---(", matriz[3][5], ")---(", matriz[3][6], ")    |  ", p2[4], "  |", sep="")
	for i in range (5,7):
		print(" |  ", p1[i], "  |     |     |     |             |     |     |     |  ", p2[i], "  |", sep="")
	print(" |  ", p1[7], "  |     |     |    (", matriz[4][2], ")----(", matriz[4][3], ")----(", matriz[4][4], ")    |     |     |  ", p2[7], "  |", sep = "")
	print(" |  ", p1[8], "  |     |     |            |            |     |     |  ", p2[8], "  |", sep="")
	print(" |-----|     |     |            |            |     |     |-----|", )
	print("             |    (", matriz[5][1], ")----------(", matriz[5][3], ")----------(", matriz[5][5], ")    |", sep="")
	print("             |                  |                  |")
	print("             |                  |                  |")
	print("            (",matriz[6][0], ")----------------(", matriz[6][3], ")----------------(", matriz[6][6], ")", sep="")
	
def PrintMatriz(matriz):
	for i in range (len(matriz[0])):
		for j in range (len(matriz[0])):
			print(matriz[i][j], end = "")
		print("")
	
	
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
	MontaTabuleiro(matriz, p1, p2)
	#PrintMatriz(matriz)
	
main()
