'''
nmount=int(input())
num=[]
for i in range(nmount):
    num.append(int(input()))
'''
nmount=4
num=[1,100,4567,3366]
anstore=[]
num.sort(reverse=True)
def rounds(number):
    return round(number/10)*10
def chainround(i):
    pwst=len(str(i))-1
    plc=list(str(i))
    for i in range(pwst):
        if int(plc[pwst-i])>=5:
            if  int(plc[pwst-i-1])<9:
                plc[pwst-i-1]=int(plc[pwst-i-1])+1
            else:
                plc[pwst-i-1]=0
                plc.insert(0,'1')

            plc[pwst-i]='0'
        else:
            plc[pwst-i]='0'
    if int(plc[0])>=5:
        plc.insert(0,'1')
        plc[1]='0'
    if pwst>1:
        return(int("".join(plc)))
    else:
        return(int(plc[0]))
print(chainround(99))