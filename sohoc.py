print("nhap a :")
a = float(input())
print("nhap b :")
b = float(input())
print("1.Tông | 2.hieu | 3.tich | 4.thuong | 5.chia du | 6.luy thua")
print("moi ban chon :")
n = int(input())
if (n < 1 or n > 6):
    print("error")
elif (n == 1):
    tong = a + b
    print (a ," + ", b , " = ", tong)
elif (n == 2):
    hieu = a - b
    print(a," - ",b," = ",hieu)
elif (n == 3):
    tich = a * b
    print(a," * ",b," = ",tich)
elif (n == 4):
    thuong = a / b
    print(a," / ",b," = ",thuong)
elif (n == 5):
    du = a % b
    print(a," % ",b," = ",du)
elif (n == 6):
    luythua = a ** b
    print(a, " ** ",b," = ",luythua)