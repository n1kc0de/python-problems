"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: beads
"""
#wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
file = open('beads.in', 'r')
fout = open('beads.out', 'w')
num = int(file.readline())
text = file.readline()
text = text.rstrip('\n')
text = text + text + text
print(text)
lsl=0
for i in range (num,num*2):
    tmx=1
    sm=True
    it=1
    strt=text[i]
    if text[i]=="w":
        strt=text[i-it]
    while sm:
        if  (i-it)>0:
            if (text[i-it]==strt or text[i-it]=="w"):
                it=it+1
                tmx=tmx+1
            else:
                sm=False
        else:
            sm=False
    tmn=0
    sm=True
    it=1
    while sm:
        if (i+it)<len(text):
            if (text[i+it]==text[i+1] or text[i+it]=="w"):
                it=it+1
                tmn=tmn+1
            else:
                sm=False
        else:
            sm=False
    if (tmx+tmn)>=lsl:
        lsl=tmx+tmn
if num<lsl:
    lsl=num
print(lsl)
fout.write(str(lsl)+'\n')
fout.close