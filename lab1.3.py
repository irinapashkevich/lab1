import matplotlib.pyplot as plt

f=open(input())

prep=[]
group=[]
p_gr=[]
g_gr=[]

for line in f:
    a=line.split()
    a[2]=int(a[2])

    if prep.count(a[0])==0:
        prep.append(a[0])
        b=[0]*11
        b[a[2]]=1
        p_gr.append(b)
    else:
        p_gr[prep.index(a[0])][a[2]]+=1

    if group.count(a[1])==0:
        group.append(a[1])
        b=[0]*11
        b[a[2]]=1
        g_gr.append(b)
    else:
        g_gr[group.index(a[1])][a[2]]+=1

grades=[0,1,2,3,4,5,6,7,8,9,10]

fig, axes1 = plt.subplots(figsize=(len(prep)*2,3),nrows=1,ncols=len(prep))
for i in range(len(prep)):
    axes1[i].pie(p_gr[i],radius=1)
    axes1[i].set_title('prep {0}'.format(i+1))
plt.legend(grades,loc="center right",bbox_to_anchor=(1.2, 0, 0.5, 1))
#plt.show()

fig, axes2 = plt.subplots(figsize=(len(group)*2,3),nrows=1,ncols=len(group))
for i in range(len(group)):
    axes2[i].pie(p_gr[i],radius=1)
    axes2[i].set_title('group {0}'.format(i+1))
plt.legend(grades,loc="center right",bbox_to_anchor=(1.2, 0, 0.5, 1))

h_prep=-1
nh_prep=-1
razd_g=-1
max_b=-1
min_b=11
for i in range(len(prep)):
    n=0
    sum=0
    for j in range(11):
        n+=p_gr[i][j]
        sum+=p_gr[i][j]*j
    sr=sum*1.0/n
    if sr>max_b:
        max_b=sr
        h_prep=i
    if sr<min_b:
        min_b=sr
        nh_prep=i

min_b=11
for i in range(len(group)):
    n=0
    sum=0
    for j in range(11):
        n+=g_gr[i][j]
        sum+=g_gr[i][j]
    sr=sum*1.0/n
    if sr<min_b:
        min_b=sr
        razd_g=i

print("holjavnij prep: ", h_prep+1)
print("neholjavnij prep: ", nh_prep+1)
print("razdolbajskaja gruppa: ", razd_g+1)

plt.show()