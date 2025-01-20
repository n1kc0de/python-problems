"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: skidesign
"""
fin=open('skidesign.in','r')
fout=open('skidesign.out','w')
num=int(fin.readline().strip('\n'))
hills=[]
prices=[]
def wincheck():
    if hills[num-1]-hills[0]<=17:
        return True
def hillfind():
    a = 0 
    b = 0  
    num1 = hills[0]
    num2 = hills[num - 1]
    iter = 0
    run = True
    while run:
        iter += 1
        if iter == num:
            break  
        if num1 == hills[iter]:
            a += 1
        else:
            run = False
    iter = 0
    run = True
    while run:
        iter += 1
        if iter == num:
            break 
        if num2 == hills[num - 1 - iter]:
            b += 1
        else:
            run = False
    for i in range(a + 1):
        hills[i] += 1
        prices[i] += 1
    price=0
    for i in prices:
        price=price+i*i
    aval=price
    for i in range(a + 1):
        hills[i] -= 1
        prices[i] -= 1
    for i in range(b + 1):
        hills[num - 1 - i] -= 1
        prices[num - 1 - i] += 1
    price=0
    for i in prices:
        price=price+i*i
    bval=price
    for i in range(b + 1):
        hills[num - 1 - i] += 1
        prices[num - 1 - i] -= 1
    if bval>aval:
        for i in range(a+1):
            hills[i] += 1
            prices[i] += 1  
        return False
    if aval>bval:
        for i in range(b+1):
            hills[num - 1 - i] -= 1
            prices[num - 1 - i] += 1
        return False
    if aval==bval:
        for i in range(b+1):
            hills[num - 1 - i] -= 1
            prices[num - 1 - i] += 1
        return False
    return False
    
for i in range(num):
    hills.append(int(fin.readline().strip('\n')))
    prices.append(0)
hills=sorted(hills)
while not wincheck():
    hillfind()
print(hills)
price=0
print(prices)
for i in prices:
    price=price+i*i
fout.write(str(price)+"\n")  
fout.close() 

