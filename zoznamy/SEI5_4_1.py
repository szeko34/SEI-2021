# Tu napíšte svoj kód :-)
#úvod do práce so súborom, otvorenie súboru a hľadanie zoznamu najdlhších riadkov
subor=open("vstup.txt","r")

"""
x=subor.read()
x=subor.read(5)
x=subor.readline()"""
x=subor.readlines()

d=0
di=[]

for i in range(len(x)):
    if len(x[i])>d:
        d=len(x[i])
        di=[i]
    elif len(x[i])==d:
        di.append(i)
    print(di)


print(d-1,di)




subor.close()
