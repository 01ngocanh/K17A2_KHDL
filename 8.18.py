n = int(input("nhập số:"))
tong = 0
for i in range(1, n):
    if(n % i == 0):
        tong +=i
if(tong == n):
    print("là số hoàn hảo", n)
else:
    print("không là số hoàn hảo", n)
    
