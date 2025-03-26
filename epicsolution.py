"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: ariprog
"""
fin=open('ariprog.in','r')
fout=open('ariprog.out','w')
length = int(fin.readline().strip('\n'))
n = int(fin.readline().strip('\n'))
def bisquares(n):
    bisquares = []
    for i in range(0, n+1):
        for j in range(i, n+1):
            bisquares.append(i**2 + j**2)
    return bisquares
bisquares = list(set(bisquares(n)))
bisquares.sort()
# turn bisquares into hashmap, with key as index and value as the bisquare


checkifinbisquares = lambda x: x in bisquares

start = 1
if length > 6:
    start = 4
if length > 10:
    start = 12
if length >12:
    start = 84

output=[]
for diff in range(start, bisquares[-1] - bisquares[0],start):
    for i in range(0, len(bisquares)):
        if (bisquares[i],diff) in output:
            continue
        count = 0
        # see how long a sequence of form bisquares[i] + diff*k is in the bisquares list
        while bisquares[i] + diff*(length-1) <= bisquares[-1] and checkifinbisquares(bisquares[i] + diff*count):
            count += 1
        
        if count >= length:
            for j in range(count-length+1):
                print(bisquares[i] + diff*j, diff)
                output.append(str(bisquares[i] + diff*j)+" "+str(diff)+"\n")
print(output)
for i in output:
    fout.write(i)
fout.close()