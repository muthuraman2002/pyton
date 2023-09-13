string=input().split()
arr=[]
for i in string:
    arr.append(i[::-1])
for i in arr:
    print(i,end=" ")