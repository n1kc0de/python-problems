"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: friday
"""

file = open('friday.in','r') 
fout = open('friday.out','w') 
year=int(file.readline())
weeks=[0,0,0,0,0,0,0]
lpcnt=0
def hmy(a,lpcnt):
    weeks[((a-1900)%7+lpcnt)%7]+=1
    weeks[((a-1900)%7+3+lpcnt)%7]+=1
    if ((a-1900)%4==0 and (a-1900)%100!=0): 
        lpcnt=lpcnt+1
    if (a%400==0):
        lpcnt=lpcnt+1
    weeks[((a-1900)%7+3+lpcnt)%7]+=1
    weeks[((a-1900)%7+6+lpcnt)%7]+=1
    weeks[((a-1900)%7+1+lpcnt)%7]+=1
    weeks[((a-1900)%7+4+lpcnt)%7]+=1
    weeks[((a-1900)%7+6+lpcnt)%7]+=1
    weeks[((a-1900)%7+2+lpcnt)%7]+=1
    weeks[((a-1900)%7+5+lpcnt)%7]+=1
    weeks[((a-1900)%7+lpcnt)%7]+=1
    weeks[((a-1900)%7+3+lpcnt)%7]+=1
    weeks[((a-1900)%7+5+lpcnt)%7]+=1
    return lpcnt
for i in range(year):
    lpcnt=hmy(1900+i,lpcnt)
fout.write(str(weeks[0])+" "+str(weeks[1])+" "+str(weeks[2])+" "+str(weeks[3])+" "+str(weeks[4])+" "+str(weeks[5])+" "+str(weeks[6])+"\n")
fout.close