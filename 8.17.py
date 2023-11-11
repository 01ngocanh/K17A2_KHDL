a = float(input("số nguyên a:"))
b = float(input("số nguyên b:"))
def ucln(a,b):
    if b == 0:
        return a
    else: b!=0
    return ucln(b, a%b)
def bcnn(a,b):
    return int((a*b) / ucln(a,b))
print("bcnn=", bcnn(a,b))
