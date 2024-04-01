x=input('enter the first string').lower()
y=input('enter the second sring').lower()
k=[x[i] for i in range(0,len(x))]
k.sort() 
l=[y[i] for i in range(0,len(y))]
l.sort()
if (k==l):
    print('TRUE')
else:
    print('FLASE')