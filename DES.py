import math
import re

def toBinary(a):
    binary = ""
    binary = ''.join(format(i, '08b') for i in bytearray(a, encoding='utf-8'))
    binary = binary.zfill(64)
    return binary


def binary_to_string(binary_string):
    string = ''
    for i in range(0, len(binary_string), 8):
        binary_value = binary_string[i:i + 8]
        decimal = int(binary_value, 2)  # Convert binary to decimal
        character = chr(decimal)  # Convert decimal to character
        string += character
    return string


def shift(halfkey, val):
    shifted = ""
    if val == 1:
        for i in range(1, 28):
            shifted += halfkey[i]
        shifted += halfkey[0]
        return shifted
    elif val == 2:
        for i in range(0, 2):
            for j in range(1, 28):
                shifted += halfkey[j]
            shifted += halfkey[0]
            halfkey = shifted
            shifted = ""
        return halfkey
    return shifted


def xoring(x, y):
    result = ""
    for i in range(0, len(y)):
        if x[i] == y[i]:
            result += "0"
        else:
            result += "1"
    return result


def bintodec(a):
    dec = int(a, 2)
    return dec


def dectobin(a):
    a = bin(a)[2:].zfill(4)
    return a


def keygeneration(key):
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]
    # key=y
    perm_key = ""
    rounds = []

    for i in range(0, 56):
        perm_key += key[pc1[i] - 1]
    # print(perm_key)
    halfleft = perm_key[0:28]
    # print(halfleft)
    halfright = perm_key[28:56]
    # print(halfright)

    for i in range(0, 16):
        fullkey = ""
        if i == 0 or i == 1 or i == 8 or i == 15:
            halfleft = shift(halfleft, 1)
            halfright = shift(halfright, 1)
        else:
            halfleft = shift(halfleft, 2)
            halfright = shift(halfright, 2)
        full_key = halfleft + halfright
        # print(full_key)
        round = ""
        for j in range(0, 48):
            round += full_key[pc2[j] - 1]
        # print(round)
        rounds.append(round)
        # print(rounds[i])
    # print(full_key)
    return rounds


def des(key, text):
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    ep = [32, 1, 2, 3, 4, 5, 4, 5,
          6, 7, 8, 9, 8, 9, 10, 11,
          12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21,
          22, 23, 24, 25, 24, 25, 26, 27,
          28, 29, 28, 29, 30, 31, 32, 1]
    pt = [16, 7, 20, 21, 29, 12, 28, 17,
          1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9,
          19, 13, 30, 6, 22, 11, 4, 25]
    ivp = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
    sb = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]
    # print(sb[1])
    p = ""
    for i in range(0, 64):
        p += text[ip[i] - 1]

    halfleft = p[0:32]
    # print(halfleft)
    halfright = p[32:64]
    # print(halfright)
    for i in range(0, 16):
        right = ""
        xr = ""
        ct = 0
        for j in range(0, 48):
            right += halfright[ep[j] - 1]
            # ct=ct+1
        # print(right)
        # print(ct)
        xr = xoring(key[i], right)
        res = ""
        row = ""
        cl = ""
        # print(len(xr))
        f = 0
        for j in range(0, 8):
            # print(f)
            row += xr[f]
            row += xr[f + 5]
            # row+=xr[15]
            # print(row)
            cl += xr[f + 1] + xr[f + 2] + xr[f + 3] + xr[f + 4]
            # print(cl)
            col = bintodec(cl)
            rw = bintodec(row)
            val = sb[j][rw][col]
            # print(val)
            res += dectobin(val)
            f = f + 6
            row = ""
            cl = ""
            # not done yet
        p2 = ""

        # print(res)
        # print(len(res))
        for j in range(0, 32):
            p2 += res[pt[j] - 1]
        last = xoring(p2, halfleft)
        # print(last)
        halfleft = last
        if i < 15:
            t = halfright
            halfright = halfleft
            halfleft = t
        # f=halfleft+halfright
        # print(f)
    full = halfleft + halfright
    cipher = ""
    for i in range(0, 64):
        cipher += full[ivp[i] - 1]
    return cipher


def ddes(key, text):
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    ep = [32, 1, 2, 3, 4, 5, 4, 5,
          6, 7, 8, 9, 8, 9, 10, 11,
          12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21,
          22, 23, 24, 25, 24, 25, 26, 27,
          28, 29, 28, 29, 30, 31, 32, 1]
    pt = [16, 7, 20, 21, 29, 12, 28, 17,
          1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9,
          19, 13, 30, 6, 22, 11, 4, 25]
    ivp = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
    sb = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]
    # print(sb[1])
    p = ""

    for i in range(0, 64):
        p += text[ip[i] - 1]

    halfleft = p[0:32]
    # print(halfleft)
    halfright = p[32:64]

    for i in range(15, -1, -1):
        # print('ntered')
        # print(key[i])
        # print(len(key),i)
        right = ""
        xr = ""
        ct = 0
        for j in range(0, 48):
            right += halfright[ep[j] - 1]
            # ct=ct+1
        # print(right)
        # print(ct)
        xr = xoring(key[i], right)
        res = ""
        row = ""
        cl = ""
        # print(len(xr))
        f = 0
        for j in range(0, 8):
            # print(f)
            row += xr[f]
            row += xr[f + 5]
            # row+=xr[15]
            # print(row)
            cl += xr[f + 1] + xr[f + 2] + xr[f + 3] + xr[f + 4]
            # print(cl)
            col = bintodec(cl)
            rw = bintodec(row)
            val = sb[j][rw][col]
            # print(val)
            res += dectobin(val)
            f = f + 6
            row = ""
            cl = ""
            # not done yet
        p2 = ""

        # print(res)
        # print(len(res))
        for j in range(0, 32):
            p2 += res[pt[j] - 1]
        last = xoring(p2, halfleft)
        # print(last)
        halfleft = last
        if i > 0:
            t = halfright
            halfright = halfleft
            halfleft = t
        # f=halfleft+halfright
        # print(f)
    full = halfleft + halfright
    cipher = ""
    for i in range(0, 64):
        cipher += full[ivp[i] - 1]
    return cipher


def encrypt(PlainText,key):
    #key="yes is"
    x = toBinary(PlainText)

    # print(x)
    # print(len(PlainText))
    # print(len)
    # while len(x) % 64 != 0:
    #     x += '00000000'
    x.zfill(64)
    #keybinary = toBinary(key)
    kemz = keygeneration(key)
    # print(kemz)
    INDEXING = 0
    kemzo = ''

    while INDEXING + 64 <= len(x):
        kemzo += des(kemz, x[INDEXING:INDEXING + 64])
        INDEXING += 64
    # print(binary_to_string(kemzo))
    return kemzo


# KEYS=[]
# j=0
# for i in range(15,-1,-1):
##  j+=1
# INDEXING +=64
# print(kemzo)
def decrypt(kemzo,key):
    #key = "yes is"
    #keybinary = toBinary(key)
    kemz = keygeneration(key)

    INDEXING2 = 0
    plainss = ''
    while INDEXING2 + 64 <= len(kemzo):
        plainss += ddes(kemz, kemzo[INDEXING2:INDEXING2 + 64])
        INDEXING2 += 64
    # print(plainss)
    plainssfinal = binary_to_string(plainss)
    pattern = r"[^a-zA-Z!@#$%^&*(),.?\":{}|<>]"
    filtered_text = re.sub(pattern, '', plainssfinal)
    # print(plainssfinal)

    return filtered_text
