import numpy as np
import pylab as py

X = [2,10,20]
Y = [1,4,9]

py.xlabel('sample number')
py.ylabel(' Readings')
py.title('PH Readings')
py.plot(X,Y,'r')
py.show()
