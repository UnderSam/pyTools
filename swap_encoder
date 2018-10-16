def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]
def encode_Long_name(strs):
    val = ""
    for j in strs:
        if(j.encode("unicode-escape").decode("utf-8")==j):
            val = val+str(hex(ord(j))).replace("0x","")+"00"   #ord->char to ascii
        else:
            m_d = j.encode("unicode-escape").decode("utf-8")
            #print(m_d)
            m_d = m_d.replace("\\u","")
            crypt = right(m_d,2)+left(m_d,2)
            val = val + crypt
        #print(crypt)
    return val.upper()
def Decoder(Ecd_name):
    cells = []
    cl = ""
    for idx,ci in enumerate(Ecd_name):
        cl = cl + ci
        #print(cl)
        if (idx+1)%4 ==0:
            cells.append(right(cl,2)+left(cl,2))
            cl=""
    name = ""
    for i in cells:
        name+=chr(int("0x"+i,0))
    print(name)
