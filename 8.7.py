x = int(input("nhập số điện:"))
if x<=50:
    print(x*1678)
elif x<=100:
    print(50*1678+(x-50)*1734)
elif x<=200:
    print(50*1678+50*1734+(x-100)*2014)
elif x<=300:
    print(50*1678+50*1734+100*2014+(x-200)*2536)
elif x<=400:
    print(50*1678+50*1734+100*2014+100*2536+(x-300)*2834)
else:
    print(50*1678+50*1734+100*2014+100*2536+100*2834+(x-400)*2927)
