s1 = "hello&everyone&welcome&toTkR"
c=0
for ch in s1:
    if ch=='&':
        c+=1
    else:
        pass
print(c)

s1 = "hello&everyone"
s2=s1.replace("&"," ")
print(s2)   