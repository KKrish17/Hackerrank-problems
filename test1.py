i=int(input())
n=int(input())
a=[]
temp=0
for k in range(int(len(str(i))/3)):
    a.append(str(i)[temp:temp+n])
    temp=temp+n
x=0
for k in range(len(a)):
    if x<a[k].count('1'):
        x=a[k].count('1')
print(x)
