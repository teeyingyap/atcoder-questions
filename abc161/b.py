N,M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

totalVotes = 0
for i in range(len(A)):
	totalVotes += A[i]

selected = 0
for i in range(len(A)):
	if A[i] >= totalVotes/(4*M):
		selected +=1 

if selected >= M:
	print("Yes")
else: 
	print("No")
