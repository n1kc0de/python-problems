"""
ID: nikhil tharakan [nikhil3]
LANG: PYTHON3
TASK: milk2
"""
def attempt2():
    fin=open("milk2.in","r")
    fout=open("milk2.out","w")
    num=int((fin.readline()).rstrip('\n'))
    time=[]
    tnr=[]
    for i in range(num):
        line = fin.readline().rstrip('\n').split(' ')
        integer_line = [int(x) for x in line]
        time.append(integer_line)
    time=sorted(time, key=lambda row: row[0])
    print(time)
    mnt=0
    tnr.append(time[0])
    mxt=int(tnr[0][1])-int(tnr[0][0])
    for i in range(num):
        exit=False
        for j in range(len(tnr)-1,len(tnr)):
            if int(tnr[j][0])<=int(time[i][0]) and int(tnr[j][1])>=int(time[i][0]) and int(tnr[j][1])<=int(time[i][1]):
                tnr[j][1]=time[i][1]
            elif int(tnr[j][1])<int(time[i][0]) and int(tnr[j][1])<int(time[i][1]):
                exit=True
        if exit:
            tnr.append(time[i])
    mxt=0
    mnt=0
    for i in range(len(tnr)):
        if (int(tnr[i][1])-int(tnr[i][0]))>mxt:
            mxt=int(tnr[i][1])-int(tnr[i][0])
        if i!=len(tnr)-1:
            if (int(tnr[i+1][0])-int(tnr[i][1]))>mnt:
                mnt=int(tnr[i+1][0])-int(tnr[i][1])
    print(tnr)
    if len(tnr)!=1:
        if int(tnr[len(tnr)-1][0])-int(tnr[len(tnr)-2][1])>mnt:
            mnt=int(tnr[len(tnr)-1][0])-int(tnr[len(tnr)-2][1])
    print(str(mxt)+" "+str(mnt)+'\n')
    fout.write(str(mxt)+" "+str(mnt)+'\n')
    fout.close
attempt2()
