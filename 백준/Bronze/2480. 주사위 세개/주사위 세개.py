a,b,c = map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b!=c or a==c!=b or b==c!=a:
    if a==b:
        print(1000+a*100)
    else:
        print(1000+c*100)
else:
    m = max(a,b,c)
    print(m*100)