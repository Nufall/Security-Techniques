import random


def GCD(x, y):
    if (y == 0):
        return x
    else:
        return GCD(y, x % y)


def invMod(e, eular):
    for i in range(eular):
        if (e * i) % eular == 1:
            return i
    return None


def keygen():
    ct = 0
    for i in range(100, 200):
        z = random.randrange(100, 200)
        for x in range(2, z):
            if (z % x == 0):
                break
        else:
            if (ct == 1 and z != p):
                # print(z)
                q = z
                break
            if (ct == 0):
                # print(z)
                p = z
                ct += 1
    n = p * q
    eular = (p - 1) * (q - 1)
    e = random.randrange(1, eular)

    while (e < eular):
        if (GCD(e, eular) != 1):
            e = e + 1
        else:
            break
    d = invMod(e, eular)
    return n, e, d


def cipherRSA(msg, n, e):
    C = [(ord(M) ** e) % n for M in msg]
    return C


def decipherRSA(cipher, n, d):
    M = [chr((C ** d) % n) for C in cipher]
    return ''.join(M)


# n, e, d = keygen()
# cipher = cipherRSA("hello", n, e)
# print('cipher',cipher)
# deciphered = decipherRSA(cipher, n, d)
# print(deciphered)


