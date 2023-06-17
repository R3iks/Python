import os 
import math

import numpy as np


#as keyword is alias
import area as ar 

#from keyword to import specific function(s)
from perimeter import circle, rectangle


print("Area of a circle is {}".format(area.circle(10))) # string format

print(f"Area is {area.circle(10)}") # f string

print ("Area is %d" %(area.circle(10))) # older format

print(f"Perimeter of a circle is {circle(10)}")

