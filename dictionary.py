"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: namenum
"""
dict=open("dict.txt","r")
fin=open("namenum.in","r")
fout=open("namenum.out","w")
#change to /n when you submit
cows=int((fin.readline()).rstrip('\n'))
serln=len(str(cows))
cd=[]
burner=[]
final=[]
e=dict.readlines()
a="a"
b="b"
c="c"
d=[]
for i in range(len(e)):
    if len(e[i])==serln+1:
        g=(e[i]).rstrip('\n')
        d.append(g)
print(d)
def basenum(d):
    global a
    global b
    global c
    if d==2:
        a="a"
        b="b"
        c="c"
    if d==3:
        a="d"
        b="e"
        c="f"
    if d==4:
        a="g"
        b="h"
        c="i"
    if d==5:
        a="j"
        b="k"
        c="l"
    if d==6:
        a="m"
        b="n"
        c="o"
    if d==7:
        a="p"
        b="r"
        c="s" 
    if d==8:
        a="t"
        b="u"
        c="v" 
    if d==9:
        a="w"
        b="x"
        c="y"  
def cdadd(d): 
    global burner
    burner=[]
    basenum(d)
    for i in cd:
        burner.append(i+a)
        burner.append(i+b)
        burner.append(i+c)
    return burner
basenum(int(str(cows)[0]))
cd.append(a)
cd.append(b)
cd.append(c)
for i in range(1,serln):
    cdadd(int(str(cows)[i]))
    cd=burner
print(cd)
for i in cd:
    if i.upper() in d:
        print(True)
        final.append(i.upper())
if len(final)>0:
    for i in final:
        fout.write(i+'\n')
else:
    fout.write('NONE'+'\n')
fout.close