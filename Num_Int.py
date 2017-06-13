# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:13:46 2016

@author: PAVAN
"""

#Header Files
import numpy as np
import parser
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#str=raw_input("\nEnter expression in terms of x and y: ")


def func(str1,x,y):
    from numpy import *
    code=parser.expr(str1).compile()
    return eval(code)
    
def ask_for_graph():
    if raw_input("Do you want to print a graph?(y/n):") in ['y','Y']:
        return 1
    else:
        return 0
    
def monte_carlo_1d(str1,xmin,xmax,n):    
    x=np.linspace(xmin,xmax,10000)
    yp=func(str1,x,0)
    ymin=np.min(yp)
    ymax=np.max(yp)
  
    plt.plot(x,yp,linewidth=5)
    if ymin>0:
        ymin=0
    if ymax<0:
        ymax=0
    i=n
    c=0
    l=0
    pospoint=0
    negpoint=0
    
    while(i>0):
        x=np.random.uniform(xmin,xmax)
        y=np.random.uniform(ymin,ymax)
        i=i-1
        if y>0:
            if y>func(str1,x,0):
                plt.scatter(x,y,color='r')
            if y<func(str1,x,0):
                plt.scatter(x,y,color='g')
                pospoint=pospoint+1
            c=c+1
        if y<0:
            if(y<func(str1,x,0)):
                plt.scatter(x,y,color='r')
            if y>func(str1,x,0):
                plt.scatter(x,y,color='g')
                negpoint=negpoint+1
            l=l+1


    print'No.of positive points in the graph=',c
    print'No.of negative points in the graph=',l

    area_pos=(xmax-xmin)*(ymax)
    area_pos=float(area_pos)
    print'Area of the positive rectangle',area_pos
    area_neg=(xmax-xmin)*(0-ymin)
    area_neg=float(area_neg)
    print 'Area of the negative rectangle',area_neg

    pos_integral=pospoint*area_pos
    if c!=0:
        pos_integral=float(pos_integral)/c
    else:
        pos_integral=0
    print 'Positive integral of the graph is ',pos_integral

    neg_integral=negpoint*area_neg
    if l!=0:
        neg_integral=float(neg_integral)/l
    else:
        neg_integral=0

    print 'Negative integral of the graph is ',neg_integral
    
    def_integral=(pos_integral-neg_integral)
    print'Definite integral of the expression is ', def_integral
    
    #To plot the graph
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')            
    plt.plot(x, y)
    plt.grid()
    plt.show()

def monte_carlo_2d(str1):
    x1=input("Enter lower limit of x: ")
    x2=input("Enter upper limit of x: ")
    y1=input("Enter lower limit of y: ")
    y2=input("Enter upper limit of y: ")

    n=400   #The number of xs, ys and zs generated

    #Creating a database of values
    x=np.linspace(x1,x2,n)
    y=np.linspace(y1,y2,n)
    z=[func(str1,x[i],y[j]) for i in range(n) for j in range(n)]
    z_max=np.max(z)
    z_min=np.min(z)
   
    
    #Number of random points to be generated
    n1=int(input("Enter the number of random points to be generated: "))
    
    #Lists containing the coordinates of the random numbers
    xrand=np.random.randint(x1,x2,n1)
    yrand=np.random.randint(y1,y2,n1)
    z_y_xrand=[func(str1,xrand[i],yrand[i]) for i in range(n1)]
    zrand=np.random.uniform(z_min,z_max,n1)
    m1=0    #counting all random points above the x-y plane   
    m2=0    #counting all random points below the x-y plane
    
    for i in range(n1):
        if(zrand[i]>=0):
            m1+=1
        else:
            m2+=1

    k1=0    #counting inner points above the x-y plane   
    k2=0    #counting outer points below the x-y plane     

    for i in range(n1):
        if z_y_xrand[i]>=0:  #For the case when it's above the x-y plane
            if (zrand[i]<z_y_xrand[i]) and (zrand[i]>=0):
                k1+=1
        else:          #For the case when it's below
            if (zrand[i]>z_y_xrand[i]) and (zrand[i]<=0):
                k2+=1
    upper_vol=z_max*(x2-x1)*(y2-y1)  
    lower_vol=z_min*(x2-x1)*(y2-y1) 

    if(m1==0):
        integral= (k2*lower_vol/m2)
    elif(m2==0):
        integral= (k1*upper_vol/m1)
    else:
        integral= (k1*upper_vol/m1)+(k2*lower_vol/m2)

    print "The integral is equal to: ", integral
    
    if(ask_for_graph()==1):
    #Plotting 3d
        try:
            fig = plt.figure()
            ax = Axes3D(fig)
            xp=np.linspace(x1,x2,300)
            yp=np.linspace(y1,y2,300)
            zp=[]              
            X, Y = np.meshgrid(xp, yp)
            zp=func(str1,X, Y)
            ax.plot_wireframe(X, Y, zp, 
                              rstride=3, 
                              cstride=3, 
                              alpha=0.3,            # transparency of the surface 
                              cmap=plt.cm.BuPu)         # colour map
            ax.scatter(xrand,yrand,zrand,c='red')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Monte Carlo 2-D')
            plt.show()
        except:
            print "Graph cannot be plotted"

def simpsons_rule(str1,xmin,xmax,n):  
    #Creating a database of values
    '''
    x=np.linspace(xmin,xmax,2*n)
    x1=np.linspace(xmin,xmax,n)
    y=[func(str1,x[i],0) for i in range(2*n)]
    y1=[]
    sum=0
    i=0
    '''
    x=np.linspace(xmin,xmax,n)
    y=[func(str1,x[i],0) for i in range(n)]

    sum=0

    for i in range(n-1):
        sum+=(x[i+1]-x[i])*(func(str1,x[i],0)+4*func(str1,(x[i]+x[i+1])/2,0)+func(str1,x[i+1],0))/6

    print "The Integral is: ",sum
    if(ask_for_graph()==1):
        plt.plot(x, y,'r-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Simpson's Rule")
        plt.show()
    #y1.append(0)
    '''
    print "The Integral is: ",sum
    if(ask_for_graph()==1):
        plt.plot(x1, y1,'r-')
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Simpson's Rule")
        plt.show()
    '''

def booles_rule(str1,xmin,xmax,n):

    #Creating a database of values
    x=np.linspace(xmin,xmax,n)
    #y=[func(str1,x[i],0) for i in range(n)]

    sum=0
    for i in range(n-1):
        h=(x[i+1]-x[i])/5
        sum+=2*h*(7*func(str1,x[i],0)+32*func(str1,x[i]+h,0)+12*func(str1,x[i]+2*h,0)+32*func(str1,x[i]+3*h,0)+7*func(str1,x[i]+4*h,0))/45
    print "The Integral is: ",sum    
    if(ask_for_graph()==1):
        #plt.plot(x1, y1,'r-')
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Boole's Rule")
        plt.show()

def trapez(str1,xmin,xmax,n):
    h= float(xmax-xmin)/n
    s= 0.0
   
    for i in range(0,n):
        s+=(func(str1,xmin+i*h,0)+func(str1,xmin+(i+1)*h,0))*h*0.5

    #return s*h  
    print "The Integral is: ",s
    x1=[]
    y1=[]  
      
    x=np.linspace(xmin,xmax,n)
    for i in range(n-1):
        a=func(str1,x[i],0)
        b=func(str1,x[i+1],0)
        x1.append(x[i])
        x1.append(x[i])
        x1.append(x[i+1])
        x1.append(x[i+1])
        y1.append(0)
        y1.append(a)
        y1.append(b)
        y1.append(0)
    x2 = np.linspace(xmin,xmax,10*n,endpoint=False)
    y2 = func(str1,x2,0)
    
    if(ask_for_graph()==1):    
        plt.plot(x1,y1)
        plt.plot(x2,y2)
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Trapezoidal Rule")
        plt.show()
def plot_riemann_1d(str1,x,y,inc,n):
        plt.bar(x,y,inc,color='y')        
        plt.plot(x,func(str1,x,0))    
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')
        if(n==1):
            plt.title("Reimann Left")
        elif(n==2):
            plt.title("Reimann Right")
        else:
            plt.title("Reimann Centre")
        plt.show()   
def riemann_left(str1,xmin,xmax,n):     
    inc=float((xmax-xmin))/n   
    #i=xmin
    x=np.linspace(xmin,xmax,n)
    y=[func(str1,x[j],0) for j in range(0,n-1)]
    k=np.sum(y)
    y.append(0)
    print "The Integral is: ",k*inc
    if(ask_for_graph()==1):
        plot_riemann_1d(str1,x,y,inc,1) 
        
def riemann_right(str1,xmin,xmax,n):
     inc=float((xmax-xmin))/n   
     x=np.linspace(xmin,xmax,n)
     y=[func(str1,x[j],0) for j in range(1,n)]
     y.append(0)
     k=np.sum(y)
     print "The Integral is: ",k*inc
     if(ask_for_graph()==1):
        plot_riemann_1d(str1,x,y,inc,2)    
def riemann_centre(str1,xmin,xmax,n):     
     inc=float((xmax-xmin))/n   
     x=np.linspace(xmin,xmax,n)
     y=[func(str1,(x[j]+x[j+1])/2,0) for j in range(0,n-1)]
     y.append(0)
     k=np.sum(y)
     print "The Integral is: ",k*inc
     if(ask_for_graph()==1):
         plot_riemann_1d(str1,x,y,inc,3) 
def riemann_2d(str1):
    a=input("Enter lower limit of x: ")
    a1=input("Enter upper limit of x: ")
    b=input("Enter lower limit of y: ")
    b1=input("Enter upper limit of y: ")
    n=input("Enter side of sqr base: ")
    inc1=n
    inc2=n
    l=[]
    i=a
    j=b
    while j<b1:
        p = []
        i= a
        while i<a1:
            vol=((i+inc1)-i)*((j+inc2)-j)*(func(str1,i,j))
            p.append(vol)
            i = i+inc1
        l.append(sum(p))
        j = j+inc2
    print "The Integral is: ",sum(l)
