"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: barn1
"""
fin=open('barn1.in','r')
fout=open('barn1.out','w')
info=fin.readline().strip('\n').split(' ')
bn=int(info[2])
mxb=int(info[0])
ocs=int(info[1])
board=[]
for i in range(bn):
    board.append(int(fin.readline().strip('\n')))
board=sorted(board)
print(board)
def initialcheck():
    prevb=[]
    for i in range(bn):
        if len(prevb)>0:
            if board[i]-1==prevb[len(prevb)-1][len(prevb[len(prevb)-1])-1]:
                prevb[len(prevb)-1].append(board[i])
            else:
                prevb.append([board[i]])  
        else: 
            prevb.append([board[i]])
    return(prevb)
b=initialcheck()
if len(initialcheck())>mxb:
    b=initialcheck()
    cur=0
    op=False
    run=True
    while run and cur<1000:
        if op==False:
            cur=cur+1
        op=False
        fr=True
        i=0
        while fr and run:
            i=i+1
            br=0
            print(i)
            print(len(b))
            if i==len(b):
                fr=False
            else:
                print(i)
                if b[i-1][len(b[i-1])-1]==b[i][0]-cur:
                    b[i-1]=b[i-1]+b[i]
                    del b[i]
                    print('yes')
                    i=i-1
                    op=True
                    if len(b)<=mxb:
                        run=False
                        break
num=0
if mxb==1:
    num=board[len(board)-1]-board[0]+1
elif mxb>=len(board):
    num=len(board)
else:
    for i in range(len(b)):
        num=num+b[i][len(b[i])-1]-b[i][0]+1
fout.write(str(num)+"\n")
fout.close
