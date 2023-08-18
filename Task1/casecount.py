st="my name is akhil"
low=0
upper=0

for i in st:
    if i.islower:
        low+=1
    elif i.isupper:
         upper+=1
    else:
        pass
print("capital count",upper)
print("lower count:",low)
