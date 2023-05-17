def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key={i:0 for i in range(len(keyword))}
    for i in range(len(keyword)):
        if keyword[i] in en_abc:
            key[i] = en_abc.find(keyword[i])
        elif keyword[i] in en_ABC:
            key[i] = en_ABC.find(keyword[i])
        elif keyword[i] in rus_abc:
            key[i] = rus_abc.find(keyword[i])
        elif keyword[i] in rus_ABC:
            key[i] = rus_ABC.find(keyword[i])
    ans = ''
    a = [key[i % len(keyword)] for i in range(len(plaintext))]
    for i in range(len(plaintext)):
        if plaintext[i] in en_abc:
            sdvig = (a[i] + en_abc.find(plaintext[i])) % 26
            ans += en_abc[sdvig % 26]
        elif plaintext[i] in en_ABC:
            sdvig = (a[i] + en_ABC.find(plaintext[i])) % 26
            ans += en_ABC[sdvig % 26]
        elif plaintext[i] in rus_abc:
            sdvig = (a[i] + rus_abc.find(plaintext[i])) % 33
            ans += rus_abc[sdvig % 33]
        elif plaintext[i] in rus_ABC:
            sdvig = (a[i] + rus_ABC.find(plaintext[i])) % 33
            ans += rus_ABC[sdvig % 33]
        elif plaintext[i]==' ':
            ans += ' '
    return ans

def decrypt_vigenere( ciphertex:str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = {i: 0 for i in range(len(keyword))}
    for i in range(len(keyword)):
        if keyword[i] in en_abc:
            key[i] = en_abc.find(keyword[i])
        elif keyword[i] in en_ABC:
            key[i] = en_ABC.find(keyword[i])
        elif keyword[i] in rus_abc:
            key[i] = rus_abc.find(keyword[i])
        elif keyword[i] in rus_ABC:
            key[i] = rus_ABC.find(keyword[i])
    ans = ''
    a = [key[i % len(keyword)] for i in range(len(ciphertex))]
    for i in range(len(ciphertex)):
        if ciphertex[i] in en_abc:
            sdvig = (en_abc.find(ciphertex[i])-a[i]) % 26
            ans += en_abc[sdvig % 26]
        elif ciphertex[i] in en_ABC:
            sdvig = (en_ABC.find(ciphertex[i])-a[i]) % 26
            ans += en_ABC[sdvig % 26]
        elif ciphertex[i] in rus_abc:
            sdvig = (rus_abc.find(ciphertex[i])-a[i]) % 33
            ans += rus_abc[sdvig % 33]
        elif ciphertex[i] in rus_ABC:
            sdvig = (rus_ABC.find(ciphertex[i])-a[i]) % 33
            ans += rus_ABC[sdvig % 33]
        elif ciphertex[i] == ' ':
            ans += ' '
    return ans
