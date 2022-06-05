count=0
def flipfront(arr,n):
    revers=arr[0:n]
    revers.reverse()
    revers+=arr[n:]
    global count
    count+=1
    return revers

def pancake_sort(arr):
    copy=arr
    true=arr
    true.sort()
    for x in range(len(copy)):
        big=copy[:len(copy)-x]
        big.sort()
        big=big[-1]
        inx=copy.index(big)+1
        #print(big,inx,len(copy)-x)
        if inx==1:
            copy=flipfront(copy,len(copy)-x)
        else:
            copy=flipfront(copy,inx)
            copy=flipfront(copy,len(copy)-x)

        if copy==true:
            break
        
        #print(copy)
    #print(copy)

f = open("gistfile1.txt", "r")
for x in f.read().split():
    temp=[]
    for y in x:
        temp.append(int(y))
    pancake_sort(temp)
print('Times Flipfronted: '+str(count))

#flipfront([0, 1, 2, 3, 4], 2)
#flipfront([0, 1, 2, 3, 4], 3)
#flipfront([0, 1, 2, 3, 4], 5)
#flipfront([1, 2, 2, 2], 3)


