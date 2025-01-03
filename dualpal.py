"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: dualpal
"""
fin=open('dualpal.in','r')
fout=open('dualpal.out','w')
n=fin.readline().strip('\n').split(" ")
ans=[]
print(n)
num=["0",'1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
def baseconvert(reg,conv):
    if reg==0:
        return 0
    digits=''
    while reg:
        digits=str(num[int(reg%conv)])+digits
        reg = reg//conv
    return digits
def palcheck(n):
    if len(n)==1:
        return True
    for i in range(len(n)):
        if not n[i]==n[len(n)-1-i]:
            return False
    return True
a=int(n[1])
while len(ans)<int(n[0]):
    a+=1
    sol=0
    for i in range(2,11):
        if palcheck(baseconvert(int(a),int(i))):
            sol+=1
    if sol>=2:
        ans.append(a)
print(ans)
for i in ans:
    print(i)
    fout.write(str(i)+"\n")
fout.close
