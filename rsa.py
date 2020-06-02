from decimal import Decimal 

#Kiểm tra số nguyên tố
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


#Nhập p , q
p=int(input('Nhap so nguyen to p: '))
q=int(input('Nhap so nguyen to q (khac p): '))

#Kiểm tra 2 số nguyên tố
if not (isPrime(p) and isPrime(q) ):
    raise ValueError('2 so phai la so nguyen to.')
elif (p == q):
    raise ValueError('2 so khong duoc bang nhau.')

#P Q đã nhập
print("P va Q da nhap:\np=" + str(p) + ", q=" + str(q) + "\n")

# n = p * q
n=p*q
print("n = p * q = " + str(n) + "\n")

# phi(n) = (p-1)(q-1)
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")


# Ước chung lớn nhất
def gcd(a, b):
    while b != 0:
      c = a % b
      a = b
      b = c
    return a
    
#Tính nghịch đảo modul (Euclid) -- Modular multiplicative inverse
def modinv(a, m):
    for x in range(1, m):
      if (a * x) % m == 1:
        return x
    return None
    
# Mảng hiện các số nguyên tố cùng nhau -> chọn e
def coprimes(a):
    l = []
    for x in range(2, a):
      if gcd(a, x) == 1 and modinv(x,phi) != None:
        l.append(x)
    for x in l:
      if x == modinv(x,phi):
        l.remove(x)
    return l

#Xuat file
def publickey(e,n):
    sn = str(n)
    se = str(e)
    file = open("public.txt", "w+")
    file.write("PublicKey: (" + se + "," + sn + ")");
    file.close()
    
def privatekey(d,n):
    sn = str(n)
    sd = str(d)
    file = open("private.txt", "w+")
    file.write("PrivateKey: (" + sd + "," + sn + ")");
    file.close()
    

#In mảng các số nguyên tố cùng nhau
print("Chon e trong cac so duoi day:\n")
print(str(coprimes(phi)) + "\n")

#Chọn e
e=int(input())

#Tính d
d=modinv(e,phi)

print("\n Khoa cong khai (Public Key) cua ban la: (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Khoa bi mat (Private Key) cua ban la: (d=" + str(d) + ", n=" + str(n) + ").\n")

#Nhập message -- M
s = input("Nhap message de ma hoa: ")
print("\nMessage da nhap: " + s + "\n")


#Message đã mã hóa
ctt = Decimal(0) 
ctt =int(s)**e
ct = ctt % n


#Message đã giải mã
dtt = Decimal(0) 
dtt = ct**d 
dt = dtt % n 


#Xuất file public key và private key
publickey(e,n)
privatekey(d,n)


#In ra màn hình
print("Encrypting: " + str(s) + "^" + str(e) + " Mod " + str(n) + "\n") 
print("Message da ma hoa: " + str(ct) + "\n")

print("Decrypting: " + str(ct) + "^" + str(d) + " Mod " + str(n) + "\n") 
print("Message da giai ma: " + str(dt) + "\n")

print("Xuat file thanh cong")
