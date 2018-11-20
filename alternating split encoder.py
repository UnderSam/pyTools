def encrypt(text, n):
    if text is None:
        return None
    if len(text) == 0 or n <=0 :
        return text

    for __ in range(n):
        text = text[1::2]+text[0::2]
    return text

def decrypt(encrypted_text, n):
    if encrypted_text is None:
        return None
    if len(encrypted_text) == 0 or n <=0 :
        return encrypted_text

    new = ""
    mid = len(encrypted_text)//2
    for __ in range(n):
        temp = ""
        for i in range(mid):
            temp += encrypted_text[mid:][i]+encrypted_text[:mid][i]
        encrypted_text = temp
        new = temp
    return new
