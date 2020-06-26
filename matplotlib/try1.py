import matplotlib.pyplot as plt
import numpy

x= numpy.linspace(0,10,1000)
y= numpy.random.randint(1000,size=1000)

plt.plot(x,y,'+')
plt.show()
