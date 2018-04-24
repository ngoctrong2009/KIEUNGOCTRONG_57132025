print("nhap n:")
n = int(input())
for i in range(1,n):
    print(i)
print("tong so chan cua day")
for i in range(1,n):
    if(i%2 == 0):
        tong = tong + i
print(tong)