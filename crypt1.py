"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: crypt1
"""
fin=open('crypt1.in','r')
fout=open('crypt1.out','w')
n=int(fin.readline().strip('\n'))
digits=sorted(fin.readline().strip('\n').split(' '))
store=[]
for i in range(n):
    digits[i]=int(digits[i])
    store.append(int(digits[i]))
print(digits)
def combination(l):
    temp=[]
    for a in l:
        for b in digits:
            temp.append(int(str(a)+str(b)))
    return(temp)
def check(number):
    ret=True
    for i in range(len(str(number))):
        if not int(str(number)[i]) in digits:
            ret=False
    return ret
for i in range(4):
    store=combination(store)
solution=0
for i in store:
    v=0
    n1=int(str(i)[:2])
    n2=int(str(i)[-3:])
    p1=int(str(n1)[0])*n2
    p2=int(str(n1)[1])*n2
    if check(p1) and check(p2) and check(n1*n2) and len(str(p1))<4 and len(str(p2))<4 and n1*n2<100000:
        solution=solution+1
        print(str(n1)+" "+str(n2))
fout.write(str(solution)+"\n")