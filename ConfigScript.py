import sys

tags= sys.argv[1]
quickGenesFile= sys.argv[2]

file = open('cellbrowser.conf','r')

lines = file.readlines()

def Find_Word(x):
    for i in lines:
        if x in i:
            return lines.index(i)

Find_Tags="tags ="
Find_Quick="quickGenesFile ="


lines[Find_Word(Find_Tags)]= 'tags =[\"' + tags + '\"]\n'
lines[Find_Word(Find_Quick)]= 'quickGenesFile =\"' + quickGenesFile + '\"\n'

file=open('cellbrowser.conf','w')
file.writelines(lines)
file.close()



