# init a low index to 0 and a high index to the length-1
# if the sum of two values of two indexs bigger than target, decrease the high index
# if the sum of two values of two indexs smaller than target, increase the low index
# util the sum of two values of two indexs equals target
def find_number(l, n):
    c = len(l)
    si = 0
    ei = c-1
    
    flag = False
    while True:
        if l[si]+l[ei] > n and ei > 0:
            ei = ei - 1
        elif l[si]+l[ei] < n and si < c:
            si = si + 1
        elif l[si]+l[ei] == n:
            flag = True
            break
        else:
            break
    if flag:
        return (si, ei, l[si], l[ei], n)

if __name__=='__main__':
    tp = find_number([1,3,5,7,9,12,14,18,23,34,45,56,67,78,89,90,100,101,120,130], 115)
    if tp:
        print 'n=l[%s]+l[%s]=%s+%s=%s' % tp
    else:
        print 'fail to find the match number'