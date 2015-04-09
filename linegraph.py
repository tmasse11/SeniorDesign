import numpy
import pylab 

data=numpy.array(numpy.random.rand(10))
y,binEdges = numpy.histogram(data,bins=100)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
pylab.plot(bincenters,y,'-')
pylab.show()
