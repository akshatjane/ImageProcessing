import numpy as np
import matplotlib.image as img
import statistics as stits
a=img.imread("Sample.png")
h,w=a.shape[:2]
k=np.zeros([h,w,3])
for i in range(0,h):
 for j in range(0,w):
  n=[a[i][j][0],a[i][j][1],a[i][j][2]]
  m=int(stits.mean(n))
  k[i][j][0]=int(m)
  k[i][j][1]=int(m)
  k[i][j][2]=int(m)
img.imsave('test.png',k)