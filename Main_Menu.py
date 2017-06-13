# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:02:57 2016

@author: PAVAN
"""

from Num_Int import *
exit=0
while(exit==0):
    print"\t\t\tNumerical Integration\n\n"
    print"Enter:\n\t1:Riemann Approximation in 1D\n\t2:Trapezium Rule"
    print "\t3:Simpson's Rule\n\t4:Boole's Rule\n\t5:Monte Carlo"
    print"\t6:Monte Carlo in 2D\n\t7:Riemann Approximation in 2D\n\t8:Exit\n"
    inp=input("Choice: ")
    if(inp==8):
        print"\nThank You for using the program. Good bye!"
        exit=1
        continue    
    if(inp<1 and inp>8):
        print "\nInvalid Input. Try again"
        continue
    if(inp<5):
        str1=raw_input("\nEnter expression in terms of x: ") 
        a=input("Enter the lower limit of x: ")
        b=input("Enter the upper limit of x: ")
        n=input("Enter the number of divisions: ")
        if(inp==1):
            print"\nEnter:\n\t1:Riemann Right\n\t2:Riemann Left\n\t3:Riemann Center\n\t4:To go to Main Menu\n"    
            inp1=input("Choice: ")
            if(inp1==1):
                riemann_right(str1,a,b,n)
            elif(inp1==2):
                riemann_left(str1,a,b,n)
            elif(inp1==3):
                riemann_centre(str1,a,b,n)
            else:
                continue
        elif(inp==2):
            trapez(str1,a,b,n)
        elif(inp==3):
            simpsons_rule(str1,a,b,n)
        elif(inp==4):
            booles_rule(str1,a,b,n)
    elif(inp==5):
        str1=raw_input("\nEnter expression in terms of x : ") 
        a=input("Enter the lower limit of x: ")
        b=input("Enter the upper limit of x: ")
        n1=int(input("Enter the number of random points to be generated: "))
        monte_carlo_1d(str1,a,b,n1)
    elif(inp<=7):      
        str1=raw_input("\nEnter expression in terms of x and y: ")
        if(inp==6):
            monte_carlo_2d(str1)
        else:
            riemann_2d(str1)
    else:
        continue1
            
    e=0
    while(e==0):
        ask=raw_input("\nDo you want to compute another integral?(y/n): ")
        if(ask in ['n','N']):
            exit=1
            e=1
        elif(ask in ['y','Y']):
            e=1
        else:
            print"\nInvalid input. Enter again.\n"