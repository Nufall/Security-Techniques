# CipherText = [0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0]
# key =       [1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1]
# CipherText = [0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0]
# key = [0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,1]
# from client2 import *

THEFINALPLAIN = []
THEFINALCIPHER = []


def SubNib(Given):
    Base = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']

    SBox = ['1001', '0100', '1010', '1011', '1101', '0001', '1000', '0101', '0110', '0010', '0000', '0011', '1100',
            '1110', '1111', '0111']
    for i, x in enumerate(Base):
        if str(Given) == x:
            # print('given: ',str(Given) )
            # print('x: ',str(x) )
            return (SBox[i])


def RotNib(Given):
    # print(w1)
    new = []
    swap = Given[0:4]
    new[0:4] = Given[4:8]
    new[4:8] = swap[0:4]
    return new


def ShiftRows(Given):
    new = Given[0:16]
    swap = Given[4:8]
    new[4:8] = Given[12:16]
    new[12:16] = swap[0:4]
    return new


def InverseSubNib(Given):
    Base = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']

    SBox = ['1001', '0100', '1010', '1011', '1101', '0001', '1000', '0101', '0110', '0010', '0000', '0011', '1100',
            '1110', '1111', '0111']
    for i, x in enumerate(SBox):
        if str(Given) == x:
            # print('given: ',str(Given) )
            # print('x: ',str(x) )
            return (Base[i])


def string_to_binary(string):
    binary_string = ''

    for character in string:
        ascii_value = ord(character)
        binary_value = bin(ascii_value)[2:]
        binary_value = binary_value.zfill(8)
        binary_string += binary_value

    return binary_string


def binary_to_string(binary_string):
    string = ''
    for i in range(0, len(binary_string), 8):
        binary_value = binary_string[i:i + 8]
        decimal = int(binary_value, 2)
        character = chr(decimal)
        string += character

    return string


