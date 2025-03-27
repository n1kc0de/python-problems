"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: numtri
"""
fin=open("numtri.in","r")
fout=open("numtri.out","w")
s=[]
for i in range(int(fin.readline().strip("\n"))):
    s.append(fin.readline().strip('\n').split(' '))
def down():
    if len(s)>1:
        for i in range(len(s[1])):
            if i==0:
                s[1][i]=int(s[1][i])+int(s[0][i])
            if i==len(s[1])-1:
                s[1][i]=int(s[1][i])+int(s[0][i-1])
            if not i==0 and not i==len(s[1])-1:
                s[1][i]=int(s[1][i])+max(int(s[0][i-1]),int(s[0][i]))
        s.pop(0)
        return True
    else: 
        return False
while down():
    pass
m=0
for i in s[0]:
    if int(i)>m:
        m=i
fout.write(str(m)+"\n")
