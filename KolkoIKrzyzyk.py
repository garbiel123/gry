import os
from colorama import Fore, Back
import random 

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def screenXO(screen):
    os.system('cls')

    
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    size = len(screen)                  #rozmiar ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        
        for j in row:
            if(j>0): printGreen(" X ")
            elif j<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")
    
    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")

    

def check_win(board, player):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or \
                board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Sprawdzanie wygranej na przekątnych
    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

if __name__ == "__main__":
    rozmiar = 3
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)
    
    
   

    gracz = 1
    board = [[0 for _ in range(3)] for _ in range(3)]
    current_player = 1

    while True:
        screenXO(board)
        row = int(input("Wybierz numer wiersza (0-2): "))
        col = int(input("Wybierz numer kolumny (0-2): "))
        
        if col < 2 and row < 2 and board[row][col] != 0:
                
                print("To pole jest już zajęte. Spróbuj ponownie.")
        elif col > 2 or row > 2:
                print("Zbyt wysoka liczba. Spróbuj ponownie.")
        else :
                
                print("To pole jest już zajęte. Spróbuj ponownie.")

        while col > 2 or row > 2 or board[row][col] != 0:
            
            row = int(input("Wybierz numer wiersza (0-2): "))
            col = int(input("Wybierz numer kolumny (0-2): "))
            
            if col < 2 and row < 2 and board[row][col] != 0:
                
                print("To pole jest już zajęte. Spróbuj ponownie.")
            elif col > 2 or row > 2:
                print("Zbyt wysoka liczba. Spróbuj ponownie.")
            
            
        board[row][col] = current_player

        if check_win(board, current_player):
            screenXO(board)
            print("Gracz", current_player, "wygrywa!")
            break

        
        if all(board[i][j] != 0 for i in range(3) for j in range(3)):
            screenXO(board)
            print("Remis!")
            break

        
        current_player = -1 if current_player == 1 else 1 