def GF(a, b):
    if a < 0 or b < 0:
        return 0
    Multiplication = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                      [2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
                      [3, 6, 5, 12, 15, 10, 9, 11, 8, 13, 14, 7, 4, 1, 2],
                      [4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
                      [5, 10, 15, 7, 2, 13, 8, 14, 11, 4, 1, 9, 12, 3, 6],
                      [6, 12, 10, 11, 13, 7, 1, 5, 3, 9, 15, 14, 8, 2, 4],
                      [7, 14, 9, 15, 8, 1, 6, 13, 10, 3, 4, 2, 5, 12, 11],
                      [8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1],
                      [9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14],
                      [10, 7, 13, 14, 4, 9, 3, 15, 5, 8, 2, 1, 11, 6, 12],
                      [11, 5, 14, 10, 1, 15, 4, 7, 12, 2, 9, 13, 6, 8, 3],
                      [12, 11, 7, 5, 9, 14, 2, 10, 6, 1, 13, 15, 3, 4, 8],
                      [13, 9, 4, 1, 12, 8, 5, 2, 15, 11, 6, 3, 14, 10, 7],
                      [14, 15, 1, 13, 3, 2, 12, 9, 7, 6, 8, 4, 10, 11, 5],
                      [15, 13, 2, 9, 6, 4, 11, 1, 14, 12, 3, 8, 7, 5, 10]]
    return Multiplication[a][b]


def binaryToDecimal(n):
    return int(n, 2)


def Encrypt(plaintext, key):
    plaintextstr = str(plaintext[0])

    for x in range(1, 16):
        plaintextstr = str(plaintextstr) + str(plaintext[x])
    w0 = key[0:8]
    w1 = key[8:16]
    print(w0)
    print(w1)
    print(w1)
    rotw1 = RotNib((w1))
    # w1=key[8:16]
    print('here: ', rotw1)
    print(w1)
    # w0 = key[0:8]
    w1str1 = rotw1[0]
    w1str2 = rotw1[4]
    # print(w0)
    # plaintext = ['1','1','0','1','0','1','1','1','0','0','1','0','1','0','0','0']
    # key =       ['0','1','0','0','1','0','1','0','1','1','1','1','0','1','0','1']

    for x in range(1, 4):
        w1str1 = str(w1str1) + str(rotw1[x])
    for x in range(5, 8):
        w1str2 = str(w1str2) + str(rotw1[x])

    print(w1str1)
    print(w1str2)
    w1str1 = SubNib(str(w1str1))
    w1str2 = SubNib(str(w1str2))
    print(w1str1)
    print(w1str2)
    w1forw2 = (str(w1str1) + str(w1str2))
    print(w1forw2)
    constant = '10000000'
    w0str = str(key[0])

    for x in range(1, 8):
        w0str = str(w0str) + str(key[x])
    # print (w0str)
    # print(constant)
    # print(w1forw2)

    w2 = [(int(a) ^ int(b) ^ int(c)) for a, b, c in zip(w0str, constant, w1forw2)]

    w1str = str(w1[0])

    for x in range(1, 8):
        w1str = str(w1str) + str(w1[x])

    w2str = str(w2[0])

    for x in range(1, 8):
        w2str = str(w2str) + str(w2[x])

    w3 = [(int(a) ^ int(b)) for a, b in zip(w1str, w2str)]

    w3str = str(w3[0])

    for x in range(1, 8):
        w3str = str(w3str) + str(w3[x])
    print('Printing sub-keys')
    print(w0str)
    print(w1str)
    print(w2str)
    print(w3str)

    print(w3)
    w3forrot = w3
    rotw3 = RotNib(w3forrot)
    print(rotw3)
    w3str1 = rotw3[0]
    w3str2 = rotw3[4]
    for x in range(1, 4):
        w3str1 = str(w3str1) + str(rotw3[x])
    for x in range(5, 8):
        w3str2 = str(w3str2) + str(rotw3[x])

    print(w3str1)
    print(w3str2)
    print(w3)
    w3str1 = SubNib(str(w3str1))
    w3str2 = SubNib(str(w3str2))
    print(w3str1)
    print(w3str2)
    w3forw4 = (str(w3str1) + str(w3str2))
    print(w3forw4)
    constant2 = '00110000'
    print(w2str)
    print(constant2)
    print(w3forw4)
    w4 = [(int(a) ^ int(b) ^ int(c)) for a, b, c in zip(w2str, constant2, w3forw4)]
    print(w4)

    w4str = str(w4[0])

    for x in range(1, 8):
        w4str = str(w4str) + str(w4[x])
    print(w4str)
    w5 = [(int(a) ^ int(b)) for a, b in zip(w3str, w4str)]
    print(w5)

    w5str = str(w5[0])

    for x in range(1, 8):
        w5str = str(w5str) + str(w5[x])
    print(w5str)
    k0 = w0
    k0.extend(w1)

    k1 = w2
    k1.extend(w3)

    k2 = w4
    k2.extend(w5)

    print(k0)
    print(k1)
    print(k2)
    k0str = str(k0[0])
    for x in range(1, 16):
        k0str = str(k0str) + str(k0[x])

    k1str = str(k1[0])
    for x in range(1, 16):
        k1str = str(k1str) + str(k1[x])

    k2str = str(k2[0])
    for x in range(1, 16):
        k2str = str(k2str) + str(k2[x])

    print('K0: ' + k0str)
    print('K1: ' + k1str)
    print('K2: ' + k2str)
    round1 = [(int(a) ^ int(b)) for a, b in zip(plaintextstr, k0str)]
    print(round1)

    round1str1 = str(round1[0])
    for x in range(1, 4):
        round1str1 = str(round1str1) + str(round1[x])

    round1str2 = str(round1[4])
    for x in range(5, 8):
        round1str2 = str(round1str2) + str(round1[x])

    round1str3 = str(round1[8])
    for x in range(9, 12):
        round1str3 = str(round1str3) + str(round1[x])

    round1str4 = str(round1[12])
    for x in range(13, 16):
        round1str4 = str(round1str4) + str(round1[x])

    print(round1str1)
    print(round1str2)
    print(round1str3)
    print(round1str4)
    after1str = SubNib(round1str1)
    after2str = SubNib(round1str2)
    after3str = SubNib(round1str3)
    after4str = SubNib(round1str4)
    print(after1str)
    print(after2str)
    print(after3str)
    print(after4str)
    str_1 = after1str + after2str + after3str + after4str
    beforeshiftrows = list(str_1.strip(" "))
    beforeshiftrows = [int(i) for i in beforeshiftrows]
    print(beforeshiftrows)
    aftershiftrow = ShiftRows(beforeshiftrows)
    print(beforeshiftrows)
    print(aftershiftrow)
    s00 = str(aftershiftrow[0])
    for x in range(1, 4):
        s00 = str(s00) + str(aftershiftrow[x])
    print(s00)

    s10 = str(aftershiftrow[4])
    for x in range(5, 8):
        s10 = str(s10) + str(aftershiftrow[x])
    print(s10)

    s01 = str(aftershiftrow[8])
    for x in range(9, 12):
        s01 = str(s01) + str(aftershiftrow[x])
    print(s01)

    s11 = str(aftershiftrow[12])
    for x in range(13, 16):
        s11 = str(s11) + str(aftershiftrow[x])
    print(s11)
    M = [1, 4, 4, 1]

    news00 = GF(M[0] - 1, binaryToDecimal(s00) - 1) ^ GF(M[1] - 1, binaryToDecimal(s10) - 1)
    news10 = GF(M[2] - 1, binaryToDecimal(s00) - 1) ^ GF(M[3] - 1, binaryToDecimal(s10) - 1)

    news01 = GF(M[0] - 1, binaryToDecimal(s01) - 1) ^ GF(M[1] - 1, binaryToDecimal(s11) - 1)
    news11 = GF(M[2] - 1, binaryToDecimal(s01) - 1) ^ GF(M[3] - 1, binaryToDecimal(s11) - 1)

    # news10 = GF(M[2],binaryToDecimal(s00)-1) ^ GF(M[3],binaryToDecimal(s10)-1)
    # news00 = (M[0] * binarys00) + (M[1] * binarys10)
    news00 = bin(news00)[2:].zfill(4)
    news10 = bin(news10)[2:].zfill(4)
    news01 = bin(news01)[2:].zfill(4)
    news11 = bin(news11)[2:].zfill(4)
    # print(bin(news10)[2:].zfill(4))
    outputofr1 = str(news00) + str(news10) + str(news01) + str(news11)
    print(outputofr1)
    inputforround2 = [(int(a) ^ int(b)) for a, b in zip(outputofr1, k1str)]
    print(inputforround2)

    inputr21 = str(inputforround2[0])
    for x in range(1, 4):
        inputr21 = str(inputr21) + str(inputforround2[x])
    print(inputr21)

    inputr22 = str(inputforround2[4])
    for x in range(5, 8):
        inputr22 = str(inputr22) + str(inputforround2[x])
    print(inputr22)

    inputr23 = str(inputforround2[8])
    for x in range(9, 12):
        inputr23 = str(inputr23) + str(inputforround2[x])
    print(inputr23)

    inputr24 = str(inputforround2[12])
    for x in range(13, 16):
        inputr24 = str(inputr24) + str(inputforround2[x])
    print(inputr24)
    subnibr21 = SubNib(inputr21)
    subnibr22 = SubNib(inputr22)
    subnibr23 = SubNib(inputr23)
    subnibr24 = SubNib(inputr24)
    print(subnibr21, subnibr22, subnibr23, subnibr24)
    allsubnibs = subnibr21 + subnibr22 + subnibr23 + subnibr24
    outputofr2 = list(allsubnibs.strip(" "))
    outputofr2 = [int(i) for i in allsubnibs]

    outputofr2 = ShiftRows(outputofr2)
    print(outputofr2)
    CipherText = [(int(a) ^ int(b)) for a, b in zip(outputofr2, k2str)]
    print(CipherText[0:4])
    print('CipherText: ')
    print(CipherText[0:4])
    print(CipherText[4:8])
    print(CipherText[8:12])
    print(CipherText[12:16])
    return CipherText


def Decrypt(CipherText, key):
    indexing = 0
    print('CipherTexy = ', CipherText)
    CipherTextstr = str(CipherText[0])
    w0 = key[0:8]
    w1 = key[8:16]
    for x in range(1, 16):
        CipherTextstr = str(CipherTextstr) + str(CipherText[x])
    print(CipherTextstr)
    print(w1)
    rotw1 = RotNib((w1))
    # w1=key[8:16]
    print(rotw1)
    print(w1)
    # w0 = key[0:8]
    w1str1 = rotw1[0]
    w1str2 = rotw1[4]
    # print(w0)
    # plaintext = ['1','1','0','1','0','1','1','1','0','0','1','0','1','0','0','0']
    # key =       ['0','1','0','0','1','0','1','0','1','1','1','1','0','1','0','1']
    for x in range(1, 4):
        w1str1 = str(w1str1) + str(rotw1[x])
    for x in range(5, 8):
        w1str2 = str(w1str2) + str(rotw1[x])

    print(w1str1)
    print(w1str2)
    w1str1 = SubNib(str(w1str1))
    w1str2 = SubNib(str(w1str2))
    print(w1str1)
    print(w1str2)
    w1forw2 = (str(w1str1) + str(w1str2))
    print(w1forw2)
    constant = '10000000'
    w0str = str(key[0])

    for x in range(1, 8):
        w0str = str(w0str) + str(key[x])
    # print (w0str)
    # print(constant)
    # print(w1forw2)

    w2 = [(int(a) ^ int(b) ^ int(c)) for a, b, c in zip(w0str, constant, w1forw2)]

    w1str = str(w1[0])

    for x in range(1, 8):
        w1str = str(w1str) + str(w1[x])

    w2str = str(w2[0])

    for x in range(1, 8):
        w2str = str(w2str) + str(w2[x])

    w3 = [(int(a) ^ int(b)) for a, b in zip(w1str, w2str)]

    w3str = str(w3[0])

    for x in range(1, 8):
        w3str = str(w3str) + str(w3[x])
    print('Printing sub-keys')
    print(w0str)
    print(w1str)
    print(w2str)
    print(w3str)

    print(w3)
    w3forrot = w3
    rotw3 = RotNib(w3forrot)
    print(rotw3)
    w3str1 = rotw3[0]
    w3str2 = rotw3[4]
    for x in range(1, 4):
        w3str1 = str(w3str1) + str(rotw3[x])
    for x in range(5, 8):
        w3str2 = str(w3str2) + str(rotw3[x])

    print(w3str1)
    print(w3str2)
    print(w3)
    w3str1 = SubNib(str(w3str1))
    w3str2 = SubNib(str(w3str2))
    print(w3str1)
    print(w3str2)
    w3forw4 = (str(w3str1) + str(w3str2))
    print(w3forw4)
    constant2 = '00110000'
    print(w2str)
    print(constant2)
    print(w3forw4)
    w4 = [(int(a) ^ int(b) ^ int(c)) for a, b, c in zip(w2str, constant2, w3forw4)]
    print(w4)

    w4str = str(w4[0])

    for x in range(1, 8):
        w4str = str(w4str) + str(w4[x])
    print(w4str)
    w5 = [(int(a) ^ int(b)) for a, b in zip(w3str, w4str)]
    print(w5)

    w5str = str(w5[0])

    for x in range(1, 8):
        w5str = str(w5str) + str(w5[x])
    print(w5str)
    k0 = w0
    k0.extend(w1)

    k1 = w2
    k1.extend(w3)

    k2 = w4
    k2.extend(w5)

    print(k0)
    print(k1)
    print(k2)
    k0str = str(k0[0])
    for x in range(1, 16):
        k0str = str(k0str) + str(k0[x])

    k1str = str(k1[0])
    for x in range(1, 16):
        k1str = str(k1str) + str(k1[x])

    k2str = str(k2[0])
    for x in range(1, 16):
        k2str = str(k2str) + str(k2[x])

    print('K0: ' + k0str)
    print('K1: ' + k1str)
    print('K2: ' + k2str)
    round1 = [(int(a) ^ int(b)) for a, b in zip(CipherText, k2str)]
    print(round1)
    AfterInverseShiftRow = ShiftRows(round1)
    print(round1)
    print(AfterInverseShiftRow)
    AfterInverseSTR1 = str(AfterInverseShiftRow[0])
    for x in range(1, 4):
        AfterInverseSTR1 = str(AfterInverseSTR1) + str(AfterInverseShiftRow[x])

    AfterInverseSTR2 = str(AfterInverseShiftRow[4])
    for x in range(5, 8):
        AfterInverseSTR2 = str(AfterInverseSTR2) + str(AfterInverseShiftRow[x])

    AfterInverseSTR3 = str(AfterInverseShiftRow[8])
    for x in range(9, 12):
        AfterInverseSTR3 = str(AfterInverseSTR3) + str(AfterInverseShiftRow[x])

    AfterInverseSTR4 = str(AfterInverseShiftRow[12])
    for x in range(13, 16):
        AfterInverseSTR4 = str(AfterInverseSTR4) + str(AfterInverseShiftRow[x])
    print(AfterInverseSTR1, AfterInverseSTR2, AfterInverseSTR3, AfterInverseSTR4)
    InvShiftRow1 = InverseSubNib(AfterInverseSTR1)
    InvShiftRow2 = InverseSubNib(AfterInverseSTR2)
    InvShiftRow3 = InverseSubNib(AfterInverseSTR3)
    InvShiftRow4 = InverseSubNib(AfterInverseSTR4)
    print(InvShiftRow1, InvShiftRow2, InvShiftRow3, InvShiftRow4)
    forround2 = str(InvShiftRow1) + str(InvShiftRow2) + str(InvShiftRow3) + str(InvShiftRow4)
    print(forround2)
    beforerinvermixcol = [(int(a) ^ int(b)) for a, b in zip(forround2, k1str)]
    print(beforerinvermixcol)
    s00inverse1 = str(beforerinvermixcol[0])
    for x in range(1, 4):
        s00inverse1 = str(s00inverse1) + str(beforerinvermixcol[x])

    s00inverse2 = str(beforerinvermixcol[4])
    for x in range(5, 8):
        s00inverse2 = str(s00inverse2) + str(beforerinvermixcol[x])

    s00inverse3 = str(beforerinvermixcol[8])
    for x in range(9, 12):
        s00inverse3 = str(s00inverse3) + str(beforerinvermixcol[x])

    s00inverse4 = str(beforerinvermixcol[12])
    for x in range(13, 16):
        s00inverse4 = str(s00inverse4) + str(beforerinvermixcol[x])
    print(s00inverse1, s00inverse2, s00inverse3, s00inverse4)
    M = [9, 2, 2, 9]

    afterinverses00 = GF(M[0] - 1, binaryToDecimal(s00inverse1) - 1) ^ GF(M[1] - 1, binaryToDecimal(s00inverse2) - 1)
    afterinverses10 = GF(M[2] - 1, binaryToDecimal(s00inverse1) - 1) ^ GF(M[3] - 1, binaryToDecimal(s00inverse2) - 1)

    afterinverses01 = GF(M[0] - 1, binaryToDecimal(s00inverse3) - 1) ^ GF(M[1] - 1, binaryToDecimal(s00inverse4) - 1)
    afterinverses11 = GF(M[2] - 1, binaryToDecimal(s00inverse3) - 1) ^ GF(M[3] - 1, binaryToDecimal(s00inverse4) - 1)

    # news10 = GF(M[2],binaryToDecimal(s00)-1) ^ GF(M[3],binaryToDecimal(s10)-1)
    # news00 = (M[0] * binarys00) + (M[1] * binarys10)
    afterinverses00 = bin(afterinverses00)[2:].zfill(4)
    afterinverses10 = bin(afterinverses10)[2:].zfill(4)
    afterinverses01 = bin(afterinverses01)[2:].zfill(4)
    afterinverses11 = bin(afterinverses11)[2:].zfill(4)
    # print(bin(news10)[2:].zfill(4))
    print(afterinverses00, afterinverses10, afterinverses01, afterinverses11)
    beforeshiftrow2 = afterinverses00 + afterinverses10 + afterinverses01 + afterinverses11
    print(beforeshiftrow2)

    forshiftrow2 = list(beforeshiftrow2)
    for i, x in enumerate(forshiftrow2):
        forshiftrow2[i] = int(forshiftrow2[i])
    print(forshiftrow2)

    beforeinversesubnib2 = ShiftRows(forshiftrow2)
    print(beforeinversesubnib2)
    beforeinversesubnib2str1 = str(beforeinversesubnib2[0])
    for x in range(1, 4):
        beforeinversesubnib2str1 = str(beforeinversesubnib2str1) + str(beforeinversesubnib2[x])

    beforeinversesubnib2str2 = str(beforeinversesubnib2[4])
    for x in range(5, 8):
        beforeinversesubnib2str2 = str(beforeinversesubnib2str2) + str(beforeinversesubnib2[x])

    beforeinversesubnib2str3 = str(beforeinversesubnib2[8])
    for x in range(9, 12):
        beforeinversesubnib2str3 = str(beforeinversesubnib2str3) + str(beforeinversesubnib2[x])

    beforeinversesubnib2str4 = str(beforeinversesubnib2[12])
    for x in range(13, 16):
        beforeinversesubnib2str4 = str(beforeinversesubnib2str4) + str(beforeinversesubnib2[x])
    print(beforeinversesubnib2str1, beforeinversesubnib2str2, beforeinversesubnib2str3, beforeinversesubnib2str4)
    BeforeLastAddRoundKey1 = InverseSubNib(beforeinversesubnib2str1)
    BeforeLastAddRoundKey2 = InverseSubNib(beforeinversesubnib2str2)
    BeforeLastAddRoundKey3 = InverseSubNib(beforeinversesubnib2str3)
    BeforeLastAddRoundKey4 = InverseSubNib(beforeinversesubnib2str4)
    print(BeforeLastAddRoundKey1, BeforeLastAddRoundKey2, BeforeLastAddRoundKey3, BeforeLastAddRoundKey4)
    allkeys = BeforeLastAddRoundKey1 + BeforeLastAddRoundKey2 + BeforeLastAddRoundKey3 + BeforeLastAddRoundKey4
    print(allkeys)
    PlainText = [(int(a) ^ int(b)) for a, b in zip(k0, allkeys)]
    print("Plain Text: ", PlainText)
    return PlainText


def AESCallEncrypt(msg,keystring):
    THEFINALCIPHER = []


    keystest = list(keystring)
    for i, x in enumerate(keystest):
        keystest[i] = x

    key = keystest

    # key = [1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1]

    bbb = string_to_binary(msg)
    INDEX = 0
    print('length bbb: ', len(bbb))
    if len(bbb) % 16 != 0:
        bbb += '00000000'
    cipheredbinarytext = list(bbb)
    print('i wanna test here: ', cipheredbinarytext)
    for i, x in enumerate(cipheredbinarytext):
        cipheredbinarytext[i] = int(cipheredbinarytext[i])

    while INDEX + 16 <= len(cipheredbinarytext):
        ciphered = Encrypt(cipheredbinarytext[INDEX:INDEX + 16], key)
        THEFINALCIPHER.append(ciphered)
        INDEX += 16

    textbutciphered = ''
    for i, x in enumerate(THEFINALCIPHER):
        for j, y in enumerate(THEFINALCIPHER[i]):
            textbutciphered += str(y)
    print('text binary but ciphered: ', textbutciphered)

    return textbutciphered


def AESCallDecrypt(THEFINALCIPHER,keystring):
    THEFINALCIPHER2 = []
    THEFINALPLAIN = []
    for x in THEFINALCIPHER:
        THEFINALCIPHER2.append(x)
    for i, x in enumerate(THEFINALCIPHER2):
        THEFINALCIPHER2[i] = x
    THEFINALCIPHER3 = []
    IND = 0
    while IND + 16 <= len(THEFINALCIPHER2):
        THEFINALCIPHER3.append(THEFINALCIPHER2[IND:IND + 16])
        IND += 16

    #keystring = '1010001000111001'
    keystest = list(keystring)
    for i, x in enumerate(keystest):
        keystest[i] = x

    key = keystest
    print('THEFINALCIPHER: ', THEFINALCIPHER3)
    for i, x in enumerate(THEFINALCIPHER3):
        theplain = Decrypt(x, key)
        THEFINALPLAIN.append(theplain)

    textbutplain = ''
    for i, x in enumerate(THEFINALPLAIN):
        for j, y in enumerate(THEFINALPLAIN[i]):
            textbutplain += str(y)

    print('Ciphered Binary: ', THEFINALCIPHER)

    print('Plain Binary: ', THEFINALPLAIN)
    print('Plain Text: ', binary_to_string(textbutplain))
    #print('binary to string here: ' binary_to_string)
    return binary_to_string(textbutplain)
# print('msg received: ' ,messagefromclient)
# encmessage = AESCallEncrypt(messagefromclient)
# print(encmessage)
# plainttt = AESCallDecrypt(encmessage)
# print('plainttt: ', plainttt)
# print('decrypted aho: ', encmessage)
# encmsgbinarytext=''

# print(str(encmsgbinarytext))


# for x in encmsgbinarytext:
# THEFINALCIPHER2 = []
#     THEFINALCIPHER2.append(x)
# for i,x in enumerate(THEFINALCIPHER2):
#     THEFINALCIPHER2[i] = x
# THEFINALCIPHER3 = []
# IND = 0
# while IND+16 <= len(THEFINALCIPHER2):
#     THEFINALCIPHER3.append(THEFINALCIPHER2[IND:IND+16])
#     IND +=16
# print(encmessage)
# print(THEFINALCIPHER3)
# FINALPLAINBGD = AESCallDecrypt(THEFINALCIPHER3)
# client(str(encmsgbinarytext))
