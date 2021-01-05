import matplotlib.image as img ,sys,numpy

m=img.imread(sys.argv[1])
dst=sys.argv[2]
xoffset=int(sys.argv[3])
yoffset=int(sys.argv[4])
twidth=int(sys.argv[5])
theight=int(sys.argv[6])
temp=numpy.zeros([twidth,theight,3],dtype=numpy.uint8)
i=0
j=0
while i<twidth:
    j=0
    while j<theight:
        temp[i][j,0]=m[xoffset+i][yoffset+j,0]
        temp[i][j,1]=m[xoffset+i][yoffset+j,1]
        temp[i][j,2]=m[xoffset+i][yoffset+j,2]
        j+=1
    i+=1

img.imsave(dst,temp)
