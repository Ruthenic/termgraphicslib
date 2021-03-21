from termgraphicslib.canvas import *
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
        srn = drawline([n,0+int(i/2)],[n,15-int(i/2)],[255-int(i*10),0,0],canvas=srn)
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
while True:
    pc = [px,py]
    if dire=='n':
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
        print(dire)
    if dire=='s':
        lengthnegsix = rayCast(pc, [px-6, len(lev)-1],lev)
        lengthnegfiv = rayCast(pc, [px-5, len(lev)-1],lev)
        lengthnegfor = rayCast(pc, [px-4, len(lev)-1],lev)
        lengthnegthr = rayCast(pc, [px-3, len(lev)-1],lev)
        lengthnegtwo = rayCast(pc, [px-2, len(lev)-1],lev)
        lengthnegone = rayCast(pc, [px-1, len(lev)-1],lev)
        lengthzero = rayCast(pc, [px, len(lev)-1],lev)
        lengthone = rayCast(pc, [px+1, len(lev)-1],lev)
        lengthtwo = rayCast(pc, [px+2, len(lev)-1],lev)
        lengththr = rayCast(pc, [px+3, len(lev)-1],lev)
        lengthfor = rayCast(pc, [px+4, len(lev)-1],lev)
        lengthfiv = rayCast(pc, [px+5, len(lev)-1],lev)
        lengthsix = rayCast(pc, [px+6, len(lev)-1],lev)
        #print(lengthone,lengthtwo,lengththree)
        for i in lev:
            print(i)
        print(dire)
    if dire=='w':
        lengthnegsix = rayCast(pc, [0, py-6],lev)
        lengthnegfiv = rayCast(pc, [0, py-5],lev)
        lengthnegfor = rayCast(pc, [0, py-4],lev)
        lengthnegthr = rayCast(pc, [0, py-3],lev)
        lengthnegtwo = rayCast(pc, [0, py-2],lev)
        lengthnegone = rayCast(pc, [0, py-1],lev)
        lengthzero = rayCast(pc, [0, py],lev)
        lengthone = rayCast(pc, [0, py+1],lev)
        lengthtwo = rayCast(pc, [0, py+2],lev)
        lengththr = rayCast(pc, [0, py+3],lev)
        lengthfor = rayCast(pc, [0, py+4],lev)
        lengthfiv = rayCast(pc, [0, py+5],lev)
        lengthsix = rayCast(pc, [0, py+6],lev)
        #print(lengthone,lengthtwo,lengththree)
        for i in lev:
            print(i)
        print(dire)
    if dire=='e':
        #probably not the best of ideas to draw all length values from the first row but /shrug
        lengthnegsix = rayCast(pc, [len(lev[0])-1, py-6],lev)
        lengthnegfiv = rayCast(pc, [len(lev[0])-1, py-5],lev)
        lengthnegfor = rayCast(pc, [len(lev[0])-1, py-4],lev)
        lengthnegthr = rayCast(pc, [len(lev[0])-1, py-3],lev)
        lengthnegtwo = rayCast(pc, [len(lev[0])-1, py-2],lev)
        lengthnegone = rayCast(pc, [len(lev[0])-1, py-1],lev)
        lengthzero = rayCast(pc, [len(lev[0])-1, py],lev)
        lengthone = rayCast(pc, [len(lev[0])-1, py+1],lev)
        lengthtwo = rayCast(pc, [len(lev[0])-1, py+2],lev)
        lengththr = rayCast(pc, [len(lev[0])-1, py+3],lev)
        lengthfor = rayCast(pc, [len(lev[0])-1, py+4],lev)
        lengthfiv = rayCast(pc, [len(lev[0])-1, py+5],lev)
        lengthsix = rayCast(pc, [len(lev[0])-1, py+6],lev)
        #print(lengthone,lengthtwo,lengththree)
        for i in lev:
            print(i)
        print(dire)
    srn = drawLines([lengthnegsix,lengthnegfiv,lengthnegfor,lengthnegthr,lengthnegtwo,lengthnegone,lengthzero,lengthone,lengthtwo,lengththr,lengthfor,lengthfiv,lengthsix])
    draw(srn)
    movdir = input('Direction? ')
    if movdir.lower() == 'up':
        if dire=='n':
            py-=1
        if dire=='w':
            px-=1
        if dire=='s':
            py+=1
        if dire=='e':
            px+=1
        if lev[py][px] == 'w':
            print("Cannot move here!")
            if dire=='n':
                py+=1
            if dire=='w':
                px+=1
            if dire=='s':
                py-=1
            if dire=='e':
                px-=1
        elif lev[py][px] == 'x':
            print("You found the end!")
            exit()
        else:
            if dire=='n':
                temp=py+1
                lev[temp][px] = '.'
            if dire=='w':
                temp=px+1
                lev[py][temp] = '.'
            if dire=='s':
                temp=py-1
                lev[temp][px] = '.'
            if dire=='e':
                temp=px-1
                lev[py][temp] = '.'
            lev[py][px] = 'p'
    '''if movdir.lower() == 'back':
        if dire=='n':
            py+=1
        if lev[py][px] == 'w':
            print("Cannot move here!")
            py-=1
        else:
            lev[py][px] = 'p'
            lev[pc[1]][px] = '.'''
    if movdir.lower() == 'tl':
        if dire=='n':
            dire='w'
        elif dire=='w':
            dire='s'
        elif dire=='s':
            dire='e'
        elif dire=='e':
            dire='n'
    if movdir.lower() == 'tr':
        if dire=='n':
            dire='e'
        elif dire=='w':
            dire='n'
        elif dire=='s':
            dire='w'
        elif dire=='e':
            dire='s'
