import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.linspace(-1, 1, 50)
# y1 = 2*x + 1
# y2 = 3*x+3
# plt.figure()
# plt.plot(x,y1)
# plt.figure()
# plt.plot(x,y2)
# plt.show()

# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# T = np.arctan2(Y,X)
# plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
# plt.xticks(())
# plt.yticks(())
# plt.show()

fig = plt.figure()
ax = fig.add_axes(Axes3D(fig))
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
plt.show()