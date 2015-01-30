# (a1+an)*n/2=x
# (a1+a1+n-1)*n/2=x
# n^2+(2a1-1)n-2x=0
# n=(1-2a1+sqrt((2a1-1)^2+8x))/2
import math
def find_seq(n):
    a0 = 0
    if n % 2 == 0:
        a0 = n/2
    else:
        a0 = (n+1)/2
    
    seq = []
    for i in range(1,a0):
        delta = (2*i-1)**2+8*n
        if delta != math.ceil(math.sqrt(delta))**2:
            continue
        seq_len = int((1-2*i+math.sqrt(delta))*1.0/2)
        seq.append(range(i, i+seq_len))
    return seq

if __name__=='__main__':
    import sys
    n = 15
    if len(sys.argv) > 1 and sys.argv[1]:
        n = int(sys.argv[1])
    seq = find_seq(n)
    for l in seq:
        print l
