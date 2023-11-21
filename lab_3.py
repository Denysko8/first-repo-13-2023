a = int(input('First point = '))
b = int(input('Second point = '))
amount = 0
list = []

for i in range(a,b+1):
	if '5' not in str(i):
		print(i)
		list.append(i)
		amount += 1

print ("Amount =",amount)
print(len(list))

#C:\Users\admin\Desktop\Python\Lab_3\lab_3.py