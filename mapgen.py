from sys import argv
blankmap = ''
for i in range(1,int(argv[1])):
    blankmap+='w'
blankmap+='w\n'
for i in range(1, int(argv[2])-2):
    blankmap+='w'
    for i in range(1,int(argv[1])-1):
        blankmap+='.'
    blankmap+='w\n'
for i in range(1,int(argv[1])):
    blankmap+='w'
blankmap+='w'
print(blankmap)
