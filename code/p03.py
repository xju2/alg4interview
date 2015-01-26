#!/usr/bin/env python
#Maximum contiguous subseqence sum algorithm

#devide-and-conquer
def max_sub_sum1(array):
    return max_sum_dac(array, 0, len(array) -1)
#real implementation
def max_sum_dac(array, left, right):
    #base case
    if left == right :
        if array[ left ] > 0:
            return array[ left ]
        else:
            return 0
    
    center = ( left + right ) / 2
    maxLeftSum = max_sum_dac(array, left, center)
    maxRightSum = max_sum_dac(array, center+1, right)
    #obtain the border sum
    maxAcrossBorderSum = 0
    acrossBorderSum = 0
    for i in range(left,right+1):
        acrossBorderSum = acrossBorderSum + array[i]
        if acrossBorderSum < 0:
            acrossBorderSum = 0
        if acrossBorderSum > maxAcrossBorderSum:
            maxAcrossBorderSum = acrossBorderSum 

    return max(maxLeftSum, maxRightSum, maxAcrossBorderSum)

def max_sub_sum2(array):
    theSum = 0
    theMaxSum = 0
    for a in array:
        theSum = theSum + a
        if theSum < 0:
            theSum = 0
        if theSum > theMaxSum:
            theMaxSum = theSum

    return theMaxSum

a=[-2, 11, -4, 13, -5, -2]
print max_sub_sum1(a)
print max_sub_sum2(a)
