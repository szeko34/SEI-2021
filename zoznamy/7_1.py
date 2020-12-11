# Tu napíšte svoj kód :-)
import tkinter,random

sirka=400
vyska=40
n=10
rozmer=sirka/n

plocha=tkinter.Canvas(width=sirka,height=vyska)
plocha.pack()

"""
zoznam = [0,2,1,0,0,0,0,1,1,2] #_XO____OOX
zoznam = [0,"x","o",0,0,0,0,"o","o","x"] #_XO____OOX
zoznam = ["","x","o","","","","","o","o","x"] #_XO____OOX
"""

zoznam = [0,0,0,0,0,0,0,0,0,0]
zozna = [0]*10
zozn = []
for i in range(10):
    zozn.append(0)

print(zozna)

def mriezka(a,b):
    for i in range(a-1):
        plocha.create_line((i+1)*sirka/a,0,(i+1)*sirka/a,vyska)
    for i in range(b-1):
        plocha.create_line(0,(i+1)*vyska/b,sirka,(i+1)*vyska/b)


def krizik(a,b):
    print("x",rozmer,a,b)

    plocha.create_line(a*rozmer,b*rozmer,(a+1)*rozmer,(b+1)*rozmer)
    plocha.create_line((a+1)*rozmer,b*rozmer,a*rozmer,(b+1)*rozmer)

def kruzok(a,b):
    print("o",rozmer,a,b)
    plocha.create_oval(a*rozmer,b*rozmer,(a+1)*rozmer,(b+1)*rozmer)

def Lklik(event):
    stlpec=int(event.x//rozmer)
    if zozna[stlpec]==0:
        krizik(stlpec,event.y//(vyska))
        zozna[stlpec]=2
        print(zozna)

def Pklik(event):
    stlpec=int(event.x//rozmer)
    if zozna[stlpec]==0:
        kruzok(stlpec,event.y//(vyska))
        zozna[stlpec]=1
        print(zozna)

mriezka(n,1)
plocha.bind("<Button-1>",Lklik)
plocha.bind("<Button-3>",Pklik)

