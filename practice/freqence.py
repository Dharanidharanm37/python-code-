a=153
temp=a
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==a:
    print("armstrong")
else:
    print("not armstrong")

