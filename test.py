test=["string = fun", "Sometimes we don't find things", "Why string="]

def Find_Word(x):
    for i in test:
        if x in i:
            return test.index(i)

Find="string="

print(Find_Word(Find))
