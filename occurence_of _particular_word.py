a=input('enter string:')
l=a.split()
d={}
for i in l:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)
