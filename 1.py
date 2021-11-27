a=dict() #мат
b=dict() #физ
c=dict() #инф
k1=0
k2=0
k3=0
_s=input()
while _s!='':
    s = _s.split()
    a[s[0]+s[1]]=int(s[2])
    k1+=1
    _s=input()

_s=input()
while _s!='':
    s = _s.split()
    b[s[0]+s[1]]=int(s[2])
    k2+=1
    _s=input()

_s=input()
while _s!='':
    s = _s.split()
    c[s[0]+s[1]]=int(s[2])
    k3+=1
    _s=input()
k=k1+k2+k3
print(k)









