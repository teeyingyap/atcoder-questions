S = str(input())

N = len(S)
palinBool = "No"

if S== S[::-1] and S[:((N-1)//2)] == S[((N-1)//2)-1::-1] and S[((N+3)//2)-1:] == S[N-1:((N+3)//2)-2:-1]:
	palinBool = "Yes"

print(palinBool)
