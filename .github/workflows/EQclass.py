import sympy as sp  # for Maths Expression handling
import numpy as np
import scipy as sc
import matplotlib as mp
import math
import errno
import colorama
from colorama import Fore, Back, Style
from sympy import *

colorama.init(autoreset=True)    # to automatically reset colour at the end of print


class Equation:
    x, e = sp.symbols('x e')
    dp = 9  # Decimal place

    def f_x(self, n):        # To compute f(x) at any given value of x

        if N(self.expr.subs(Equation.e, math.e).subs(Equation.x, n), Equation.dp) == zoo:
            return 'Math Error !!!'
        else:
            return N(self.expr.subs(Equation.e, math.e).subs(Equation.x, n), Equation.dp)

    def root_exist(self):       # To check if root exist in the given Interval

        if (float(self.f_x(self.interval[0])) * float(self.f_x(self.interval[1]))) < 0:
            print(Fore.CYAN + "\tRoot Exist in the given Interval .")
            return True
        else:
            print(Fore.RED + "\tRoot Does Not Exist in the given Interval .")
            return False

    def __init__(self):
        try:
            self.expr = (sp.nsimplify(input("Enter an Expression : ")))
            if self.expr.count(Equation.x) != 0:
                self.interval = []
                choice = input("Do you want to enter any interval ? \n " + Fore.BLUE + " Enter ( y / n ) :  ")
                if choice == 'y':
                    self.interval.insert(0, sp.nsimplify(input("Enter the lower bound of the Interval : ")))
                    self.interval.insert(1, sp.nsimplify(input("Enter the upper bound of the Interval : ")))
                    if self.f_x(self.interval[0]) == 'Math Error !!!' or self.f_x(self.interval[1]) == 'Math Error !!!':
                        print("\nf(" + str(self.interval[0]) + ') = ', end='')
                        print(self.f_x(self.interval[0]))
                        print("f(" + str(self.interval[1]) + ') = ', end='')
                        print(self.f_x(self.interval[1]))
                        self.find_intervals()
                    if not self.root_exist():
                        self.find_intervals()
                else:
                    self.find_intervals()

                choice = input("Do you want to enter Tolerance ? \n" + Fore.BLUE + " Enter ( y / n ) :  ")
                if choice == 'y':
                    self.Tolerance = float(input("Enter the Tolerance (in decimals) : "))
                else:
                    self.Tolerance = 0.0001  # 10^-4
                print(Fore.GREEN + "\t\tDefault Value Is Assigned to " + str(self.Tolerance) + " Tolerance .")

            choice = input("Do you want to enter no. of Decimal places ? \n " + Fore.BLUE + " Enter ( y / n ) :  ")
            if choice == 'y':
                Equation.dp = input("Enter the no.of decimal places : ")
            else:
                print(Fore.GREEN + "\t\tDefault Value Is Assigned to " + str(Equation.dp) + " Decimal Places .")
        except SympifyError:
            print(Fore.RED + "\n\t\tInvalid Expression !!! ")
            exit()

    def display(self):

        print("\nThe Expression is : \n")
        pprint(N(self.expr, Equation.dp))
        if self.expr.count(Equation.x) != 0:
            print("\nThe Interval is : " + str(self.interval))
            print("\nf(" + str(self.interval[0]) + ') = ', end='')
            print(self.f_x(self.interval[0]))
            print("f(" + str(self.interval[1]) + ') = ', end='')
            print(self.f_x(self.interval[1]))
            self.root_exist()
            print("Tolerance = ", end='')
            print(self.Tolerance)

    def find_intervals(self):       # To find best interval if user has not provided any interval .
        self.interval.clear()       # Range to find the intervals in between(to be added in future )
        for i in range(1, 20):
            if self.f_x(i) != zoo and self.f_x(i + 1) != zoo:
                if float(self.f_x(i)) * float(self.f_x(i+1)) < 0:
                    self.interval.insert(0, i)
                    self.interval.insert(1, i+1)
                    break
            else:
                continue
        if not self.interval:
            print(Fore.Red + "\n\t\t Cannot Find Valid Intervals for the given Expression !!! ")
            exit()

