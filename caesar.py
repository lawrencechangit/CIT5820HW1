
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for letter in plaintext:
        ascii=ord(letter)
        if ascii>=97 and ascii<=122:
            letter=ascii-96
            letter_afterkey=(letter+key)%26
            if letter_afterkey!=0:
                newascii=letter_afterkey+96
            else:
                newascii=122
        elif ascii>=65 and ascii<=90:
            letter=ascii-64
            letter_afterkey=(letter+key)%26
            if letter_afterkey!=0:
                newascii=letter_afterkey+64
            else:
                newascii=90
        new_letter=chr(newascii)
        ciphertext=ciphertext+new_letter
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    for letter in ciphertext:
        ascii=ord(letter)
        if ascii>=97 and ascii<=122:
            letter=ascii-96
            letter_beforekey=(letter-key)%26
            if letter_beforekey!=0:
                plainascii=letter_beforekey+96
            else:
                plainascii=122
        elif ascii>=65 and ascii<=90:
            letter=ascii-64
            letter_beforekey=(letter-key)%26
            if letter_beforekey!=0:
                plainascii=letter_beforekey+64
            else:
                plainascii=90   
        plain_letter=chr(plainascii)
        plaintext=plaintext+plain_letter
    return plaintext
