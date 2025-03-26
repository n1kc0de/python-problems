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
def calcbisq():
    bisquares=set()
    for i in range(lim+1):
        for j in range(i,lim+1):
            bisquares.add(i**2+j**2)
    isbsq=[False]*135001
    for i in bisquares:
        isbsq[i]=True
    return bisquares, isbsq
bsq,chbsq=calcbisq()
sol=[]
cheese=1
if length>=10:
    cheese=12
if length>=12:
    cheese=84
step=cheese
while step*(length-1)<=farth:
    for j in bsq:
        w=True
        for i in range(length):
            if chbsq[j+i*step]:
                pass
            else:
                w=False
                break
        if w==True:
            sol.append([j,step])
    step+=cheese
for a in sol:
    fout.write(str(a[0])+" "+str(a[1])+"\n")
if len(sol)==0:
    fout.write("NONE"+"\n")
fout.close()
        
