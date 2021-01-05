#gray scale
import matplotlib.image as img
a=img.imread("sample.png")
w,h=a.shape[:2]
import numpy as np
b=np.zeros([w,h,3])
import statistics as stits
for i in range(0,w):
 for j in range(0,h):
  k=[a[i][j][0],a[i][j][1],a[i][j][2]]
  z=max(k)
  b[i][j][0]=z
  b[i][j][1]=z
  b[i][j][2]=z
img.imsave('shine2.png',b)



