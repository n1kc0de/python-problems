"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: milk
"""
fin=open('milk.in','r')
fout=open('milk.out','w')
info=fin.readline().strip('\n').split(' ')
farm=[]
cost=0
for i in range(int(info[1])):
    farm.append(fin.readline().strip('\n').split(' '))
for i in range(len(farm)):
    farm[i][0]=int(farm[i][0]) 
    farm[i][1]=int(farm[i][1])      
farm=sorted(farm,key=lambda x: x[0])
print(farm)
while int(info[0])>0:
    if int(farm[0][1])<=int(info[0]):
        cost=cost+int(farm[0][0])*int(farm[0][1])
        info[0]=int(info[0])-int(farm[0][1])
        del farm[0]
    else:
        cost=cost+int(farm[0][0])*int(info[0])
        info[0]='0'
        del farm[0]
fout.write(str(cost)+"\n")
fout.close