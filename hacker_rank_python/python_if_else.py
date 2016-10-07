value = int(input().strip())
if value % 2 == 1:
	print('Weird')
elif 2 <= value <= 5:
	print('Not Weird')
elif 6 <= value <= 20:
	print('Weird')
else:
	print('Not Weird')
