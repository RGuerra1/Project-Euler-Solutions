days = 0
for i in range(1900,2001):
	days +=30*4 +31*7 + 27
	if i%4 == 0 and i%400 != 0:
		days +=1
sundays = days/7
print sundays