"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: sprime
"""
fin=open("sprime.in","r")
fout=open("sprime.out","w")
r=int(fin.readline().strip("\n"))
print(r)
def pcheck(num):
    if num <= 1:
        return False
    for i in range(2, (int((num)**0.5)) + 1):
        if num % i == 0:
            return False
    return True
initial=[2,3,5,7]
odd=set()
odd.add(1)
odd.add(3)
odd.add(5)
odd.add(7)
odd.add(9)
while len(str(initial[0]))<r:
    for i in odd:
        if pcheck(initial[0]*10+i):
            initial.append(initial[0]*10+i)
    initial.remove(initial[0])

    pass
for i in initial:
    fout.write(str(i)+"\n")