#Imports the matplotlibrary and numpy to plot the figures
import matplotlib.pyplot as plt
#Imports the numpy 
import numpy as np
#Method that plots the squares to be drawn in the image.
def draw_squares(ax,n,dx,dy,r):
    if n>0:
        #Sets a new x and y from the top to be drawn in the figure from the top 
       x1 = dx-r
       y1 = dy+r
       #Sets a new x and y from the top to be drawn in the figure from the bottom 
       x2 = dx+r
       y2 = dy-r
       #Array that contains the values to be used to plot the squares
       p = np.array([[x1, y2],[x1,y1],[x2,y1],[x2, y2],[x1, y2]])
       #The call that actually plots the squares in the method
       ax.plot(p[:,0],p[:,1],color='k')
       #Recursively calls the method again to draw the remaining squares, starting from top left and ending on bottom left
       draw_squares(ax,n-1,x1,y1,r*.5)
       draw_squares(ax,n-1,x2,y1,r*.5)
       draw_squares(ax,n-1,x2,y2,r*.5)
       draw_squares(ax,n-1,x1,y2,r*.5)

#Closes the window where the figure is drawn   
plt.close("all") 
fig, ax = plt.subplots() 
#Calls the method draw_squares, and sets the values to draw the figure.
draw_squares(ax,4,0,0,100)
#Sets the aspect ratio to be shown of the figure at hand
ax.set_aspect(1.0)
#Turns on or off the measurements of the axis in the figure
ax.axis('on')
#Displays the figure on the terminal
plt.show()
#Saves an image as PNG of the figure you plotted
fig.savefig('squares.png')

'''
For figure a): Change n to 2
    
For figure b): Change n to 3

For figure c): Change n to 4
'''