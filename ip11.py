import numpy as np
import matplotlib.image as img
b=np.zeros([256,256,3]);
a=np.zeros([256,256,3]);
for i in range(256):
 for j in range(256):
  a[i][j][0]=256-255;
  a[i][j][1]=256-(255-j);
  a[i][j][2]=256-(255-j);
  b[i][j][0]=256-(255-j);
  b[i][j][1]=256-1;
  b[i][j][2]=256-1;
c=np.concatenate((a,b),axis=1)
img.imsave("shine11.jpg",c);
