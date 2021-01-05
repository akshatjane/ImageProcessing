import numpy as np
import matplotlib.image as img
a=np.zeros([256,256,3]);
b=np.zeros([256,256,3]);
c=np.zeros([256,256,3]);
d=np.zeros([256,256,3]);
for i in range(256):
 for j in range(256):
  a[i][j]=[256-255,256-(255-j),256-(255-j)];
  b[i][j]=[256-(255-j),256-1,256-1];
  c[i][j]=[256-255,256-255,256-(255-j)];
  d[i][j]=[256-(255-j),256-(255-j),256-1];
e=np.concatenate((a,b),axis=1)
f=np.concatenate((c,d),axis=1)
z=np.concatenate((e,f),axis=0)
img.imsave("shine13.jpg",z);
