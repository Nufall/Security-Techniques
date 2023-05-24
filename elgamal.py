import random
from math import pow
a=random.randint(2,10)
#list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def prime_gen():

    while True:
        #q = random.randint(pow(10,20),pow(10,50))
        #q = random.choice(list_of_primes)
        q = random.randint(2, 1000)
        if is_prime(q):
            return q

#To fing gcd of two numbers
def greatest_comm_divisor(a,b):
    if a<b:
        return greatest_comm_divisor(b,a)
    elif a%b==0:
        return b
    else:
        return greatest_comm_divisor(b,a%b)

#For key generation i.e. large random number
def generate_key(q):
    #key= random.randint(pow(10,20),q)
    key = random.randint(2, q)
    while greatest_comm_divisor(q,key)!=1:
        #key=random.randint(pow(10,20),q)
        key = random.randint(2, q)
    return key

def is_prime(number):

    #Returns True if the number is prime, else False.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def modulas(a,b,c):
    #calculate the value of(a ^ b) % c,
    #devide b by 2 then check remainder 2
    #y is power 2 remainder c
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c

#For asymetric encryption
def encryption_elgamal(msg,q,h,primitive_root):
    #it generates a random integer k using the generate_key() function, and computes the value of the secret key s using the modulas() function, as s = h ^ k mod q.
    #k is random
    #s is private key for the encryption
    ct=[]
    k=generate_key(q)
    s=modulas(h,k,q)
    public_key_a=modulas(primitive_root,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    #print("g^k used= ",p)
    #print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,public_key_a

#For decryption
def decryption_elgamal(ct,public_key_a,session_key,q):
    pt=[]
    h=modulas(public_key_a,session_key,q)
    print('ct: ', ct[0])
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt

def starter():
    q= prime_gen()
    primitive_root=random.randint(2,q)
    session_key=generate_key(q)
    public_key_b=modulas(primitive_root,session_key,q)
    return q,public_key_b,primitive_root,session_key

# msg=input("Enter message.")
# q,public_key_b,primitive_root,session_key = starter()
#
# capsule = '-'.join([str(q) , str(public_key_b) , str(primitive_root) , str(session_key)])
#
# capsule = (capsule.split('-'))
# print('capsule: ', capsule)
# for i,x in enumerate(capsule):
#     capsule[i] = int(x)
# print('capsule: ', capsule)
# ct,public_key_a=encryption_elgamal(msg,q,public_key_b,primitive_root)
# print('public_key_a',public_key_a)
# #print("Original Message=",msg)
# print("Encrypted Maessage=",ct)
# pt=decryption_elgamal(ct,public_key_a,session_key,q)
# d_msg=''.join(pt)
# print("Decryted Message=",d_msg)