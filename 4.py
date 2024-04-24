def mt(num:int):
    for i in range(0,num+1):
        for j in range(0,num+1):
            if i ==0 and j==0:
                print(' ',end='')
            else:
                print(i*j if j>0 and i>0 else j if i<=0 else i,end=' ')
        print('\n')
