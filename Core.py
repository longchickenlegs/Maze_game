import os
import random
import msvcrt


def Grid_Maker(x, y, Empty_Point_Value):
    '''
    Creates a grid given x{int} and y{int} coordinates and places Empty_Point_Value{single char. str} as the empty values in the grid.
    The output is a dictionary of a grid made up with Empty_Point_Value strings as values and x,y coordinates as keys.
    '''
    Grid = {}
    for i in range(x):
        for j in range(y):
            Grid[(i, j)] = Empty_Point_Value
    return Grid


def Grid_Printer(Grid):
    '''
    Prints a given Grid{dict} after clearing the terminal.
    '''
    if os.name == 'nt':  # If windows.
        os.system('cls')
    else:  # If linux or others (assuming they are linux based).
        os.system('clear')
    y_max = list(Grid.keys())[-1][-1] + 1
    # the y axis is needed to know where to stop printing each line and to skip y times to start the next line.
    for i in range(0, len(list(Grid.values())), y_max):
        print(str(list(Grid.values())[i:(i + y_max)]).replace('[', '').replace(
            ',', '').replace(']', '').replace("'", '').replace(' ',''))


def Movement(Grid, Position_x, Position_y, trail):
    '''
    Places a head as string 'O' in Grid{dict} and allows for the movement of the head using wsad.
    Utilizes Grid_Printer
    Requires the current position of snake head x and y coordinates.
    The trail can be changed using trail{single char. str}.
    '''
    while True:
        Choice = msvcrt.getch()
        if str(Choice) == "b'd'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x, Position_y + 1)] = 'O'
            Position_y += 1
        if str(Choice) == "b'a'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x, Position_y - 1)] = 'O'
            Position_y -= 1
        if str(Choice) == "b's'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x + 1, Position_y)] = 'O'
            Position_x += 1
        if str(Choice) == "b'w'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x - 1, Position_y)] = 'O'
            Position_x -= 1
        Grid_Printer(Grid)


def Wall_Maker(Grid):
    '''
    Applies walls to Grid{dict} to be demolished later
    '''
    x_max = list(Grid.keys())[-1][0] + 1
    y_max = list(Grid.keys())[-1][1] + 1
    for i in range(x_max):
        for j in range(1, y_max, 2):
            Grid[(i, j)] = '│'
    for i in range(1, x_max, 2):
        for j in range(y_max):
            Grid[(i, j)] = '─'


def Start_End(Grid):
    '''
    Places strings S and E to indicate the start and end of a maze in places 0,0 and x_max, y_max of Grid{dict}.
    '''
    x_max = list(Grid.keys())[-1][0]
    y_max = list(Grid.keys())[-1][1]
    Grid[(0,0)] = 'S'
    Grid[(x_max,y_max)] = 'E'


def Maze_Maker(Grid):
    '''
    Creates a Maze given a Grid{dict}
    '''
    #-------------------In line functions--------------------#
    def Break(x,y):
        '''Destroys a wall given x,y coordinates'''
        Grid[(x,y)] = '.'
    def Check_X_amount(x,y):
        '''Checks the number of X's that are around the position with x,y coordinates. Will return an int of the number of said X's'''
        def To_See(x,y):
            '''Will output True if coordinates x,y show an X, False otherwise'''
            if Grid[(x,y)] == 'X':
                return True
            else:
                return False
        To_Return = 0
        # +-2 is placed due to the walls.
        if To_See(x+2,y):  # down
            To_Return += 1
        if To_See(x-2,y):  # up
            To_Return += 1
        if To_See(x,y+2):  # left
            To_Return += 1
        if To_See(x,y-2):  # right
            To_Return += 1
    #--------------------------------------------------------#
    #-----------------Establishing the start-----------------#
    Position = (0,0)
    coin = random.randrange(2)
    if coin == 0:
        Break(1,0)
        Position = (2,0)
    elif coin == 1:
        Break(0,1)
        Position = (0,2)
    #--------------------------------------------------------#
    coin = random.randrange(Check_X_amount)
    if coin == 0:
        Break(1,0)
        Position = (2,0)
    elif coin == 1:
        Break(0,1)
        Position = (0,2)
    elif coin == 2:
        Break(1,0)
        Position = (2,0)
    elif coin == 3:
        Break(0,1)
        Position = (0,2)


# It is best if x and y are odd numbers.
t = 'X'
x = 15
y = 81
G = Grid_Maker(x, y, t)
Wall_Maker(G)
Start_End(G)
Maze_Maker(G)
Grid_Printer(G)
# Movement(G, 0, 0, t)
