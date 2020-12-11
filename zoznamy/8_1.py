# Tu napíšte svoj kód :-)
subor = open("mensi.txt","r")

riadky = subor.readlines()
print(riadky)

for i in range(len(riadky)):
    #print(repr(riadok), end = " ")
    if riadky[i].count("1") % 2 == 0:
        print ("parny ",riadky[i].count("1"))
    else:
        print (i,"neparny ",riadky[i].count("1"))

for i in range(len(riadky[0])):
    print(i, end = " ")
    pocet = 0
    for riadok in riadky:
        pocet += int(riadok[i])
    print(pocet)

subor.close()

