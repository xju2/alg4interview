# use modulus to get next remove index

def remove_circle(n, m):
    l = range(1, n+1)
    length = len(l)
    cur_index = 0
    while length > 1:
        remove_index = (cur_index + m-1) % length
        l.remove(l[remove_index])
        cur_index = (remove_index + 1) % length
        length = length-1
    return l[0]

if __name__=='__main__':
    print remove_circle(100, 34)
        