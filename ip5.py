import matplotlib.image as img
a=img.imread("sample.png")
w,h=a.shape[:2]
import numpy as np
b=np.zeros([w,h,3])
import statistics as stits
for i in range(0,w):
 for j in range(0,h):
  b[i][j][0]=a[i][j][0];
  b[i][j][1]=a[i][j][1];
  b[i][j][2]=a[i][j][2];
img.imsave('shine5.png',b)



