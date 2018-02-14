print("Modules, (c) Verloka Vadim 2018\n\n\n")

import math             #import module math
import random as rnd    #import module using pseudoname for him

print("math: {}".format(math.e))
print("rnadom: {}".format(rnd.random()))

from math import cos            #import one method from module
from math import sin as s       #import one method from module using pseudoname
from math import (sinh,cosh)    #import few methods from module

print("cos: {}".format(cos(45)))
print("sin: {}".format(s(180)))
print("sinh: {}".format(sinh(180)))
print("cosh: {}".format(cosh(45)))

from sys import *        #import all methods from module

print("sys: {}".format(path))

#my own modules

import ownmodule

ownmodule.hello()
ownmodule.world("suck")
print("A: {} || B: {}".format(ownmodule.A, ownmodule.B))

import ownmodule2