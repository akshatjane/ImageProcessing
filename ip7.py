import matplotlib.image as img
a=img.imread("sample.png")
w,h=a.shape[:2]
import numpy as np
b=np.zeros([w,h,3])
for i in range(w):
 for j in range(h):
  new=(0.3*a[i][j][0]+0.59*a[i][j][1]+0.11*a[i][j][2])
  newRed = int(new * 2)
  if newRed > 255:
   newRed = 255
  newGreen = int(new * 1.5)
  if newGreen > 255:
   newGreen = 255
  newBlue = int(new)
  if newBlue > 255:
   newBlue = 255
  b[i][j][0]=newGreen;
  b[i][j][1]=newRed;
  b[i][j][2]=newBlue;
img.imsave('shine7.png',b)



