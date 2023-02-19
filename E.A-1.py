########## Problem-1
a=0
b=1
for i in range(10):
 print(a, end=',')
 c=a+b
 a=b
 b=c

########## Problem-2
revers=[]
x=input('enter word')
for i in range(len(x)-1,-1,-1):
    print(i)
    list(x)
    revers.append(x[i])
revers="".join(revers)
print(revers)

########## Problem-3
s=input('enter the series').split(',')
x=0
y=0
for i in s:
    if int(i)%2==0:
     x+=1
    else:
        y+=1
print(x,'even nos are there')
print(y,'odd nos are there')