#10.1
import math 
a=int(input("nhap a"))
b=int(input("nhap b"))
c=int(input("nhap c"))
d=int(input("nhap d"))
print(max(a,b,c,d))
print(min(a,b,c,d))

#10.2
import math 
x=int(input("nhap x:"))
print(abs(x))

#10.3
x=int(input("nhập x"))
n=int(input("nhập n"))
print("s=",pow(pow(x,2)+1,n))

#10.4
x=int(input("nhập x"))
n=int(input("nhập n"))
print("s=",pow(pow(x,2)+x+1,n)+pow(pow(x,2)-x+1,n))

#10.5

#10.6
a=int(input("nhập a:"))
while True:
    if a==0:
        a=int(input("a phải khác 0. nhập lại a:"))
    else:
        break 
b=int(input("nhập b:"))
while True:
    if b==0:
        b=int(input("b phải khác 0. nhập lại b:"))
    else:
        break
c=int(input("nhập c:"))
delta= b**2 -4*a*c
import math
if delta<0:
    print("phương trình vô nghiệm")
elif delta==0:
    print("phương trình có nghiệm kép x1=x2=", -(b/(2*a)))
else:
    print("phương trình có hai nghiệm phân biệt:")
    print("x1=", (-(b) + math.sqrt(delta)/(2*a)))
    print("x2=", (-(b) - math.sqrt(delta)/(2*a)))

#10.7
str1 = " a b c d e f duck "
str2 = "duck"
print("Nhập chuỗi S:",str1)
print("Nhập chuỗi tìm S_find:",str1.find(str2))
print("Số lần S_sub xuất hiện trong S:",str1.count("d"))
print("Chuỗi S sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:",str1.strip())
print("Chuỗi S sau khi thay thế:",str1.replace("duck","dog"))

#10.8
x=int(input("nhập ngày:"))
y=int(input("nhập tháng:"))
z=int(input("nhập tháng:"))
print("ngày:", x ,"tháng:", y, "năm:", z)
import calendar 
print(calendar.isleap(z))
print(calendar.weekday(z,y,x))
print(calendar.monthrange(z,y))
