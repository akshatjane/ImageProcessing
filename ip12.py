import numpy as np;
import matplotlib.image as img;
a=np.zeros([256,256,3]);
b=np.zeros([256,256,3]);
for i in range(256):
 for j in range(256):
  a[i][j][0]=256-255;
  a[i][j][1]=256-255;
  a[i][j][2]=256-(255-j);
  b[i][j][0]=256-(255-j);
  b[i][j][1]=256-(255-j);
  b[i][j][2]=256-1;
c=np.concatenate((a,b),axis=1)
img.imsave("shine12.jpg",c);
