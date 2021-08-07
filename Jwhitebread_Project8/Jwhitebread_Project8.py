#Jake Whitebread
#Dr. Citro
#Project 8: Numerical Integration, Reimann
#April 17, 2021
#I affirm that this is my work

import numpy as np
from scipy.integrate import odeint, quad, simps
import matplotlib.pyplot as plt
from scipy import pi

#function to solve for the reimann sum. Solves left, right, and middle approximations
def reimannSum(f, min, max, n):
    step = (max - min)/n        #finds how many steps are needed
    left = np.linspace(min,max - step, n)   #finds step size for left approximation
    mid = np.linspace(step / 2, max - step / 2, n)  #find step size for the midpoint approximation
    right = np.linspace(step, max, n)   #step size for the right approximation

    leftSum = np.sum(f(left) * step)                    #calculates left sum
    print("Riemann Sum of Left approx.:\t", leftSum)    #print sum

    midSum = np.sum(f(mid) * step)                      #calculates midpoint sum
    print ("Riemann Sumn of midpoint approx.:\t", midSum)   #print sum

    rightSum = np.sum(f(right) * step)                  #calculates right sum
    print ("Riemann Sum of right approx.:\t", rightSum) #print sum


#function to plot the riemann sums
def plotRiemann(f, min,max,step):
    n = 1000

    #x and y spaces. First two are for bar chart
    x = np.linspace(min,max,step+1)
    y = f(x)
    x2 = np.linspace(min,max,n*step+1)
    y2 = f(x2)

    plt.figure(figsize=(15,5))

    #define left endpoints and create plot for left approximation
    plt.subplot(1,3,1)
    plt.plot(x2,y2,'b')
    leftX = x[:-1]
    leftY = y[:-1]

    #plot left approximation
    plt.plot(leftX,leftY,'b.',markersize = 10)
    plt.bar(leftX, leftY, width = (max-min) / step, alpha = 0.2, align = 'edge', edgecolor = 'b')
    plt.title('Left Riemann Sum, step = {}'.format(step))

    #define midpoint endpoints and create plot
    plt.subplot(1,3,2)
    plt.plot(x2,y2,'b')
    midX =( x[1:] + x[1:]) / 2
    midY = f(midX)

    #plot midpoint approximation
    plt.plot(midX,midY, 'b.', markersize=10)
    plt.bar(midX,midY, width = (max-min) / step, alpha = 0.2, edgecolor = 'b')
    plt.title('Midpoint Riemann Sum, step = {}'.format(step))

    #define right endpoints and create plot
    plt.subplot(1,3,3)
    plt.plot(x2,y2,'b')
    rightX = x[1:]
    rightY = y[1:]

    #plot right approximation
    plt.plot(rightX, rightY, 'b.', markersize = 10)
    plt.bar(rightX, rightY, width = -(max-min) / step, alpha = 0.2, align = 'edge', edgecolor = 'b')
    plt.title('Right Riemann Sum, step = {}'.format(step))

    plt.show()

    #function to create plot for part 2: download speed vs. time
def pltDownload(xs,ys):
    plt.plot(xs,ys,'b.',markersize = 1)
    plt.fill_between(xs,ys,alpha=0.2,edgecolor='b')
    plt.title("Download Speed v. Time")
    plt.xlabel("Time (min)")
    plt.ylabel("Download Speed (Mbs)")
    plt.show()

    for i in range(len(ys)): ys[i] *= 60.0      #this changes data to megabits a minute instead of seconds
    print("The area under the curve is:", simps(ys,xs), "megabits")

def main():
    #lambda functions
    f = lambda x: np.sin(x) + 1         #function for 1a
    g = lambda x: (3*x) + (2*(x**2))    #function for 1b
    h = lambda x: np.log(x)             #function for 1c_1
    i = lambda x: (x**2) - (x**3)       #function for 1c_2

    #solves and prints value for the riemann sum for each of the functions. Uses built in function from above.
    print("\nThe riemman sum for 1a:"); reimannSum(f, -pi, pi, 4)                      
    print("\nThe riemman sum for 1b:"); reimannSum(g, 0, 1, 1000)         
    print("\nThe riemman sum for 1c_1:"); reimannSum(h, 1, np.e, 1000)        
    print("\nThe riemman sum for 1c_2:"); reimannSum(i, -1, 0, 1000)    
    
    #plots each of the riemann sums of each function. Uses built in plotting function from above.
    plotRiemann(f,-pi,pi,4)
    plotRiemann(g,0,1,50)
    plotRiemann(h,1,np.e,50)
    plotRiemann(i,-1,0,50)

    #part 2:
    xSpace = np.linspace(0,31,32)       #linspace for the time values
    #array for the download speed data I collected
    ySpace = [0,7,7.4,6.6,7.2,7.3,5.5,6.8,5.5,5.8,6.8,6.8,5.9,6.7,6,4.1,6.4,6.9,6.1,7.2,6.6,6.4,6.4,6.7,6.7,5.8,6,5.5,6.1,7,6.8,6.8]
    pltDownload(xSpace,ySpace)      #plots graph for part 2 using built in function defined above



main()