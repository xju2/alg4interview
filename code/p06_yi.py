# get a list of number that the count of every number equals the value of every number index in the list
def get_count(l):
    '''
    get the count of each number into a dict
    '''
    d = {}
    for i in l:
        if d.get(i):
            d[i] = d.get(i) + 1
        else:
            d[i] = 1
    return d

def change(l):
    '''
    change value of list with the count of index in list in time
    '''
    i = 0
    while i < len(l):
        d = get_count(l)
        if d.get(i):
            l[i] = d.get(i)
        else:
            l[i] = 0
        i = i+1

def travel(l, debug=False):
    '''
    change the list util the list cannot be changed
    '''
    while True:
        if debug:
            print l
        c = l[:]
        change(l)
        if c == l:
            break

if __name__=='__main__':
    a = []
    import random
    for i in range(10):
        a.append(random.randint(0,9))
    travel(a, True)

