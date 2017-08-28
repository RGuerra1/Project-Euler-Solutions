n=100
value = 1
for i in range(2,n+1):
	value = value*i
print value
sol_value = 0
for char in str(value):
	sol_value+= int(char)
print sol_value