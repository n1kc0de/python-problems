"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: milk3
"""
change=0
fin=open('milk3.in',"r")
op=fin.readline().strip('\n').split(' ')
for i in range(len(op)):
    op[i]=int(op[i])
print(op)
perm=[[0,0,op[2]]]
def combcheck(cur,a,b):
    global change
    t=[perm[cur][0],perm[cur][1],perm[cur][2]]
    if perm[cur][a]<=op[b]-perm[cur][b]:
        t[b]=perm[cur][b]+perm[cur][a]
        t[a]=0
    else:
        t[b]=op[b]
        print('k')
        print(-(op[b]-perm[cur][b]))
        t[a]=perm[cur][a]-(op[b]-perm[cur][b])
    if t not in perm:
        perm.append(t)
        change=1
    print(t)
def permcreate():
    global change
    change=0
    for i in range(len(perm)):
        combcheck(i,2,1)
        combcheck(i,0,1)
        combcheck(i,1,0)
        combcheck(i,2,0)
        combcheck(i,0,2)
        combcheck(i,1,2)
    if change==1:
        return True
num=0
while permcreate():
    num+=1
sol=[]
for i in range(len(perm)):
    if perm[i][0]==0 and perm[i][2] not in sol:
        sol.append(perm[i][2])
sol.sort()
print(sol)
a=str(sol[0])
for i in range(1,len(sol)):
    a=a+" "+str(sol[i])
fout=open('milk3.out','w')
fout.write(a+"\n")
fout.close