"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: ariprog
"""
fin=open('ariprog.in','r')
fout=open('ariprog.out','w')
length=int(fin.readline().strip('\n'))
lim=int(fin.readline().strip('\n'))
farth=2*lim**2
def bisqchk(n,max):
    iter=max
    alt=n
    sol=False
    while iter>=0:
        if (alt-iter**2)>=0:
            if ((alt-iter**2)**0.5).is_integer() and (alt-iter**2)**0.5<=max:
                sol=True
                iter=-1
                break
        iter=iter-1
    return(sol)
cheese=1
if length>=12:
    cheese=84
dif=cheese
ans=[]
work=[]
for test in range(farth+1):
    if bisqchk(test,lim):
        work.append(test)
work.sort()
a=0
while dif*(length-1)<=work[len(work)-1]:
    print(dif)
    alpha=work.copy()
    for i in alpha:
        works=True
        for test in range(length):
            a=a+1
            if  i+test*dif not in work:
                works=False
                for b in range(1,test):
                    alpha.remove(i+b*dif)
                break
        if works==True:
            ans.append([i,dif])
    dif=dif+cheese
print(ans)
for a in ans:
    fout.write(str(a[0])+" "+str(a[1])+"\n")
if len(ans)==0:
    fout.write("NONE"+"\n")
fout.close()
