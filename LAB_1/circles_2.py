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
def draw_circles_2(ax,n,center,radius):
    #Draws depending on the number of circles needed
    if n>0:
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle(center,radius)
        #Plots the main circle from the data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle(center,radius/3)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles_2(ax,n-1,center,radius/3)
        
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle([center[0]+radius-radius/3,center[1]],radius/3)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles_2(ax,n-1,[center[0]+radius-radius/3,center[1]],radius/3)
        
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle([center[0]-radius+radius/3,center[1]],radius/3)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles_2(ax,n-1,[center[0]-radius+radius/3,center[1]],radius/3)
        
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle([center[0],center[1]+radius-radius/3],radius/3)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles_2(ax,n-1,[center[0],center[1]+radius-radius/3],radius/3)
        
        #Finds x and y by sending the center and the radius to the Method Circle, where it will calculate the figure itself.
        x,y = circle([center[0],center[1]-radius+radius/3],radius/3)
        #Plots the circle from data found from the "Circle" method. To give its unique shape, I added the value of the radius to x so that it  
        ax.plot(x, y,color='k')
        #Recursively calls itself again with a radius times the width. This will call itself over and over until the counter n reaches 0.
        draw_circles_2(ax,n-1,[center[0],center[1]-radius+radius/3],radius/3)
        
#Closes the window where the figure is drawn
plt.close("all") 
fig, ax = plt.subplots() 
#Calls the method draw_circles2, and sets the values to draw the figure. I removed w or width as it is not necessary in the code to calculate it in this program
draw_circles_2(ax, 2, [100,100], 100)
#Sets the aspect ratio to be shown of the figure at hand
ax.set_aspect(1.0)
#Turns on or off the measurements of the axis in the figure
ax.axis('on')
#Displays the figure on the terminal
plt.show()
#Saves an image as PNG of the figure you plotted
fig.savefig('circles.png')

'''
For figure a): Change n to 2
    
For figure b): Change n to 3

For figure c): Change n to 4
'''
