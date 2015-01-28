# three methods to get fibonacci number

# the worst method, iterator from top to bottom
# bad performace when n >= 35
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# nice method, from bottom to top
# bad performace when n >= 500 000
def fibonacci1(n):
    a = 0
    if n == 0:
        return a
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b

# the best method, matrix multiply
# matrix [[1,1],[1,0]] multiply self by N times, the index (1,0) or (0,1) of result is the N fibonacci number
# bad performace when n >= 40 000 000
def fibonacci2(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    if n % 2 == 0:
        return dot(fibonacci2(n/2), fibonacci2(n/2))
    else:
        return dot(dot(fibonacci2((n-1)/2), fibonacci2((n-1)/2)), [[1, 1], [1, 0]])
    
def dot(m1, m2):
    '''
    suppose m1 and m2 are 2*2 matrix, returns m1 * m2
    '''
    m3 = [[0, 0], [0, 0]]
    m3[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
    m3[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
    m3[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
    m3[1][1] = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
    return m3

if __name__=='__main__':
    from time import time
    s = time()
    test1 = 35
    a = fibonacci(test1)
    print 'function fibonacci(%s) costs %0.1f seconds.' % (test1, (time()-s))
    s = time()
    test2 = 100000
    a1 = fibonacci1(test2)
    print 'function fibonacci1(%s) costs %0.1f seconds.' % (test2, (time()-s))
    s = time()
    a2 = fibonacci2(test2)[1][0]
    print 'function fibonacci2(%s) costs %0.1f seconds.' % (test2, (time()-s))