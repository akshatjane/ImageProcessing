import statistics , numpy , matplotlib.image as img , sys
src=sys.argv[1]
xoffset=int(sys.argv[2])
yoffset=int(sys.argv[3])
nimg=img.imread(src)
w,h=nimg.shape[:2]
temp=numpy.zeros([w,h,3],dtype=numpy.uint8)
i=0
while i<w-xoffset:
    j=0
    while j<h-yoffset:
        temp[i+xoffset][j+yoffset]=nimg[i][j]
        j+=1
    i+=1

img.imsave("tdog.jpg",temp)
