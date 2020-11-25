import matplotlib.pyplot as plt

f=open(input())
N=int(f.readline())
x=[]
y=[]
for i in range(N):
    a=f.readline().split()
    x.append(float(a[0]))
    y.append(float(a[1]))

plt.scatter(x,y)
plt.title('Number of points: {0}'.format(N))

plt.show()