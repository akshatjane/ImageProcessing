#gray scale
import matplotlib.image as img
a=img.imread("sample.jpg")
w,h=a.shape[:2]
import numpy as np
b=np.zeros([w,h,3])
import statistics as stits
for i in range(0,w):
 for j in range(0,h):
  n=[a[i][j][0],a[i][j][1],a[i][j][2]]
  k=int(stits.mean(n))
  b[i][j][0]=int(k)
  b[i][j][1]=int(k)
  b[i][j][2]=int(k)
img.imsave('shine1.jpg',b)



