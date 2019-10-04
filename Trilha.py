#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Jogo Trilha em Python



def MontaTabuleiro (matriz):
	#matriz 7x7
	#lugar de peça = 0x0 0x3 0x6 1x1 1x3 1x5 2x2 2x3 2x4 3x0 3x1 3x2 3x4 3x5 3x6 4x2 4x3 4x4 5x1 5x3 5x3 6x0 6x3 6x6
	print(matriz[0][0], "----------------", matriz[0][3], "----------------", matriz[0][6])
	for i in range (2):
		print(" |                    |                    |", )
	print(" |      ", matriz[1][1], "----------", matriz[1][3], "----------", matriz[1][5], "      |", sep = "")
	for i in range (2):
		print(" |       |            |            |       |", )
	print(" |       |    ", matriz[2][2], "----", matriz[2][3], "----", matriz[2][4], "    |       |", sep = "")
	for i in range (2):
		print(" |       |     |             |     |       |")
	print(matriz[3][0], "-----", matriz[3][1], "---", matriz[3][2], "           ", matriz[3][4], "---", matriz[3][5], "-----", matriz[3][6], sep ="")
	for i in range (2):
		print(" |       |     |             |     |       |")
	print(" |       |    ", matriz[4][2], "----", matriz[4][3], "----", matriz[4][4], "    |       |", sep = "")
	for i in range (2):
		print(" |       |            |            |       |", )
	print(" |      ", matriz[5][1], "----------", matriz[5][3], "----------", matriz[5][5], "      |", sep = "")
	for i in range (2):
		print(" |                    |                    |", )
	print(matriz[6][0], "----------------", matriz[6][3], "----------------", matriz[6][6])

def main():
	matriz = [" "]*7
	for i in range (7):
		matriz[i] = [" "]*7
	matriz[0][0] = "( )"
	matriz[0][3] = "( )"
	matriz[0][6] = "( )"
	matriz[1][1] = "( )"
	matriz[1][3] = "( )"
	matriz[1][5] = "( )"
	matriz[2][2] = "( )"
	matriz[2][3] = "( )"
	matriz[2][4] = "( )"
	matriz[3][0] = "( )"
	matriz[3][1] = "( )"
	matriz[3][2] = "( )"
	matriz[3][4] = "( )"
	matriz[3][5] = "( )"
	matriz[3][6] = "( )"
	matriz[6][0] = "( )"
	matriz[6][3] = "( )"
	matriz[6][6] = "( )"
	matriz[5][1] = "( )"
	matriz[5][3] = "( )"
	matriz[5][5] = "( )"
	matriz[4][2] = "( )"
	matriz[4][3] = "( )"
	matriz[4][4] = "( )"
	MontaTabuleiro(matriz)
	
main()
