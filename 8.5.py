a = float(input("nhập số năm:"))
if((a%4==0)&(a%100!=0)or(a%400==0)):
    print("năm nhuận")
else:
    print("không phải năm nhuận")
