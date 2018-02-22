print("Modules, (c) Verloka Vadim 2018\n\n\n")

import math             #Импортирование модуля math
import random as rnd    #Импорт модуля random и присвоение ему псевдонима rnd

print("math: {}".format(math.e))
print("rnadom: {}".format(rnd.random()))

from math import cos            #Импортирование однго методо из модуля
from math import sin as s       #Импортирование однго методо из модуля
                                #и присвоение ему псевдонима
from math import (sinh,cosh)    #Импортирование нескольких методов из модуля

print("cos: {}".format(cos(45)))
print("sin: {}".format(s(180)))
print("sinh: {}".format(sinh(180)))
print("cosh: {}".format(cosh(45)))

from sys import *        #Импортирование всех методов из модуля

print("sys: {}".format(path))

#my own modules

import ownmodule

ownmodule.hello()
ownmodule.world("suck")
print("A: {} || B: {}".format(ownmodule.A, ownmodule.B))

import ownmodule2