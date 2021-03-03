# import tkinter as tk
# Import module  
from tkinter import *

# CONSTANTS
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600

CELL_EMPTY = 0
CELL_WALL = 1
CELL_EXIT = 2
CELL_COIN = 3
CELL_BOMB = 4
CELL_PLAYER = 5
CELL_WORM = 6

score = 0
game_over = False

# VARIABLES
map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,5,0,1,3,0,0,1,3,0,0,0,0,0,0,0,0,0,3,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1],
    [1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,4,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,6,0,0,0,0,0,0,0,0,0,4,1,3,0,0,1,0,0,1],
    [1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,3,4,1,0,0,1,3,3,1,3,4,3,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,3,0,1],
    [1,0,0,1,0,0,0,3,1,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,3,0,1,0,0,0,0,3,0,0,0,0,3,0,0,1,0,0,1],
    [1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
]


# def getWormPosition():
#     global map
#     playerRow = -1
#     playerColumn = -1


#     for rowIndex in range(len(map)) :
#         if 6 in map[rowIndex] :
#             playerRow = rowIndex
#     for columnIndex in range(len(map[playerRow])):
#         if map[playerRow][columnIndex] == 5 :
#             playerColumn = columnIndex

#     # TODO
#     return  [playerRow, playerColumn]


# def wormGreen_move():
#     global map,game_over
#     if not game_over :

        


def getPlayerPosition():
    global map
    playerRow = -1
    playerColumn = -1


    for rowIndex in range(len(map)) :
        if 5 in map[rowIndex] :
            playerRow = rowIndex
    for columnIndex in range(len(map[playerRow])):
        if map[playerRow][columnIndex] == 5 :
            playerColumn = columnIndex

    # TODO
    return  [playerRow, playerColumn]


def canGo(cell):
    global score,game_over
    if cell == CELL_EMPTY :
        result = True
    elif cell == CELL_WALL :
        result = False
    elif cell == CELL_EXIT :
        result = True
    elif cell == CELL_COIN :
        score += 10
        result = True
    elif cell == CELL_BOMB :
        score -= 15
        result = True
    elif cell == CELL_WORM :
        result = True


    return result


def canGoRight():
    global map
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]
    
    rightCell = map[playerRow][playerColumn + 1]
    
    result = canGo(rightCell)

    return result


def canGoLeft():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    leftCell = map[playerRow][playerColumn - 1]
    result = canGo(leftCell)

    return result


def canGoUp():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    upCell = map[playerRow - 1][playerColumn]
    result = canGo(upCell)

    return result


def canGoDown():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    downCell = map[playerRow + 1][playerColumn]
    result = canGo(downCell)
    return result


def clickOnRigh(event):
    global map,game_over
    if canGoRight() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        # find worm cell
        if map[playerRow][playerColumn+1] == CELL_WORM :
            game_over = True

        map[playerRow][playerColumn+1] = 5
        map[playerRow][playerColumn] = 0
        
        # drawMap()
        game()


def clickOnLeft(event):
    global map,game_over
    if canGoLeft() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        # find worm
        if map[playerRow][playerColumn-1] == CELL_WORM :
            game_over = True

        map[playerRow][playerColumn-1] = 5
        map[playerRow][playerColumn] = 0
        
        # drawMap()
        game()
        
def clickOnUp(event):
    global map,game_over
    if canGoUp() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        # find worm
        if map[playerRow-1][playerColumn] == CELL_WORM :
            game_over = True

        map[playerRow-1][playerColumn] = 5
        map[playerRow][playerColumn] = 0
        
        # drawMap()  
        game()    


def clickOnDown(event):
    global map,game_over
    if canGoDown() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        # find worm
        if map[playerRow+1][playerColumn] == CELL_WORM :
            game_over = True

        map[playerRow+1][playerColumn] = 5
        map[playerRow][playerColumn] = 0
        
        # drawMap()
        game()


def game() :
    global game_over
    if game_over :
        drawMap()
        canvas.create_text(300,300,fill="darkblue",font="Times 40 italic bold",text="GAME OVER")
        # Create a Button
        btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy) 
 
        # Set the position of button on the top of window.   
        btn.pack()  
    else: 
        return drawMap()


def drawMap():
    canvas.delete("all")
    global map,score
    size = 30

    x = 15
    y = 15


    for array in map:
        for value in array:
            
            
            if value == CELL_WALL :
                canvas.create_image(x,y, image=wall)

            elif value == CELL_EXIT :
                canvas.create_image(x,y, image=exit)
           
            elif  value == CELL_COIN :
                canvas.create_image(x,y, image=coin)
           
            elif value == CELL_BOMB :
                canvas.create_image(x,y, image=bomb)

            elif value == CELL_PLAYER :
                canvas.create_image(x,y, image=player)
            
            elif value == CELL_WORM :
                canvas.create_image(x,y, image=worm)
        
            x += size
            
        x = 15
        y += size

    canvas.create_text(300,555,fill="darkblue",font="Times 20 italic bold",text="Your Score")
    canvas.create_text(300,580,fill="darkblue",font="Times 20 italic bold",text=score)


# Create an empty window

  
# Create object  
root = Tk() 
root.geometry( str(WINDOWS_WIDTH) +"x" + str(WINDOWS_HEIGHT))
canvas = Canvas(root)
 
# Image
wall = PhotoImage(file="boxCrate_double.png")
coin = PhotoImage(file="gold_1.png")
bomb = PhotoImage(file="bomb.png")
player = PhotoImage(file="femaleAdventurer_walk1.png")
exit = PhotoImage(file="signExit.png")
worm = PhotoImage(file="wormGreen_move.png")

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Click
root.bind("<Right>",clickOnRigh)
root.bind("<Left>",clickOnLeft)
root.bind("<Up>",clickOnUp)
root.bind("<Down>",clickOnDown)

# Draw 
drawMap()

# Display all
root.mainloop()