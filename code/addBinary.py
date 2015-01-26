#!/usr/bin/env python
#add two string binary, print out the binary as a string
def addBinary(a, b):#dumm implement
    result = ""
    lbit = a
    sbit = b
    if len(b) > len(a):
        lbit = b
        sbit = a
    sum = '0'
    carry = False
    for i in range(len(sbit)):
        id_s = len(sbit) - 1 - i
        id_l = len(lbit) - 1 - i
        sum = add_bit_ca(lbit[id_l],sbit[id_s],carry)
        try:    
            if len(sum) > 1:
                result = sum[1]+result
                carry = True
            else:
                result = sum[0]+result
                carry = False
        except:
            print "input isn't binary number!"
            return ""
    
    id_l = len(lbit) - 1 - len(sbit)
    while len(sum) > 1:
        if id_l > -1:
            sum = add_bit(lbit[id_l],'1')
            result = sum[1] +result
            id_l = id_l - 1
        else: 
            result = '1'+result
            break
    while id_l > -1:
        result = lbit[id_l]+result
        id_l = id_l - 1

    return result
    
def add_bit(b1, b2):
    if b1 == '0': return b2
    elif b2 == '0': return b1
    elif b1 == '1' and b2 == '1':
        return '10'
    else:
        return None

def add_bit_ca(b1,b2,carry):
    if carry:
        tmp = add_bit(b1,b2)
        if len(tmp) > 1:
            return '11'
        else:
            return add_bit(tmp[0],'1')
    else:
        return add_bit(b1,b2)

#bit better implement
def add_binary(a, b):
    result = ""
    lbit = a
    sbit = b
    if len(b) > len(a):
        lbit = b
        sbit = a
    lls = []
    sls = []
    for i in lbit:
        lls.append(i)
    for i in sbit:
        sls.append(i)
    carry = False
    while len(sls) > 0:
        m_sum = add_bit_ca(lls.pop(),sls.pop(),carry)
        try:
            if len(m_sum) > 1:
                carry = True
                result = m_sum[1]+result
            else:
                carry = False
                result = m_sum[0]+result
        except:
            print "input isn't binary number"
            return ""
    
    while len(m_sum) > 1:
        if len(lls) > 0:
            m_sum = add_bit(lls.pop(),'1')
            result = m_sum[1]+result
        else:
            result = '1' + result
            break
    while len(lls) > 0:
        result = lls.pop() + result
    return result

if __name__ == '__main__':
    a_str = "01111"
    b_str = "10011"
    print a_str,b_str
    print addBinary(a_str, b_str)
    print add_binary(a_str, b_str)
