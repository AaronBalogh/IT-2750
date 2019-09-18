mylist = ['The quick brown fox jumps over the lazy dog']
newList = []
for mylist in mylist:
    newList.append(mylist.lower())
print(newList)
def getMostFrequent(mylist):
    dict = {}
    for n in mylist:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(getMostFrequent(mylist))

def uniqueLetters(mylist):
    x = []
    for a in mylist:
        if a not in x:
            x.append(a)
    return x
print(uniqueLetters(mylist))
