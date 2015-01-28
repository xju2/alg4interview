# use reduce to get sum of a sequence
def get_sum(n):
    return reduce(lambda x, y: x+y, range(n+1), 0)
    
if __name__=='__main__':
    n = 100
    print get_sum(n)
