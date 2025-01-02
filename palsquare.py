"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: palsquare
"""
num=["0",'1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
fin=open('palsquare.in','r')
fout=open('palsquare.out','w')
base=int(fin.readline().strip(' '))
pd=[]
cpd=[]
def baseconvert(reg,conv):
    if reg==0:
        return 0
    digits=''
    while reg:
        digits=str(num[int(reg % conv)])+digits
        reg = reg//conv
    return digits
def palcheck(n):
    if len(n)==1:
        return True
    for i in range(len(n)):
        if not n[i]==n[len(n)-1-i]:
            return False
    return True
for i in range(0,301):
    if palcheck(str(baseconvert(i*i,base))) and i!=0:
        fout.write(str(baseconvert(i,base))+" "+str(baseconvert(i*i,base))+'\n')