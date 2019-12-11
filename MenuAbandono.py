#######################  Comandos Sistema Operacional  #########################
import os
import Kbhit

####################################### Menu ###################################

def MenuAbandono():
    vetor_menu_abandono = []
    vetor_menu_abandono.append ('Não')
    vetor_menu_abandono.append ('Sim')
    x = 0
    coordenadas_abandono = SelectedMenuAbandono(vetor_menu_abandono, x)
    
    if (coordenadas_abandono == 1):
        return True
    else:
        return False

#################################### Monta Menu Abandono################################
def MontaMenuAbandono(vetor_menu_abandono, x):
    print_vetor_menu_abandono = []
    for i in range (4):
            print_vetor_menu_abandono.append(" ")
            
    for i in range (2):
        if (i == x):
            print_vetor_menu_abandono[i] = ">" + vetor_menu_abandono[i] + "<"
        else:
            print_vetor_menu_abandono[i] = " " + vetor_menu_abandono[i] + " "
    PrintMenuAbandono(print_vetor_menu_abandono)

#################################### Print Menu Abandono ################################
def PrintMenuAbandono (print_vetor_menu_abandono):
    if (os.name == 'nt'):
        os.system('cls')
    else:	
        os.system('clear')

    print("|-------------------------------------------------------------------------------|")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                  Tem certeza que deseja abandonar a partida?                  |")
    print("|                 Você não poderá mais retomá-la da onde parou.                 |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                    ", print_vetor_menu_abandono[0], "                                    |")
    print("|                                    ", print_vetor_menu_abandono[1], "                                    |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|               Use 'W','S', para mover, 'ESPAÇO' para confirmar.               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|-------------------------------------------------------------------------------|")

    ##############################  Move seta Menu Abandono  ################################
def MoveMenuAbandono(vetor_menu_abandono, x, c, enter):
    if (ord(c) == 32): #espaço -> enter
        if(x == 1): #Sim
            enter = 1

        elif(x == 0): #Não
            enter = 2

    elif(ord(c) == 119): #w
        if(x != 0):
            x -= 1
            MontaMenuAbandono(vetor_menu_abandono, x)
    elif(ord(c) == 115): #s
        if(x != 1):
            x += 1
            MontaMenuAbandono(vetor_menu_abandono, x)
    
    return (x,enter)
            
##############################  Selected Menu Abandono  #################################
def SelectedMenuAbandono (vetor_menu_abandono, x): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    kb = Kbhit.KBHit()
    MontaMenuAbandono(vetor_menu_abandono, x)

    hit = 0
    enter = 0
    
    z = 0
    if(os.name == 'nt'):
        while (z == 0):
            if kb.kbhit():
                c = kb.getch()
                x,z = MoveMenuAbandono(vetor_menu_abandono, x, c, z)
                
    else:
        while (z == 0):
            c = getkey()
            x,z = MoveMenuAbandono(vetor_menu_abandono, x, c, z)
            
    return x

