"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: combo
"""
fin=open("combo.in","r")
fout=open("combo.out","w")
num=int(fin.readline().strip('\n'))
reg=fin.readline().strip('\n').split(' ')
master=fin.readline().strip('\n').split(' ')
sol=[]
ans=0
for i in range(3):
    reg[i]=int(reg[i])-1
    master[i]=int(master[i])-1    
for a in range(-2,3):
    for b in range(-2,3):
        for c in range(-2,3):
            if [(reg[0]+a)%num,(reg[1]+b)%num,(reg[2]+c)%num] not in sol:
                sol.append([(reg[0]+a)%num,(reg[1]+b)%num,(reg[2]+c)%num])
                ans=ans+1
for a in range(-2,3):
    for b in range(-2,3):
        for c in range(-2,3):
            if [(master[0]+a)%num,(master[1]+b)%num,(master[2]+c)%num] not in sol:
                sol.append([(master[0]+a)%num,(master[1]+b)%num,(master[2]+c)%num])
                ans=ans+1
fout.write(str(ans)+"\n")