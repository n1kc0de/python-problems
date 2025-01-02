"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: gift1
"""

file = open('gift1.in','r') 
fout = open('gift1.out','w') 
lines = file.readlines()
people1=[]
money=[]
for i in range(int(lines[0])):
    people1.append(lines[i+1])
    money.append(0)
people = []
for sub in people1:
    people.append(sub.replace("\n", ""))

lines[int(lines[0])+1]
a=int(lines[0])+1
while a<len(lines):
    cur=people1.index(lines[a])
    b=lines[a+1].split(" ")
    if not int(b[1])==0:
        money[cur]+=int(b[0])%int(b[1])-int(b[0])
        divide=(int(b[0])-int(b[0])%int(b[1]))/int(b[1])
        bef=a
        for i in range(int(b[1])):
            money[people1.index(lines[bef+2+i])]+=divide
            a=a+1
    a=a+2
place=0
for i in people:
    fout.write(str(people[place])+' '+str(int(money[place]))+"\n")
    place+=1
fout.close
