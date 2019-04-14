"""
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: April 13, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 6 Disjoint Set Forests
TA: Anindita Nath & Maliheh Zaragan
Purpose: to implement both standard union and compression techniques
to use a disjoint set forest to build a maze.
"""

#Imports various tools to help us calculate the hash tables to be used in this lab
import matplotlib.pyplot as plt
import numpy as np
import random
import time

#Method that creates a Disjoint Set Forest
def DisjointSetForest(size):
    return np.zeros ( size, dtype=np.int ) - 1
    
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def totalSets(S):
    # Gets the total number of sets
    setNum = 0
    #For i in range of the length of S, setNum is added by 1
    for i in range(len(S)):
        if S[i] < 0: 
            setNum += 1
    #Returns setNum
    return setNum


def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])


def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r


def wallList(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze called w
    w = []
    #For i and c in range of the rows and columns
    for r in range(maze_rows):
        for c in range(maze_cols):
            #C and r times the columns create the cell
            cell = c + r*maze_cols
            #If the value of c does not equal columns -1, it will append on column of cell + 1
            if c != maze_cols-1:
                w.append([cell, cell+1])
                #If the value of c does not equal rows -1, it will append on column of cell + columns
            if r != maze_rows-1:
                w.append([cell, cell+maze_cols])           
    #Returns w
    return w

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri


def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri


def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
            
#Method that sets the requirements to build a standard union maze
def su_maze():
    #Draws the initial maze with only the number of cells so that the user knows whicch was the total amount
    draw_maze(walls, rows, columns, cellNums=True)
    #While the total number of sets is greater than 1
    while totalSets(S) > 1:
        #Removes a random wall 
        remove_wall = random.randint(0,len(walls)-1)
        #If the walls in S from 0 does not equal to the walls in S from 1, then it will unite terms
        if find(S,(walls[remove_wall])[0]) != find(S, (walls[remove_wall])[1]):
            union(S,(walls[remove_wall])[0], (walls[remove_wall])[1])
            walls.pop(remove_wall)
            
#Method that sets the requirements to build a compression maze
def c_maze():
    #Draws the initial maze with only the number of cells so that the user knows whicch was the total amount
    draw_maze(walls, rows, columns, cellNums=True)
    #While the total number of sets is greater than 1
    while totalSets(S) > 1:
        #Removes a random wall 
        remove_wall = random.randint(0,len(walls)-1)
        #If the walls in S from 0 does not equal to the walls in S from 1, then it will unite by size
        if find_c(S,(walls[remove_wall])[0]) != find_c(S, (walls[remove_wall])[1]):
            union_by_size(S, (walls[remove_wall])[0], (walls[remove_wall])[1])
            walls.pop(remove_wall)
            

#Method that draws the maze from either union or compression methods
def draw_maze(walls, rows, columns, cellNums=False):
    # Plots the maze
    fig, ax = plt.subplots()
    #For i in walls
    for i in walls:
        # If the amount of i[1] - i[0] equals 1, it will create a vertical wall
        if i[1]-i[0] == 1:  
            x0 = (i[1] % columns)
            x1 = x0
            y0 = (i[1] // columns)
            y1 = y0 + 1
        # If the amount of i[1] - i[0] equals 1, it will create a horizontal wall
        else:
            x0 = (i[0] % columns)
            x1 = x0+1
            y0 = (i[1] // columns)
            y1 = y0
        #Used to plot the frame
        ax.plot([x0, x1], [y0, y1], linewidth=1, color='k')
    #Sets a new variable called sx and sy that ues the values of the rows and columns to plot the lines
    sx = columns
    sy = rows
    ax.plot([0, 0, sx, sx, 0], [0, sy, sy, 0, 0], linewidth=2, color='k')
    #If the number of cells is true
    if cellNums:
        #For r in range of the number of rows
        for r in range(rows):
            #For c in range of the number of columns
            for c in range(columns):
                #The value of cell increases by c plus r times the number of columns
                cell = c + r*columns
                ax.text((c+.5), (r+.5), str(cell), size=10,ha="center", va="center")
    #Sets the axis to be off
    ax.axis('off')
    #Sets the axis aspect ratio to 1
    ax.set_aspect(1.0)


#Sets the total number of rows and columns that the maze contains inside of the maze
rows = 10
columns = 15

#Creates a new disjoint set forest based on the number of columns and rows
S = DisjointSetForest(rows * columns)

#Finds the Number of sets defined in the maze 
Num_Of_Sets = totalSets(S)

#Finds the number of walls inside of the maze
walls = wallList(rows,columns)

#Asks the user to choose a binary search tree or hash table with chaining 
print("Welcome, please select the way you want to build the maze.")
print("1. Maze with standard union")
print("2. Maze with compression")
print()

#Sets a variable 'x' to be made for the input section of the program
x = int(input('Choice: '))
print()
sets = dsfToSetList(S)

#If the user selects 1, the program will build a maze using standard union
if x == 1:
    #Starts a timer to be used later for running time comparisons
    start1 = time.time()
    su_maze()
    #Draws the mazed made by standard union
    draw_maze(walls, rows, columns)
    elapsed_time_union = time.time() - start1
    #Prints the running time for the su_maze method
    print('Running time for building a maze using standard union is: ', elapsed_time_union)

#If the user selects 2, the program will build a maze using compression 
elif x == 2:
    #Starts a timer to be used later for running time comparisons
    start2 = time.time()
    c_maze()
    #Draws the mazed made by standard union
    draw_maze(walls, rows, columns)
    elapsed_time_compression = time.time() - start2
    #Prints the running time for the c_maze method
    print('Running time for building a maze using compression is:', elapsed_time_compression)
    
#If the user inputs anything other than 1 or two, the following error message will be displayed
else:
    print('Incorrect input! Try again.')