n = int(input())
H = []
A = []
c = 0
for i in range(n):
	h,a = map (int, input().split())
	H.append(h)
	A.append(a)
for i in H:
	for j in A:
		if i == j:
			c +=1
print(c)
