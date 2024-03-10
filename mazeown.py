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
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
#stdscr to print the maze to
#path to draw on maze
def print_maze( maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED= curses.color_pair(2)
    for i, row in enumerate(maze):
        #enumarate-returns index as well as the value
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(1, j*2, "X", RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)
                
                

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value == start:
                return i,j
    return None
    

def find_path(maze,stdscr):
    start="O"
    end="X"
    start_pos=find_start(maze,start)
    
    q=queue.Queue()
    #fifo dsa
    q.put((start_pos,[start_pos]))#tuple having staring pos and a list, two elemlnts, as current position of node & path to get to the node , path incraeses weach time
    
    visited= set()
    while not q.empty():
        #get-remove and return an item fromqueue
        current_pos, path = q.get()
        row,col= current_pos
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.3)
        stdscr.refresh()
    #refresh and see what we wrote
        if maze[row][col] == end:
            return path
        
        neighbours=find_neighbours(maze,row,col)
        for n in neighbours:
            if n in visited:
                continue
            r, c= n
            if maze[r][c]== "#":
                continue
            new_path=path+[n]
            q.put((n,new_path))
            visited.add(n)
            
            
def find_neighbours(maze,row,col):
    neighbours= []
    if row > 0 : #UP
        neighbours.append((row-1,col))
    
    if row +1 < len(maze): #DOWN
        neighbours.append((row+1,col))
    if col > 0:
        neighbours.append((row,col-1))
    if col + 1 < len(maze[0]):
        neighbours.append((row,col+1))
        
    return neighbours
    
#stdscr-add stuff to the scrren adnd voerride the terminal 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED,curses.COLOR_BLACK)
    find_path(maze,stdscr)
    stdscr.getch()
    #gtch-wait till user inputs somthg to exit program
wrapper(main)

