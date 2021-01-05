import matplotlib.image as img
import numpy as np
a=img.imread("sample.png");
j,k=a.shape[:2]
xNew = int(j/2);
yNew = int(k/2);
xScale = xNew/(j-1);
yScale = yNew/(k-1);
b = np.zeros([xNew,yNew,3]);
for i in range(xNew-1):
 for j in range(yNew-1):
  b[i+1,j+1] = a[(1+int(i/xScale)),(1+int(j/yScale))]
img.imsave("shine14.png",b);
