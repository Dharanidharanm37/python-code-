a="hello"
fre={}
for char in a:
    if char in fre:
        fre[char] +=1
    else:
        fre[char]=1
print(fre)
