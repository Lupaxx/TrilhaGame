#Autores: Luiza Pacheco, Victor assis, Alexandre Salem e Marco Gomes
#Data de inicio: 04/10/2019
#
#Descrição: Menu do Jogo Trilha em Python

#######################  Comandos Sistema Operacional  #########################
import os
import Kbhit
        
#################################  Tutorial  ###################################
def Help():
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')
    arquivo = open("tutorial.txt", "r", encoding='utf-8')
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
            c = kb.getkey()
            z = 1
    if os.name == 'nt':
        os.system('cls')
    else:	
        os.system('clear')

####################################### Menu ###################################

def Menu():
    vetor_menu = []
    vetor_menu.append ('Iniciar Jogo')
    vetor_menu.append ('Tutorial')
    vetor_menu.append ('Sair')
    x = 1
    coordenadas = SelectedMenu(vetor_menu, x)
    
#################################### Monta Menu ################################
def MontaMenu(vetor_menu, x):
    print_vetor_menu = []
    for i in range (9):
            print_vetor_menu.append(" ")
            
    for i in range (3):
        if (i == x):
            print_vetor_menu[i] = ">" + vetor_menu[i] + "<"
        else:
            print_vetor_menu[i] = " " + vetor_menu[i] + " "
    PrintMenu(print_vetor_menu)

#################################### Print Menu ################################
def PrintMenu (print_vetor_menu):
    if (os.name == 'nt'):
        os.system('cls')
    else:	
        os.system('clear')
        
    print ('''|-------------------------------------------------------------------------------|
|                                                                               |
|             ---|---  |---\   ---|---  |       |     |      /\                 |
|                |     |    |     |     |       |     |     /  \                |
|                |     |---/      |     |       |-----|    /    \               |
|                |     |  \       |     |       |     |   /------\              |
|                |     |   \   ---|---  |-----  |     |  /        \             |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |''')
    print("|                                 ", print_vetor_menu[0], "                                |", sep="")
    print("|                                   ", print_vetor_menu[1], "                                  |", sep="")
    print("|                                     ", print_vetor_menu[2], "                                    |", sep="")
    print('''|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|        Digite 'w' ou 's' para selelcionar e 'ESPAÇO' para confirmar.          |
|                                                                               |
|                                                                               |
|-------------------------------------------------------------------------------|''')

##############################  Move seta Menu  ################################
def MoveMenu(vetor_menu, x, c, enter):
    if (ord(c) == 32): #espaço -> enter
        if(x == 2):
            enter = "Sair"
        elif(x == 1):
            Help()
            MontaMenu(vetor_menu, x)
        elif(x == 0):
            import Trilha
            Trilha.main()
            MontaMenu(vetor_menu, x)
    elif(ord(c) == 119): #w
        if(x != 0):
            x -= 1
            MontaMenu(vetor_menu, x)
    elif(ord(c) == 115): #s
        if(x != 2):
            x += 1
            MontaMenu(vetor_menu, x)
    
    return (x,enter)
            
##############################  Selected Menu  #################################
def SelectedMenu (vetor_menu, x): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    if __name__ == "__main__":
        
        kb = Kbhit.KBHit()
        MontaMenu(vetor_menu, x)

        hit = 0
        enter = 0
        
        z = 0
        if(os.name == 'nt'):
            while (z == 0):
                if kb.kbhit():
                    c = kb.getch()
                    x,z = MoveMenu(vetor_menu, x, c, z)
        else:
            while (z == 0):
                c = kb.getkey()
                x,z = MoveMenu(vetor_menu, x, c, z)
                
        return x

################################  Chama menu  ##################################

Menu()
