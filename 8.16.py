a = float(input("số nguyên a:"))
b = float(input("số nguyên b:"))
def ucln(a,b):
    if b == 0:
        return a
    else: b!=0
    return ucln(b, a%b)
print("ucln=", ucln(a,b))
