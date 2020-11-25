import matplotlib.pyplot as plt
import math

f=open(input())
x=[]
y=[]
k=0
for line in f:
    if k%2==0:
        x.append(line.split())
    else:
        y.append(line.split())
    k+=1

N=len(x)

for i in range(N):
    for j in range(len(x[i])):
        x[i][j]=float(x[i][j])
        y[i][j]=float(y[i][j])

b=math.sqrt(N)
b=int(b//1)
a=N//b
if a*b<N:
    a+=1

xx=0
yy=0

fig, axes = plt.subplots(nrows=b,ncols=a,sharex=True, sharey=True)
for i in range(N):
    axes[yy,xx].set()
    axes[yy,xx].plot(x[i],y[i])
    axes[yy,xx].set_title('Graph {0}'.format(i+1))
    axes[yy,xx].grid()
    xx+=1
    if xx>=a:
        yy+=1
        xx=0

plt.show()