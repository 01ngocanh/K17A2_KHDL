a =float(input("nhap so thu nhat:"))
b =float(input("nhap so thu hai:"))
print("phuong trinh bac nhat: -2x+7=0")
if a == 0:
    if b == 0:
        print("vo so nghiem")
    else:
        print("vo nghiem")
else:
    print("phuong trinh co nghiem x=", -b / a)
