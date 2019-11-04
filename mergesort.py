

def mergesort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergesort(L)
		mergesort(R)

		i = k = j = 0

		while i < len(L) and j<len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while(j<len(R)):
			arr[k]= R[j]
			j+=1
			k+=1
		


a= [5,3,8,9,10,98,45,7,4,3,57,98,65,3,56,64,456,8,8,9]
print(a)
mergesort(a)
print(a)