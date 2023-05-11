import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr,path = []):
    BLUE = curses.color_pair(1)
    GREEN = curses.color_pair(2)
    #enumerate is used to get the index of the element
    for i, row  in enumerate(maze):
        for j, col in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i+3,j*2+3,'X',GREEN)
            else:
                stdscr.addstr(i+3, j*2+3, col , BLUE)

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j, col in enumerate(row):
            if col == start:
                return i,j
    return None

def find_path(maze,stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze,start)

    q = queue.Queue()

    q.put((start_pos , [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row,col = current_pos

        stdscr.clear() #clears the screen
        print_maze(maze, stdscr, path)#addstr is used to print a string at a particular location
        time.sleep(0.1)
        stdscr.refresh() #refreshes the screen
        
        if maze[row][col]  == end:
            return path

        neighbors = find_neighbors(maze , row , col) #Get all the neighbour direction
        for i in neighbors:
            if i in visited:
                continue
            r , c = i
            if maze[r][c] == "#":
                continue
            
            new_path = path + [i]
            q.put((i , new_path))
            visited.add(i)


        
def find_neighbors(maze,row,col):
    neighbors = [] 
    if row > 0 : #DOWN
        neighbors.append((row - 1 , col))
    if row + 1 < len(maze): #UP
        neighbors.append((row + 1 , col))
    if col > 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): #RIGHT
        neighbors.append((row , col + 1))

    return neighbors



#stdscr is used to control the terminal
def main(stdscr): 
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK) #init_pair is used to initialize a color pair
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)

    find_path(maze,stdscr)
    stdscr.getch() #getch is used to get a character from the keyboard


# wrapper is used to initialize curses and clean up curses
wrapper(main)