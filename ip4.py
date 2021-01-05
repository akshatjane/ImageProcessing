
# Mirror
import matplotlib.image as img
a=img.imread("sample.png")
w,h=a.shape[:2]
print(w,h)
import numpy as np
b=np.zeros([h,w,3])
import statistics as stits
for i in range(0,h-1):
 for j in range(0,w-1):
  b[i][j][0]=a[j][i][0]
  b[i][j][1]=a[j][i][1]
  b[i][j][2]=a[j][i][2]
img.imsave('shine4.png',b)



