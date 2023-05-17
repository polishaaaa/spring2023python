import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ans=''
    en_abc='abcdefghijklmnopqrstuvwxyz'
    en_ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a = {en_abc[i]:en_abc[(i+shift)%len(en_abc)] for i in range(len(en_abc))}
    b = {en_ABC[i]:en_ABC[(i+shift)%len(en_ABC)] for i in range(len(en_ABC))}
    a1 = {rus_abc[i]: rus_abc[(i + shift) % len(rus_abc)] for i in range(len(rus_abc))}
    b1 = {rus_ABC[i]: rus_ABC[(i + shift) % len(rus_ABC)] for i in range(len(rus_ABC))}
    for s in plaintext:
        if s in en_abc:
            ans+=a[s]
        elif s in en_ABC:
            ans+=b[s]
        elif s in rus_abc:
            ans+=a1[s]
        elif s in rus_ABC:
            ans+=b1[s]
        else:
            ans+=s
    return (ans)



def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    ans = ''
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a = {en_abc[i]: en_abc[(i - shift) % len(en_abc)] for i in range(len(en_abc))}
    b = {en_ABC[i]: en_ABC[(i - shift) % len(en_ABC)] for i in range(len(en_ABC))}
    a1 = {rus_abc[i]: rus_abc[(i - shift) % len(rus_abc)] for i in range(len(rus_abc))}
    b1 = {rus_ABC[i]: rus_ABC[(i - shift) % len(rus_ABC)] for i in range(len(rus_ABC))}
    for s in ciphertext:
        if s in en_abc:
            ans += a[s]
        elif s in en_ABC:
            ans += b[s]
        elif s in rus_abc:
            ans += a1[s]
        elif s in rus_ABC:
            ans += b1[s]
        else:
            ans += s
    return (ans)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
