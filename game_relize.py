import random
import os
feld = list(range(1,10))

def draw_feld(feld):
    for i in range(3):
        print ("|", feld[0+i*3], "|", feld[1+i*3], "|", feld[2+i*3], "|")
def draw_feld_end(n, feld):
    for i in range (9):
        if not feld [i] == n:
            feld [i]=" "
    for i in range(3):
        print ("|", feld[0+i*3], "|", feld[1+i*3], "|", feld[2+i*3], "|")

def move (name):
    ok=False
    while not ok:
        print ("Move "+name)
        print ("Type number from 1 to 9")
        player_move=input()
        try:
            player_move=int(player_move)
        except:
            os.system('cls')
            print ("Type number fron 1 to 9.")
            draw_feld(feld)
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(feld[player_move-1]) not in "XO"):
                feld[player_move-1] = name
                ok = True
            else:
                os.system('cls')
                print ("You are not allowed to do this move. Try again.")
                draw_feld(feld)
        else:
            os.system('cls')
            print ("Type number fron 1 to 9.")
            draw_feld(feld)

def win(feld):
    win_case = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for n in win_case:
        if feld[n[0]] == feld[n[1]] == feld[n[2]]:
            return feld[n[0]]
    return False

def main(feld):
    cnt = int(random.randint(0,20))%2
    wins = False
    while not wins:
        draw_feld(feld)
        if cnt%2== 0:
            move("X")
            draw_feld(feld)
        else:
            move("O")
            draw_feld (feld)
        cnt += 1
        os.system('cls')
        if cnt > 4:
            tmp = win(feld)
            if tmp:
                print (tmp, " won!")
                wins = True
                break
        if cnt == 9:
            print ("Draw!")
            break
    if wins:
        draw_feld_end (tmp, feld)
    else: draw_feld(feld)
main(feld)