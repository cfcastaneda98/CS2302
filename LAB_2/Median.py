"""
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: February2, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 2 Median
TA: Anindita Nath & Maliheh Zaragan
Purpose: to implement several algorithms for finding the median of a list of integers, using
objects of the List class described in class, and compare their running times (measured as the number of
comparisons each algorithm makes) for various list lengths.
"""
#Used to make the random list
import random
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        self.Len = 0
        
#Makes a new empty list
def NewList(L):
    L.head = None
    L.tail = None
    L.Len = 0
    
#Makes a new List with a size of n terms, as listed in the instructions
def RandomList(n): 
    L = List()
    i = n
    while i>0:
        Append(L,random.randint(0,n*2))
        i = i - 1
    return L

#Sorting Algorithm Functions
def BubbleSort(L):
    if IsEmpty(L):
        return None
    else:
        Current = L.head
        Completed = False
        while Completed != True:
            Completed = True
            Current = L.head
            while Current.next is not None:
                if Current.item > Current.next.item:
                    nextItem = Current.next.item
                    Current.next.item = Current.item
                    Current.item = nextItem
                    Completed = False
                Current = Current.next   

def QuickSort(L):
    if L.Len > 1:
        middle = L.head.item
        List1 = List()
        List2 = List()
        Current = L.head.next
        while Current != None:
            if Current.item < middle:
                Append(List1, Current.item)
            else:
                Append(List2, Current.item)
            Current = Current.next
        
        QuickSort(List1)
        QuickSort(List2)
        
        if IsEmpty(List1):
            Append(List1, middle)
        else:
            Prepend(List2, middle)
            
        if IsEmpty(List1):
            L.head = List2.head
            L.tail = List2.tail
        else:     
            List1.tail.next = List2.head
            L.head = List1.head
            L.tail = List2.tail

def MergeSort(L):
    if L.Len > 1:
        L1 = List()
        L2 = List()
        NewLength = L.Len//2
        Current = L.head 
        
        for i in range(NewLength):
            Append(L1, Current.item)
            Current= Current.next
            
        while Current != None:
            Append(L2, Current.item)
            Current = Current.next
            
        MergeSort(L1)
        MergeSort(L2)
        NewList(L)
        MergeList(L, L1, L2)
   
def QuickSort2(L, Median):
    List1 = List()
    List2 = List()
    if L.Len <= 1:
        return L.head.item
    middle = L.head.item
    
    Current = L.head.next
    while Current != None:
        if Current.item < middle:
            Append(List1, Current.item)
            
        else:
            Append(List2,Current.item)
        Current = Current.next

    if List1.Len > Median :
        return QuickSort2(List1, Median)
    
    elif(List1.Len == 0 and Median == 0):       
        return middle
    
    elif(List1.Len == Median):
        return middle
    
    else:
        return QuickSort2(List2, Median - List1.Len - 1)
    
#Median Algorithms     
def MedianBubble(L):
    C = Copy(L)
    BubbleSort(C)
    NewLength = C.Len//2
    Current = C.head
    for i in range(NewLength):
        Current = Current.next
    return Current.item

def MedianMerge(L):
    C = Copy(L) 
    MergeSort(C)
    NewLength = C.Len//2
    Current = C.head
    for i in range(NewLength):
        Current = Current.next
    return Current.item

def MedianQuick(L):
    C = Copy(L)
    QuickSort(C)
    NewLength = C.Len//2
    Current = C.head
    for i in range(NewLength):
        Current = Current.next
    return Current.item

def MedianQuick2(L):
    C = Copy(L)
    LengthCopy = C.Len//2
    print(QuickSort2(C, LengthCopy))
    
#States if the current List is empty or not
def IsEmpty(L):
    return L.head == None     

# Inserts x at end of list L   
def Append(L,x): 
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len = L.Len + 1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.Len = L.Len + 1
        

# Inserts x at beginging of list L        
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len = L.Len + 1
    else:    
        L.head=Node(x,L.head)   
        L.Len = L.Len + 1

# Prints list L's items in order using a loop
def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next

# Appends sorted Lists into L
def MergeList(L,L1,L2):
    #Grabs the two head of each respective list. Called the variables current as it is the current item the algorithm is analyzing
    Current1 = L1.head
    Current2 = L2.head
    while Current1 != None and Current2 != None:
        #Adds the lowest term first of either list
        if Current1.item < Current2.item:
            Append(L, Current1.item)
            Current1 = Current1.next
        else:
            Append(L, Current2.item)
            Current2 = Current2.next 
    #Clarifies that if either list contains any elements, if so, they will add any remaining items to the new list
    if Current1 is None:
        while Current2 != None:
            Append(L, Current2.item)
            Current2 = Current2.next
    if Current2 is None:
        while Current1 != None:
            Append(L, Current1.item)
            Current1 = Current1.next
    
    
#Copies the content of a list and returns that copy
def Copy(L):
    copy = List()
    t = L.head
    while t != None:
        Append(copy,t.item)
        t = t.next
    return copy

#Makes a random list
L = RandomList(5)
print('Original list: ')
print('')
Print(L)
print('')
print('Sorting by:')
print('')
print('Bubble sort, median is: ')
print(MedianBubble(L))
print('')
print('Merge sort, median is: ')
print(MedianMerge(L))
print('')
print('Sorted by quick sort, median is: ')
print(MedianQuick(L))
print('')
print('Sorted by the new quick sort, median is: ')
print(MedianQuick2(L))
