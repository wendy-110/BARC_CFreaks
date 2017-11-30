import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull

#initialize variables
image_list=[]
path_width = 5
nR = 8
nC = 10

# forward pass
for x in range(int(nR/2)):
    #define image_row
    image_row = np.zeros(nC)
    #forward pass
    if x+path_width > nC:
        for index in range(x,nC):
            image_row[index] = 1
    else:
        for index in range(x,x+path_width):
                image_row[index] = 1
    image_list.append(image_row)

# stack and flip
image_all = np.vstack(image_list)
image_flip = np.flipud(image_all)
image_all = np.vstack((image_all,image_flip))

# determine row and column indicies
outline = (np.diff(np.sign(image_all)) != 0)*1

indexes = np.where(outline == 1)
points1 = np.transpose(np.vstack(indexes))

# determine convex hull from points
hull = ConvexHull(points1)

# Plot convex hull
import matplotlib.pyplot as plt
plt.plot(points1[hull.vertices,0], points1[hull.vertices,1], 'r--', lw=2)
plt.plot(points1[hull.vertices[0],0], points1[hull.vertices[0],1], 'ro')
plt.show()

# constraints from hull
hull.equations
