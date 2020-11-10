"""
Ruleta
@author: Kevin Santiago Tocora Bermudez
email: kevintocora_3d@hotmail.com
"""

from random import randint

def roulete_Available(select_Roulete):
    roulete = [randint(0,1), randint(0,1), randint(0,1)]
    print(roulete[select_Roulete-1])
    print(roulete)
    if roulete[select_Roulete-1] == 1:
        return True
    else:
        return False
    
def color_number(number):
    color = ""    
    if number_random%2 == 0:
        color = "Rojo"
    else:
        color = "Negro"
    return color
    
while(True):  
    select_Roulete=int(input("""Escoga la ruleta para jugar: 
                             1)Ruleta(1)
                             2)Ruleta(2) 
                             3)Ruleta(3)
                             """ ))   
    if roulete_Available(select_Roulete) == True:
        print("Ruleta Disponible")
        break
    else:
        print("Ruleta No Disponible")
users = []
users.append(input("Ingrese El Nombre: ")) 
users.append(input("Ingrese Su Numero de Identificación: "))
while(True): 
    money = int (input("Ingrese el valor apostar: "))
    if money <= 10000:
        users.append(money) 
        break
    else:
        print("Valor no permitido")        
out = 0
while(out != 1 and money > 0):
    game = 0
    while(True):
        Type_bet = int(input("""Escoga el modo de juego 
                                1)Numero
                                2)Color """)) 
        if Type_bet == 1 or Type_bet == 2:
            game = Type_bet
            break
        else:
            print("Ingrese un modo de juego valido")    
    number = 0
    bet_color = ""
    choose_color = ""
    if Type_bet == 1:
        while(True):
            enter_number = int(input("Ingrese un numero del 1 al 36 para jugar: "))
            if enter_number >= 1 or enter_number <= 36:
                number = enter_number
                bet_color = color_number(number)
                break
            else:
                print("Ingrese un numero valido")
    elif Type_bet == 2:
        while(True):
            choose = int(input("""Ingrese el color:
                                    1) Rojo(Numero Par)
                                    2) Negro(Numero Impar)"""))
            if choose == 1:
                choose_color = "Rojo"
                break
            elif choose == 2:
                choose_color = "Negro"
                break
            else:
                print("Color escogido invalido")       
    random_color = ""        
    number_random = 0      
    for i in range(5):
        number_random = randint(1,36)
        random_color = color_number(random_color) 
    gain = [5,1.8]
    if random_color == choose_color or number_random == number:
        money =  money*gain[Type_bet-1]
        print("Ganador")
        print("Usuario " + users[0] + " Nuevo Saldo: " + str(money))
    else:
        print("Perdedor")
        print("Nuevo Saldo: 0.000")
        break       
    continue_ = int(input("""¿Desea continuar?
                             1) Si
                             2) No """))
    if continue_ == 2:
        out = 1      

    
    
        










        