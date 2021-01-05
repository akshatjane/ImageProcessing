#translate
import matplotlib.image as img
a=img.imread("Sample.png")
w,h=a.shape[:2]
print(w)
print(h)
import numpy as np
b=np.zeros([w,h,3])
xTranslate=250;
yTranslate=500;
import statistics as stits
for i in range(0,w-1-xTranslate):
 for j in range(0,h-1-yTranslate):
  b[i+xTranslate][j+yTranslate][0]=a[i][j][0];
  b[i+xTranslate][j+yTranslate][1]=a[i][j][1];
  b[i+xTranslate][j+yTranslate][2]=a[i][j][2];  
img.imsave('shine6.png',b)



