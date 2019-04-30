"""
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: April 29, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 7 Modified Maze
TA: Anindita Nath & Maliheh Zaragan
Purpose: to implement both standard union and compression techniques
as well as new techniques to modify the maze program to create a new
solution for that specififcally maze.
"""
#Imports various tools to help us calculate the hash tables to be used in this lab
import time
import matplotlib.pyplot as plt
import numpy as np
import random

#Makes a new class that will create the functions necessary to make a graoh
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = []
        for v in range(vertices):
            self.graph.append([])
     
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

  
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

#Method that creates a Disjoint Set Forest
def DisjointSetForest(size):
    return np.zeros ( size, dtype=np.int ) - 1
        
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

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
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


#Method that finds the number of cells contained in the maze
def cells_number(S):
    count = 0
    #If S is none, then it returns 0
    if S is None:
        return 0
    #Else, it will use a for loop to count the number of cells
    for i in S:
        count+=1
        #Returns the number of cells labeled count
    return count


#Method that where n displays the number of cells and m is the amount of walls the user wants to remove
def cells_display(n,m):
    #While m is less than n minus 1
    if m < n-1:
        print('A Path from source to destination is not guranteed to exist')
    #While m is equal to n minus 1
    elif m == n-1:
        print('There is a unique path from source to destination')
    #While m is greater than n minus 1
    elif m > n-1:
        print('There is at least one path from the source to destination')
        
#method to use depth First Search using a stack to answer question 3
def dfsStack(adjList, initialNode):
    #Creates a new list that will add the visited nodes
    visitedNode = []
    #Creates the stack from the initial Node
    stack = [initialNode]
    #While Stack is True
    while stack:
        #Sest Inititial Node to pop
        initialNode = stack.pop()
        #Adds the visited node to the new list
        visitedNode.append(initialNode)
        #Prints the current node 
        print(initialNode,end=" ")
        #For i in the adjacency list started from intitial node
        for i in adjList.graph[initialNode]:
            #Append to to the stack
            stack.append(i)
    #Returns the list visitedNode
    return visitedNode
        
#Method to use depth First Search with recursion to answer question 3
def dfsRecursion(adjList,startNode, visited = None):
    #If the visited none is None, it will create a new list called visited 
    if visited is None:
        visitedNode = []
    #Appends startNode to list visited
    visitedNode.append(startNode)
    #For i in the adjacency list
    for i in adjList.graph[startNode]:
        #If i has not been visisted, recaals itslef recursively until visisted
        if i not in visitedNode:
            dfsRecursion(adjList,i,visited)
    #Returns the list visited
    return visitedNode

#Method that creates the adjacency List and applies it to this lab better unlike the graph
def addEdge(G,v1,v2):
    G.graph[v1].append(v2)

#Method to use Breadth First Search used for Question 3
def breadth_first_search(adjList,v):
    #Checks if it has visited that cell
    visit_check = [False]*(len(adjList.graph))
    #Creates a new list called K
    K=[]
    #Adds the item v to list K
    K.append(v)
    #Changes the visted check to True
    visit_check[v] = True
    #While K is true
    while K:
        #Pops item 0 from K to v
        v = K.pop(0)
        #Prints the vector v
        print(v,end=" ")
        #FOr i in adjacency list 
        for i in adjList.graph[v]:
            #If the visit check is false, append to list K, and check visit check to true
            if visit_check[i]==False:
                K.append(i)
                visit_check[i]=True
   
#When the graphs show up, it will dsiplay the close points set to all
plt.close("all") 
#Asks the user to input the number of rows he/she wants to have in their maze, the number will then be assigned to variable rows
r = input('How many rows do you want your maze to have?')
rows = int(r)
#Asks the user to input the number of columns he/she wants to have in their maze, the number will then be assigned to variable columns
c = input('How many columns do you want your maze to have?')
columns = int(c)
#Creates the adjacency list necessary for the program by using a new class called 'Graph', this is basically n
ad_list=Graph(rows*columns)
#Asks the user to input the number of walls he/she wants to remove, the number will then be assigned to variable, this is basically m
x=input('Input the amount of walls you want to remove from the maze: ') 
walls_removed = int(x) 
walls_removed += 1

#Gets the list of walls in the maze by using the method wall_list from the previous lab
walls_number = wall_list(rows,columns)
#Uses the draw maze method and makes the complete maze without any deletion
draw_maze(walls_number,rows,columns,cell_nums=True) 
# makes the new DSF by combining the rows and columns
S = DisjointSetForest(columns*rows)
# cells amount of the dsf
numCells = cells_number(S)

#Used to answer question question and then displays the message for the user
print()
print('Case:')
print()
cells_display(numCells,walls_removed)

#This essentially serves as the remove walls method so it can be used in the main section
while walls_removed > 0:
    #W is a wall that gets randomly selected
    w = random.choice(walls_number)
    #Gets the position 'p' where we chose the wall to delete
    p = walls_number.index(w)
    #If it finds that wall 0 does not equal to 1, then it deletes the wall, unites after deletion, and sends it to the adjacency list used for question 2
    if find(S,w[0]) != find(S,w[1]):
        walls_number.pop(p)
        union(S,w[0],w[1])
        addEdge(ad_list,w[0],w[1])
        walls_removed -= 1
print()

#Uses various path algorithms and prints out their running time
startTime1=time.time()
print('Using Breadth-First Search algorithm:')
breadth_first_search(ad_list,0)
endTime1=time.time()
finalTime1 = endTime1-startTime1
print()
print('Running time for Breadth-First Search results in:  ',finalTime1)
print()

print()
startTime2=time.time()
print('Using Depth First Search algorithm:')
dfsStack(ad_list,0)
endTime2=time.time()
finalTime2 = endTime2-startTime2
print()
print('Running time for Depth First Search results in: ',finalTime2)
print()

#Uses 
print()
startTime3=time.time()
print('Using Depth First Search with Recursion algorithm:')
print(dfsRecursion(ad_list,0))
endTime3=time.time()
finalTime3 = endTime3-startTime3
print()
print('Running time for Depth First Search with Recursion results in: ',finalTime3)
print()

#Use this to print the graph with the adjacency List, this is essentially used to answer question 2 in the form of a list
draw_maze(walls_number,rows,columns)
#Prints the final graph to be displayed to the user
print(ad_list.graph)