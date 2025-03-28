"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: pprime
"""
fin=open("pprime.in","r")
fout=open("pprime.out","w")
r=fin.readline().strip("\n").split(' ')
print(r)
def pcheck(num):
    if num <= 1:
        return False
    for i in range(2, (int((num)**0.5)) + 1):
        if num % i == 0:
            return False
    return True
pal=[]
leg=[1,3,5,7,9]
def genpal():
    for i in leg:
        pal.append(i)
    for i in leg:
        pal.append(i*10+i)
    for i in leg:
        for j in range(10):
            pal.append(i*100+j*10+i)
    for i in leg:
        for j in range(10):
            pal.append(i*1000+j*100+j*10+i)
    for i in leg:
        for j in range(10):
            for k in range(10):
                pal.append(i*10000+j*1000+k*100+j*10+i)
    for i in leg:
        for j in range(10):
            for k in range(10):
                pal.append(i*100000+j*10000+k*1000+k*100+j*10+i)
    for i in leg:
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    pal.append(i*1000000+j*100000+k*10000+l*1000+k*100+j*10+i)
    

def palcheck(n):
    if len(n)==1:
        return True
    for i in range(len(n)):
        if not n[i]==n[len(n)-1-i]:
            return False
    return True
sol=set()
genpal()
for i in pal:
    if i>int(r[1]):
        print(i)
        break
    if i>=int(r[0]):
        if pcheck(i):
            fout.write(str(i)+"\n")
fout.close()
