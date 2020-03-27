import sympy as sp  # for Maths Expression handling
import numpy as np
import scipy as sc
import matplotlib as mp
import math
import errno
from sympy import *

x, e = sp.symbols('x e')
car = [0, 1]
car.remove(0)
# car.(0, sp.nsimplify(input("enter an interval : ")))
print(car)
# f = sp.nsimplify(input("enter an exp : "))
# g = sp.nsimplify(input("enter an interval : "))
# pprint(N(f.subs(e, math.e).subs(x, 1)))
# 3*x+sin(x)-e**x