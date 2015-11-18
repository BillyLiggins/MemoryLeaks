import matplotlib.pyplot as plt

import pylab

fig=plt.figure()


data = pylab.loadtxt("memoryData.dat")
print data
pylab.plot( data[1:])

pylab.legend()
pylab.title("Memory over time")
pylab.xlabel("Time (30 sec steps)")
pylab.ylabel("Memory Usage (Gb)")
pylab.show()
