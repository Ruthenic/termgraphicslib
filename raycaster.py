from canvas import *
def rayCast(P0,P1,lev):
    length = 0
    ocor = line_coords(P0, P1)
    for i in ocor:
        if not lev[i[1]][i[0]] == "w":
            length+=1
        else:
            break
    return length
def drawLines(lens):
    n=0
    srn = init_default_canvas()
    for i in lens:
        srn = drawline([n,0+int(i/2)],[n,15-int(i/2)],[255,0,0],canvas=srn)
        n+=1
    return srn
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
pc = [px,py]
if dire=='n':
    #ray(s) should be facing north
    lengthnegsix = rayCast(pc, [px-6, 0],lev)
    lengthnegfiv = rayCast(pc, [px-5, 0],lev)
    lengthnegfor = rayCast(pc, [px-4, 0],lev)
    lengthnegthr = rayCast(pc, [px-3, 0],lev)
    lengthnegtwo = rayCast(pc, [px-2, 0],lev)
    lengthnegone = rayCast(pc, [px-1, 0],lev)
    lengthzero = rayCast(pc, [px, 0],lev)
    lengthone = rayCast(pc, [px+1, 0],lev)
    lengthtwo = rayCast(pc, [px+2, 0],lev)
    lengththr = rayCast(pc, [px+3, 0],lev)
    lengthfor = rayCast(pc, [px+4, 0],lev)
    lengthfiv = rayCast(pc, [px+5, 0],lev)
    lengthsix = rayCast(pc, [px+6, 0],lev)
    #print(lengthone,lengthtwo,lengththree)
    for i in lev:
        print(i)
srn = drawLines([lengthnegsix,lengthnegfiv,lengthnegfor,lengthnegthr,lengthnegtwo,lengthnegone,lengthzero,lengthone,lengthtwo,lengththr,lengthfor,lengthfiv,lengthsix])
draw(srn)
