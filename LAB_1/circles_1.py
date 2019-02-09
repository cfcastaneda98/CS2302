'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: February 8, 2019 
Instructor: Olac Fuentes 
Assingment: Lab 1 Recursion
TA: Anindita Nath & Maliheh Zaragan
Purpose: To practice using recursion amd to identify the process of ploting figures using
pythons libraries

Part 2 of 4 

Nested Circles #1
'''
#Imports the matplotlibrary and numpy to plot the figures
import matplotlib.pyplot as plt
#Imports the numpy 
import numpy as np
#Imports the math module
import math 
#Method that caclulates the center and the radius of the specififc circle. Later sends the information back to draw_circles
def circle(center,rad):
    #Calculates the shape of the circle
    n = int(4*rad*math.pi)
    #Returns Return evenly spaced numbers over the specified interval.
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y



#Method that plots the circles to be drawn in the image. 
def draw_circles(ax,n,center,radius,w):
    #Draws depending on the number of circles needed
    if n>0:
        #Finds x and y by sending the canter and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle(center,radius)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x+radius, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles(ax,n-1,center,radius*w,w)
#Closes the window where the figure is drawn
plt.close("all") 
fig, ax = plt.subplots() 
#Calls the method draw_circles, and sets the values to draw the figure
draw_circles(ax, 80, [100,0], 100,.95)
#Sets the aspect ratio to be shown of the figure at hand
ax.set_aspect(1.0)
#Turns on or off the measurements of the axis in the figure
ax.axis('on')
#Displays the figure on the terminal
plt.show()
#Saves an image as PNG of the figure you plotted
fig.savefig('circles.png')

'''
For figure a): Change n to 9, and w to .6
    
For figure b): Change n to 40, and w to .88

For figure c): Change n to 80, and w to .95
'''