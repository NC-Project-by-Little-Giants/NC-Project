import sympy as sp  # for Maths Expression handling
import numpy as np
import scipy as sc
import matplotlib as mp
import math
import errno
import colorama
from colorama import Fore, Back, Style
from sympy import *
from Root_of_Eq import Root_of_Eq
from tabulate import tabulate

colorama.init(autoreset=True)    # to automatically reset colour at the end of print


class Equation(Root_of_Eq):
    x, e = sp.symbols('x e')
    dp = 9  # Decimal place

    @staticmethod
    def f_x(fx, n):        # To compute f(x) at any given value of x

        if N(fx.subs(Equation.e, math.e).subs(Equation.x, n), Equation.dp) == zoo:
            return 'Math Error !!!'
        else:
            return N(fx.subs(Equation.e, math.e).subs(Equation.x, n), Equation.dp)

    def root_exist(self):       # To check if root exist in the given Interval

        if (float(self.f_x(self.expr, self.interval[0])) * float(self.f_x(self.expr, self.interval[1]))) < 0:
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
                    if self.f_x(self.expr, self.interval[0]) == 'Math Error !!!' or self.f_x(self.expr, self.interval[1]) == 'Math Error !!!':
                        print("\nf(" + str(self.interval[0]) + ') = ', end='')
                        print(self.f_x(self.expr, self.interval[0]))
                        print("f(" + str(self.interval[1]) + ') = ', end='')
                        print(self.f_x(self.expr, self.interval[1]))
                        self.find_intervals()
                    if not self.root_exist():
                        self.find_intervals()
                else:
                    self.find_intervals()

                choice = input("Do you want to enter Tolerance ? \n" + Fore.BLUE + " Enter ( y / n ) :  ")
                if choice == 'y':
                    self.Tolerance = float(N(input("Enter the Tolerance (in decimals) : ")))
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
            print(self.f_x(self.expr, self.interval[0]))
            print("f(" + str(self.interval[1]) + ') = ', end='')
            print(self.f_x(self.expr, self.interval[1]))
            self.root_exist()
            print("Tolerance = ", end='')
            print(self.Tolerance)

# Bisection method
            i, j, info = Root_of_Eq.bisection(self, self.expr, self.interval[0], self.interval[1], self.Tolerance, True)
            if i is None:
                print('f(x) does not change sign in ' + str(self.interval))
            else:
                print('The root is', i, 'found in', j, 'iterations')
                print('f(%g)=%g' % (i, self.f_x(self.expr, i)))
                header = ["no.", "a", "b", "p", "f(p)", "Pn-Pn-1"]
                print(tabulate(info, header, tablefmt="fancy_grid", showindex=True))
                print('Bisection Root is = ' + str(i))
# False Position / Regula Falsi Method
            x, info = Root_of_Eq.regulaFalsi(self, self.expr, self.interval[0], self.interval[1], self.Tolerance, store=True)
            header = ["no.", "a", "b", "p", "f(p)", "Pn-Pn-1"]
            print(tabulate(info, header, tablefmt="fancy_grid", showindex=True))
            print('Regula Falsi Root is = ' + str(x))
# Newton method
            p0 = (self.interval[0]+self.interval[1])/2
            dg = diff(self.expr, Equation.x)
            x, info = Root_of_Eq.newton(self, self.expr, p0, dg, store=True)
            header = ["n", "p", "f(p)", "Pn-Pn-1"]
            text = tabulate(info, header, tablefmt="fancy_grid", showindex=True)
            print(text)
            print('Newton Root is = ' + str(x))
# Secant method
            x, info = Root_of_Eq.secant(self, self.expr, self.interval[0], self.interval[1], self.Tolerance, store=True)
            header = ["no.", "a", "b", "p", "f(p)", "Pn-Pn-1"]
            print(tabulate(info, header, tablefmt="fancy_grid", showindex=True))
            print('Secant Root is = ' + str(x))
# Fixed point Method
#             x, info = Root_of_Eq.fixed_point_iteration(self, self.expr, (self.interval[0]+self.interval[1])/2, self.Tolerance, store=True)
#             header = ["no.", "p", "Pn-Pn-1"]
#             print(tabulate(info, header, tablefmt="fancy_grid", showindex=True))
#             print('Fixed point Root is = ' + str(x))

    def find_intervals(self):       # To find best interval if user has not provided any interval .
        self.interval.clear()       # Range to find the intervals in between(to be added in future )
        for i in range(1, 20):
            if self.f_x(self.expr, i) != zoo and self.f_x(self.expr, i + 1) != zoo:
                if float(self.f_x(self.expr, i)) * float(self.f_x(self.expr, i+1)) < 0:  # f(a) * f(b) < 0
                    self.interval.insert(0, i)
                    self.interval.insert(1, i+1)
                    break
            else:
                continue
        if not self.interval:
            print(Fore.RED + "\n\t\t Cannot Find Valid Intervals for the given Expression !!! ")
            exit()

