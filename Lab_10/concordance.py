import string



def concordance(g):
    """
    Outputs things like a concordance. It outputs words and the number of the lines
    they appear in. The outputed words are in alphabetical order.
    If you've come here to debug, just rewrite it.
    >>> concordance('two_cities.txt')
    best : [1, 2]
    it : [1, 2]
    of : [1, 2]
    the : [1, 2]
    times : [1, 2]
    was : [1, 2]
    worst : [2]
    """
    c = open(g, "r")

    thing = {}
    a = 0
    for d in c:
        a = a + 1
        e = d.split()
        b = set()
        for f in e:
            f = f.strip(string.punctuation).lower()
            if f != '':
                b.add(f)
        e = list(b)
        print (e)
        for f in e:
            try:
                thing[f] = thing[f] + str(a) + ', '
            except(KeyError):
                thing[f] = str(a) + ', '
    a = list(thing.keys())
    a.sort()
    i =[]
    for h in a:
        i = i + [(h + " : [" + thing[h][:-2] + "]")]
    return i



dct = concordance(input())
for line in dct:
    print(line)
