import matplotlib.image as img
a=img.imread("sample.png")
w,h=a.shape[:2]
import numpy as np
b=np.zeros([w,h,3])
print(w)
print(h)
xTranslate=0;
yTranslate=100;
for i in range(xTranslate,w-xTranslate):
 for j in range(yTranslate,h-yTranslate):
  b[i+xTranslate][j+yTranslate][0]=a[i][j][0];
  b[i+xTranslate][j+yTranslate][1]=a[i][j][1];
  b[i+xTranslate][j+yTranslate][2]=a[i][j][2];  
img.imsave('shine8.png',b)



