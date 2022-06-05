def nonogramrow(a):
    data=[]
    try:
        if a[0]==1:
            data.append(1)
    except:
        data=[]
        
    for inx in range(len(a)-1):
        if a[inx]==0 and a[inx+1]==1:
            data.append(1)
        if a[inx]==1 and a[inx+1]==1:
            data[len(data)-1]+=1
    print(data)


nonogramrow([])
nonogramrow([0,0,0,0,0])
nonogramrow([1,1,1,1,1])
nonogramrow([0,1,1,1,1,1,0,1,1,1,1])
nonogramrow([1,1,0,1,0,0,1,1,1,0,0])
nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1])
nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
