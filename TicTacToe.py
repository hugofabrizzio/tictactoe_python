import os
import time
##### INTRODUCTION #####
os.system('cls')
print("========= Let's play Tic-Tac-Toe. =========")
print("")
print("RULES:")
print("")
print("The first player is going to have the 'x'.")
print("The second player is going to have the 'o'.")
print("The player that has the turn can choose its place")
print("by typing the position that he/she want to choose.")
print("")
print("Here it is a map that you can follow to understand")
print("the order and numbers of the positions of the board.")
print("")
print(" 1 | 2 | 3 ")
print("------------")
print(" 4 | 5 | 6 ")
print("------------")
print(" 7 | 8 | 9 ")
print("")
input("So, press any key to start.")
os.system('cls')

def switch(position, shoot):
    if position == 1 :
        if M[0][0] == "x" or M[0][0] == "o":
            return True
        else : M[0][0] = shoot
    elif position == 2 :
        if M[0][1] == "x" or M[0][1] == "o":
            return True
        else : M[0][1] = shoot
    elif position == 3 :
        if M[0][2] == "x" or M[0][2] == "o":
            return True
        else : M[0][2] = shoot
    elif position == 4 :
        if M[1][0] == "x" or M[1][0] == "o":
            return True
        else : M[1][0] = shoot
    elif position == 5 :
        if M[1][1] == "x" or M[1][1] == "o":
            return True
        else : M[1][1] = shoot
    elif position == 6 :
        if M[1][2] == "x" or M[1][2] == "o":
            return True
        else : M[1][2] = shoot
    elif position == 7 :
        if M[2][0] == "x" or M[2][0] == "o":
            return True
        else : M[2][0] = shoot
    elif position == 8 :
        if M[2][1] == "x" or M[2][1] == "o":
            return True
        else : M[2][1] = shoot
    elif position == 9 :
        if M[2][2] == "x" or M[2][2] == "o":
            return True
        else : M[2][2] = shoot

def win(count):
    if count%2 == 1: print("CONGRATS X, you win!")
    else : print("CONGRATS O, you win!")

def tablero():
    print(" "+M[0][0]+" | "+M[0][1]+" | "+M[0][2]+" ")
    print("------------")
    print(" "+M[1][0]+" | "+M[1][1]+" | "+M[1][2]+" ")
    print("------------")
    print(" "+M[2][0]+" | "+M[2][1]+" | "+M[2][2]+" ")
    print("")

M = [["1","2","3"],["4","5","6"],["7","8","9"]]
#for i in M : print(i)

count = 0
while(True):
    
    os.system('cls')
    tablero()
    
    if M[0][0] == M[0][1] == M[0][2] : break
    elif M[1][0] == M[1][1] == M[1][2] : break
    elif M[2][0] == M[2][1] == M[2][2] : break
    elif M[0][0] == M[1][0] == M[2][0] : break
    elif M[0][1] == M[1][1] == M[2][1] : break
    elif M[0][2] == M[1][2] == M[2][2] : break
    elif M[0][0] == M[1][1] == M[2][2] : break
    
    count += 1
    
    if count%2 == 1: name = "x"
    else : name = "o"
    
    print("It's your turn "+name+".")
    try: tiro = int(input("Where would you like to shoot? "))
    except :
        count -= 1
        print("INCORRECT INPUT, TRY AGAIN!")
        time.sleep(3) #3 seconds
        continue
    if tiro < 10 or tiro > 0 :
        switch(tiro, name)
    else : 
        count -= 1
        print("INCORRECT INPUT, TRY AGAIN!")
        time.sleep(3) #3 seconds
        continue
    
    
    
win(count)
