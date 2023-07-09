sample={}
students={"arthi":89,"muthu":76,"bharathi":99,"ram":89,"ganesh":23}
for key,value in students.items():
    #print(key,value)
    if value>30:
        sample[key]=value
print(sample)
