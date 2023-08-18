def uni(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x
l=[1,2,3,4,5,6,7]
print(uni(l))
