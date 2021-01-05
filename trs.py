#translate image
import matplotlib.image as img
import numpy as np
a=img.imread("sample.png")
w,h=a.shape[:2]
k=np.zeros([w,h,3])
x=int(input("Enter x-offset :"))
y=int(input("Enter y-offset :"))
for i in range(0,w-1-x):
 for j in range(0,h-1-y):
  k[i+x][j+y][0]=a[i][j][0]
  k[i+x][j+y][1]=a[i][j][1]
  k[i+x][j+y][2]=a[i][j][2]
img.imsave('type.png',k)