#Imports the numpy 
import numpy as np
#Imports the matplotlibrary and numpy to plot the figures
import matplotlib.pyplot as plt
#Method that plots the tree to be drawn in the image. 
def draw_branch(ax,n,c,x,y):
    if c>0:
        #Splits the call into two sections, negative and positive x, where it will plot on two different sides of the graph
        ax.plot([n[0],n[0]-x],[n[1],n[1]-y], color='k')
        #Recursively calls it twice depending on the side of the branch
        draw_branch(ax,[n[0]-x,n[1]-y],c-1,x/2,y*0.92)
        #Splits the call into two sections, negative and positive x, where it will plot on two different sides of the graph
        ax.plot([n[0],n[0]+x],[n[1],n[1]-y], color='k')
        #Recursively calls it twice depending on the side of the branch
        draw_branch(ax,[n[0]+x,n[1]-y],c-1,x/2,y*0.92)
#Closes the window where the figure is drawn
plt.close("all") 
fig, ax = plt.subplots()
n=np.array([0,0])
#Calls the method draw_branch, and sets the values to draw the tree
draw_branch(ax, n , 4, 100, 100)
#Sets the aspect ratio to be shown of the figure at hand
ax.set_aspect(1.0)
#Turns on or off the measurements of the axis in the figure
ax.axis('on')
#Displays the figure on the terminal
plt.show()
#Saves an image as PNG of the figure you plotted
fig.savefig('bracket.png')

'''
For figure a): Change c to 3
    
For figure b): Change c to 4
    
For figure c): Change c to 7
'''