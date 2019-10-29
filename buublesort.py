a =[ 10,9,8 ,7,8,3,76,53,57,93,20]

def bubbleSort(a ):
	for i in range(len(a)):
		for j in range(len(a)-1):
			if a[j]> a[j+1]:
				a[j],a[j+1] = a[j+1], a[j]

bubbleSort(a)
print(a)