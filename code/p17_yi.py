# use a list to store unique character, at last get the first element as first unique character
def first_unique(s):
    duplicated_list = []
    unique_list = []
    for c in s:
        if duplicated_list.count(c):
            continue
        if unique_list.count(c):
            unique_list.remove(c)
            duplicated_list.append(c)
        else:
            unique_list.append(c)
    if unique_list:
        return unique_list[0]

if __name__=='__main__':
    s = 'hello world. i am yichuanzhou. nice to meet you.'
    fu = first_unique(s)
    if fu:
        print 'The first unique character in string\n%s\n is %s' % (s, fu)
    else:
        print 'There is no unique character in string \n%s' % s