arr=[]
n = input("nhap n:")
for i in range (0, n):
	d = input()
	arr.append(d)
print("mang vua nhap :")
for i in range (0,len(arr)):
	print(arr[i])
print("sap xep :")
arr.sort()
print(arr)
