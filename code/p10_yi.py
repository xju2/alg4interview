# reverse sentence on word
def reverse_by(s, delimeter):
    s_list = s.split(delimeter)
    s_list.reverse()
    return delimeter.join(s_list)

if __name__=='__main__':
    s = 'Hi, i am a student.'
    print reverse_by(s, ' ')