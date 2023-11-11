n = int(input("Nhập vào một số tự nhiên: "))
for i in range(2, n):
    if n % i == 0:
        print("không phải là số nguyên tố".format(n))
        break
else:
    print("là số nguyên tố".format(n))
