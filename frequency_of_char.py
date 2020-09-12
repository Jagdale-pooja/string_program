a=input('enter string:')
char=0
d={}
for line in a:
    if line not in d.keys():
        d[line]=0
    d[line]=d[line]+1
    wordlist=line.split()
    char+=sum(len(word)for word in wordlist)
print(d)
