mark=list(map(int,input().split(',')))
arr=[]
for i in mark:
    if i>=35:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)