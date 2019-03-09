"""
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: March 8, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 3 Binary Search Tress
TA: Anindita Nath & Maliheh Zaragan
Purpose: to implement various algorithms and methods to fully understand the
process of how a Binary Search Tree works.
"""
#Imports various tools to help us plot the binary tree to be used in this lab
import matplotlib.pyplot as plt
import numpy as np
import math 

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right
        
#This method creates the circle to be used when plotting the binary tree       
def circle(center,radius): 
    n = int(4*radius*math.pi)
    t = np.linspace(0,6.3,n)
    y = center[1]+radius*np.sin(t)
    x = center[0]+radius*np.cos(t)
    return x,y 

#This method plots the circles that will be shown when printing the binary search tree
def drawCircles(ax,center,r): 
    x,y = circle(center,r)  
    ax.plot(x,y,color='k') 
     
#Method that inserts items into a binary tree
def Insert(T,i):
    #If T is none, insert item i. This will be the root
    if T == None:
        T =  BST(i)
    #If the current item is less than item i, insert on the left branch   
    elif T.item > i:
        T.left = Insert(T.left,i)
    #If the current item is greater than item i, insert on the right branch
    else:
        T.right = Insert(T.right,i)
    #Return Tree T
    return T
    
# Prints items in BST in ascending order     
def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)

# Prints items and structure of BST  
def InOrderD(T,space):
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
        
#Method that takes in a list Z, and returns a balanced list to be used to create a balanced tree
def balancedTree(Z):   
    #If the list Z is not None
    if Z: 
        #Term median will be the node to keep track that the tree is currently being balanced
        median = len(Z) // 2
        T = BST(Z[median])
        #Will insert the left sub-tree
        T.left = balancedTree(Z[:median])
        #Will insert the left sub-tree
        T.right = balancedTree(Z[median+1:])
        #Returns the new list T
        return T 

# Returns smallest item in BST. Returns None if T is None    
def SmallestL(T):
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   

# Returns smallest item in BST. Error if T is None 
def Smallest(T):
    if T.left is None:
        return T
    else:
        return Smallest(T.left)
    
# Returns largest item in BST. Error if T is None
def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)

#Method that will print the binary tree in its full shape, including its circles, branches, and numbers
def drawTree(ax,dx,dy,n,s,T):
    #While T is not None
    if T != None:
        #Draws the circles that will be used
        drawCircles(ax,[dx,dy],1.5)
        #Contains the info on the current item it is being printed
        ax.text(dx-.5, dy-.5, T.item, size=9, weight='bold')
        #If T has a left child, then it will plot the left branch
        if T.right != None:
            ax.plot([dx,dx+(2**n)],[dy-1.5,dy-s], color='k')
            drawTree(ax,dx+(2**n),dy-s-1.5,n-1,s,T.right)
        #If T has a left child, then it will plot the left branch
        if T.left != None:
            ax.plot([dx,dx-(2**n)],[dy-1.5,dy-s], color='k')  
            drawTree(ax,dx-(2**n),dy-s-1.5,n-1,s,T.left)
        
            
# Returns the address of k in the Binary Tree, or None if k is not in the tree. This version is also iterative, meaning it will point out the current steps that it is doing         
def Find(T,k):
    #If T is empty, it will return none. This also checks if the item was not found
    if T is None:
        return None
    #Prints current item
    print('Current Node= ',T.item)
    #If T is none, it will return the node
    if T is None:
        print('Current Node is None, returning Node')
        return T
    #If T equals k, it will return T
    elif T.item == k:
        print('Current Node equals',k,', returning Node')
        return T
    #If the item is less than k, it will return to find the item on the right branch
    elif T.item<k:
        print('Item is less than',k,', moving to the right child')
        return Find(T.right,k)
    #If the item is greater than k, it will return to find the item on the left branch
    elif T.item>k:
        print('Item is greater than',k,', moving to the left child')
        return Find(T.left,k)
    #If none of the above, it will return None
    else:
        return None

#Method that extracts the data of a list, and 
def extractTree(T, L):
    #While T is not None
    if T != None:
        #Checks through every item in a tree on the left side
        extractTree(T.left, L)
        #Adds a new item to L before returning
        L += [T.item]
        #Checks through every item in a tree on the right side
        extractTree(T.right, L)
        
#Method that prints all of the items located in a particular depth of the Binary Tree. For example, k = 0 will return all the items located in depth 0      
def printDepth(T, k):
    #While T is not None
    if T != None:
        #At depth 0
        if k == 0:
            #Prints the item at depth 0
            print(T.item, end=" ")
        else:
            #Passes through all of the node at the level 'k' on the left and right side
            printDepth(T.left, k-1)
            printDepth(T.right, k-1) 
            
#Method that finds an item in the Binary Tree and prints the item, if it wasnt found, i will indicate so.            
def FindAndPrint(T,k):
    #Sends variable f to method Find, which will try to locate item k in the current Tree
    f = Find(T,k)
    #If find doesnt return none, the item was found
    if f is not None:
        print(f.item,'was found')
    #If None was returned, the item is not in the tree
    else:
        print(k,'was not found')
    
# Code to test the functions above
#Sets a new Empty tree caled T
T = None
#Sets a new list called A. The numbers being used are the ones described in the Lab Assignment for Lab 3
A = [10, 4, 15, 8, 2, 3, 1, 9, 5, 7, 12, 18]
#Prints the initial List that will be used in the program
print('Current List: ')
print(A)
#Inserts the content of the List into the tree T
for a in A:
    T = Insert(T,a)
print('Smallest leaf in the list is: ')
print(SmallestL(T).item)
print('Smallest item in the list is: ')
print(Smallest(T).item)
print('Largest item in the list is: ')
print(Largest(T).item)    

#Task 1
#Prints the binary tree using mathplotlib so it displays like that in the Lab Assignment
print('Printing Binary Tree: ')
fig, ax = plt.subplots()    
drawTree(ax,0,0,4,9,T) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

#Task 2
#Starts the Iterative Search Operation with two numbers that the User can input to check the output
print('Search Operation begin!')
k1 = int(input('Which is the first number you want to look for in the tree?'))
FindAndPrint(T,k1)
k2 = int(input('Which is the second number you want to look for in the tree?'))
FindAndPrint(T,k2)
print()

#Task 3
#Makes a duplicate of list A and then proceeds to create a new balanced tree on the input of that list
#Copies List A to Z to keep the original list. List Z will be sent to method Balance
Z = A
#Sends list Z to method balancedTree so it can be balanced before it is printed
print('Balancing tree')
S = balancedTree(Z)
#Prints the balanced tree in the form of task 1. All of the preferences are still intact
print('Printing Balanced Binary Tree: ')
fig, ax = plt.subplots()    
drawTree(ax,0,0,4,9,S) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

#Task 4 
#A_copy is new list that will extract the data of T and will print a sorted list to the user
A_copy = []
print('Extracting data')
extractTree(T, A_copy)
print('Printing extracted data, here is your new list:', A_copy)
print()

#Task 5 
#Prints the depth of a particular Binary Tree. The current tree we have righ now has a depth of 4, hence we print the four depths of the tree
#Prints at depth 0
print('Keys at depth 0:', end=' ')
printDepth(T,0)
print()
#Prints at depth 1
print('Keys at depth 1:', end=' ')
printDepth(T,1)
print()
#Prints at depth 2
print('Keys at depth 2:', end=' ')
printDepth(T,2)
print()
#Prints at depth 3
print('Keys at depth 3:', end=' ')
printDepth(T,3)
print()
#Prints at depth 4
print('Keys at depth 4:', end=' ')
printDepth(T,4)
