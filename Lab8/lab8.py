"""
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: May 12, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 8 Algorithm Design Techniques
TA: Anindita Nath & Maliheh Zaragan
Purpose: to implement both randomized algorithms and backtracking teachniques
learned in class to check if two algorithmic identities are the same, and to 
check the partitions of a new array.
"""
#Imports various tools to help us calculate the hash tables to be used in this lab
import time
import random
import mpmath
import numpy as np

#Method that goes through all of the strings of a givrn list, and and checks if they are similar in value
def similarities(S):
    #Starts a counter to keep track of all the 
    count=0
    #For i in range of the length of S
    for i in range(len(S)):#goes through all the strings
        #For i in range of the length of S
        for j in range(i,len(S)):
            #If S[i] is equal to S[j], then it will print both items, and add one to count
            if(same_values(S[i],S[j])):
                print(S[i],S[j]) 
                count+=1
    #Returns the value of count to the user
    return count
  
#Method that calculates if two strings are similar in value to each other,=.
def same_values(string_1, string_2,calls=1000,tolerance=0.0001):
    #For i in the range of calls
    for i in range(calls):
        #Assigns a random number to variable x
        x = random.uniform(-mpmath.pi,mpmath.pi)
        #Sets a new number value1 which takes the information from string_1, and evaluates it
        value1 = eval(string_1)
        #Sets a new number value2 which takes the information from string_2, and evaluates it
        value2 = eval(string_2)
        #If the absolute value of value1 - value2 is greater than the tolerance value, then it returns false
        if np.abs(value1-value2)>tolerance:
            return False
    #Returns true if the statement abive is incorrect
    return True

#Method that checks if apartion can be made from the two parts of S
def arrayPartition(S1,S2):
    #If the sum of S1 % by 2 is not 0, then there is no partition
    if sum(S1)%2!=0:#if summation of sum is odd then return error message
        return "No partition exists"
    else:
        #Creates a set needed for the next section
        res,s,= subset_summation(S1,len(S1)-1,sum(S1)//2)
        #If the length of s equals 0, then there is no partition
        if len(s)==0:
            return "No partition exists"
        #For every i in s
        for i in s: 
            #New counter is created used to get the position
            counter=0
            #For every j in S1
            for j in S1:
                #If the value of i equals the value of j, then S1 pops a value
                if i == j:
                    S1.pop(counter)
                    #Adds one to the counter
                counter+=1
        #Returns the value of s and S1
        return s,S1
         
#Method that creates a new subse
def subset_summation(S,last,goal):
    #If the value of goal equals 0, then it returns true with a new blank array 
    if goal == 0:
        return True, []
    #If the value of goal is less than or greater than 0, then it retrens false with a new blank array 
    if goal<0 or last<0:
        return False, []
    #Takes a new subset
    res, subset = subset_summation(S,last-1,goal-S[last]) 
    #If res is true, then it will append S[last and retrun true with the subset
    if res:
        subset.append(S[last])
        return True, subset
    #Otherwise, it will not take S[last from the list and move on
    else:
        return subset_summation(S,last-1,goal) 

#Starts the timer for the running time for part 1
startTime1=time.time() 
#Creates a new array called 'part1' which will import all of the functions that will be compared its equalities
part1=['mpmath.sin(x)',
       'mpmath.cos(x)',
       'mpmath.tan(x)',
       'mpmath.sec(x)',
       '-mpmath.sin(x)',
       '-mpmath.cos(x)',
       '-mpmath.tan(x)',
       'mpmath.sin(-x)',
       'mpmath.cos(-x)',
       'mpmath.tan(-x)',
       'mpmath.sin(x)/mpmath.cos(x)',
       '2*mpmath.sin(x/2)*mpmath.cos(x/2)',
       'mpmath.sin(x)**2',
       '1-mpmath.cos(x)**2',
       '(1-mpmath.cos(2*x))/2',
       '1/mpmath.cos(x)']
#The actual method t
sim_count = similarities(part1)
#Prints the count number found in the method similarities
print('The number of similarities in the equations are a total of: ', sim_count)
#Ends the timer for the running time for part 1
endTime1=time.time()
#Creates the fianl time for the running time for part 1
finalTime1 = endTime1-startTime1

#Starts the timer for the running time for part 2
startTime2=time.time()
#Creates a new array of integeres needed for part 2 of the lab
part2=[2,4,5,9,12]
#Sends the new array to method arrayPartition
print(arrayPartition(part2,part2))
#Ends the timer for the running time for part 2
endTime2=time.time()
#Creates the fianl time for the running time for part 2
finalTime2 = endTime2-startTime2

#Prints the running times of both part 1 and part 2
print('Running time for Part 1 in:  ',finalTime1)
print('Running time for Part 2 in:  ',finalTime2)