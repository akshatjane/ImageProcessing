import matplotlib.image as img
a=img.imread("sample.png")
h,w=a.shape[:2]
#img.getpixel((h,w))
import numpy as np
b=np.zeros([h,w,3])
print(w)
print(h)
xTranslate=100;
yTranslate=0;
for i in range(xTranslate,h-xTranslate):
 for j in range(yTranslate,w-yTranslate):
  b[i+xTranslate][j+yTranslate][0]=a[i][j][0];
  b[i+xTranslate][j+yTranslate][1]=a[i][j][1];
  b[i+xTranslate][j+yTranslate][2]=a[i][j][2];  
img.imsave('shine10.png',b)



