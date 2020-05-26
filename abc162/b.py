N = int(input())
mysum = 0
for i in range(1,N+1):
	if i%3 == 0 or i%5 == 0:
		mysum += 0
	else: 
		mysum += i
print(mysum)
