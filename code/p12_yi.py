# use reduce to get sum of a sequence
n = 100
print reduce(lambda x, y: x+y, range(n+1), 0)
