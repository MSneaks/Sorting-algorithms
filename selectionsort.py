a = [2,7,4,56,73,46,90,43]
smallest = 0
for i in range(len(a)):
	smallest = i
	for j in range(i+1,len(a)):
		if a[j] <a[smallest] :
			smallest = j
	a[i],a[smallest] = a[smallest],a[i]

print(a)