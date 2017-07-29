from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
import random
#filename = raw_input()
#filename  = str(filename)


points=[]
color=['b-','g-','r-','c-','m-','y-','k-']
for i in xrange(1,100):
	points.append([random.uniform(1,10000),random.uniform(1,10000)])
points=np.array(points)
plt.plot(points[:,0], points[:,1], 'o')
plt.show(block=False)
for i in xrange(10):
	flag=[0 for i in xrange(len(points))]
	if len(points)<3:
		break
	hull = ConvexHull(points)
	for simplex in hull.simplices:
		plt.plot(points[simplex, 0], points[simplex, 1], color[i%7])
	plt.draw()
	plt.pause(0.1)
	hull_indices = hull.vertices
	for i in hull_indices:
		flag[i]=1
	cpy=[]
	for i in xrange(len(points)):
		if flag[i]!=1:
			cpy.append(points[i])
	cpy=np.array(cpy)
	points=cpy
plt.show()
#if k==27 or k==-1:
#  cv2.destroyAllWindows()
