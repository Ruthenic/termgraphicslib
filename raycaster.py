from canvas import *
lev=[]
with open('map.txt') as f:
    for line in f:
        tmp=[]
        for letter in line:
            if letter != '\n':
                tmp.append(letter)
        lev.append(tmp)
ly=len(lev)-1
lx=len(lev[0])-1
py = 0
for i in lev:
    try:
        px = i.index('p')
        break
    except:
        pass
    py+=1
dire='n'
rayx,rayy=px,py
if dire=='n':
    #ray(s) should be facing north
    lengthone = 0
    lengthtwo = 0
    lengththree = 0
    lengthfour = 0
    lengthfive = 0
    lengthsix = 0
    lengthseven = 0
    lengtheight = 0
    lengthnine = 0
    while lev[rayy][rayx-7] != 'w':
        lengthone+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx-6] != 'w':
        lengthtwo+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx-5] != 'w':
        lengththree+=1
        rayy-=1
    while lev[rayy][rayx-4] != 'w':
        lengthfour+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx-3] != 'w':
        lengthfive+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx-2] != 'w':
        lengthsix+=1
        rayy-=1
    while lev[rayy][rayx-1] != 'w':
        lengthseven+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx] != 'w':
        lengtheight+=1
        rayy-=1
    rayy=py
    while lev[rayy][rayx+1] != 'w':
        lengthnine+=1
        rayy-=1
    print(lengthone,lengthtwo,lengththree)
    for i in lev:
        print(i)
srn = drawline([0,0+int(lengthone/2)],[0,15-int(lengthone/2)],[255,0,0])
srn = drawline([1,0+int(lengthtwo/2)],[1,15-int(lengthtwo/2)],[255,0,0],canvas=srn)
srn = drawline([2,0+int(lengththree/2)],[2,15-int(lengththree/2)],[255,0,0],canvas=srn)
srn = drawline([3,0+int(lengthfour/2)],[3,15-int(lengthfour/2)],[255,0,0],canvas=srn)
srn = drawline([4,0+int(lengthfive/2)],[4,15-int(lengthfive/2)],[255,0,0],canvas=srn)
srn = drawline([5,0+int(lengthsix/2)],[5,15-int(lengthsix/2)],[255,0,0],canvas=srn)
srn = drawline([6,0+int(lengthseven/2)],[6,15-int(lengthseven/2)],[255,0,0],canvas=srn)
srn = drawline([7,0+int(lengtheight/2)],[7,15-int(lengtheight/2)],[255,0,0],canvas=srn)
srn = drawline([8,0+int(lengthnine/2)],[8,15-int(lengthnine/2)],[255,0,0],canvas=srn)
draw(srn)
