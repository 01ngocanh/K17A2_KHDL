#9.1
#9.2
#9.3
x=int(input("nhập cân nặng(kg):"))
y=int(input("nhập chiều cao(m):"))
BMI= x/(y*y)
if BMI<18.5:
    print("gầy")
elif 18.5<BMI<24.99:
    print("bình thường")
else:
    print("thừa cân")

#9.4
n=int(input("nhập số:"))
x=int(input('nhập số:'))
S=(x**2+1)**n
print(S)

#9.5
n=int(input("nhập số:"))
x=int(input("nhập số:"))
A=((x**2+x+1)**n+(x**2-x+1)**n)
print(A)

#9.6
x = int(input("Nhap vao so nguyen duong x: "))
if x < 2:
    print("khong phai so nguyen to")
else:
    for i in range(2,x):
        if x%i == 0:
            print("khong phai so nguyen to")
            break
    else:
        print("la so nguyen to")

#9.7
x=int(input("số nguyên thứ nhất:"))
y=int(input("số nguyên thứ hai:"))
a=x//y
print(a)

#9.8
x = int(input("Nhap vao so nguyen duong x: "))
if x < 0:
    print("x phai la so nguyen duong")
else:
    if x == 0:
        print("0 khong phai la so hoan hao")
    tong = 0
    for i in range(1, x):
        if x%i==0:
            tong = tong + i
    if tong == x:
        print(" la so hoan hao")
    else:
        print(" khong phai so hoan hao")
        
#9.9
import math
r=float(input("Nhập vào bán kính: "))
a=float(input("Nhập vào chiều dài: "))
b=float(input("Nhập vào chiều rộng: "))
S=lambda r: math.pi*(r**2)
print("S=",S(r))
C=lambda r: r*2*3.14
print("C=",C(r))
P=lambda a, b: (a+b)*2
print("P=",P(a,b))
s=lambda a, b: a*b
print("s=",s(a,b))
