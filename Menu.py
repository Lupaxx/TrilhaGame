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

####################################### Menu ###################################

def Menu():
    vetor_menu = []
    vetor_menu.append ('Iniciar Jogo')
    vetor_menu.append ('Tutorial')
    vetor_menu.append ('sair')
    x = 1
    coordenadas = SelectedMenu(vetor_menu, x)
    
    MoveMenu(vetor_menu, x, c, enter)
#################################### Monta Menu ################################
def MontaMenu(vetor_menu, x):
    print_vetor_menu = []
    for i in range (9):
            print_vetor_menu.append(" ")
            
    for i in range (3):
        if (i == x):
            print_vetor_menu[i] = ">" + vetor_menu[i] + "<"
        else:
            print_vetor_menu[i] = " " + vetor_menu[i]
    PrintMenu(print_vetor_menu)

#################################### Print Menu ################################
def PrintMenu (print_vetor_menu):
    if (os.name == 'nt'):
        os.system('cls')
    else:	
        os.system('clear')
        
    print ('''
            ---|---  |---\   ---|---  |       |     |      /\ 
               |     |    |     |     |       |     |     /  \ 
               |     |---/      |     |       |-----|    /    \ 
               |     |  \       |     |       |     |   /------\ 
               |     |   \   ---|---  |-----  |     |  /        \ ''')
    print('\n\n\n\n                               ', print_vetor_menu[0])
    print('                                 ', print_vetor_menu[1])
    print('                                   ', print_vetor_menu[2])
    print("\n\n\n\n\n\tDigite 'w' ou 's' para selelcionar e 'espaço' para confirmar.")

##############################  Move seta Menu  ################################
def MoveMenu(vetor_menu, x, c, enter):
    if (ord(c) == 32): #espaço -> enter
        enter = 1
    elif(ord(c) == 119): #w
        if(x != 0):
            x -= 1
            MontaMenu(vetor_menu, x)
    elif(ord(c) == 115): #s
        if(x != 2):
            x += 1
            MontaMenu(vetor_menu, x)
    
    return x
            
##############################  Selected Menu  #################################
def SelectedMenu (vetor_menu, x): #Responde ao input, seleciona um lugar do tabuleiro e retorna as coordenadas desse lugar
    if __name__ == "__main__":
        
        kb = KBHit()
        MontaMenu(vetor_menu, x)

        hit = 0
        enter = 0
        
        z=0
        if(os.name == 'nt'):
            while (z == 0):
                if os.name == 'nt':
                    if kb.kbhit():
                        c = kb.getch()
                        x = MoveMenu(vetor_menu, x, c, z)
        else:
            while (z == 0):
                c = getkey()
                x = MoveMenu(vetor_menu, x, c, z)
                
        return x

################################  Chama menu  ##################################

Menu()
