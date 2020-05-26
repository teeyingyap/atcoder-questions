from math import gcd 

mysum = 0
K = int(input())
for i in range(1,K+1):
	for j in range(1,K+1):
		for k in range(1,K+1):
			mysum += gcd(gcd(i,j),k)

print(mysum)
