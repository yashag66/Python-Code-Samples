def merge_sort(alist):
	print('Spliting', alist)
	if len(alist) > 1:
		mid = len(alist)//2
		l = alist[:mid]
		h = alist[mid:]

		merge_sort(l)
		merge_sort(h)

		i = 0
		j = 0
		k = 0
		while i < len(l) and j < len(h):
			if l[i] < h[j]:
				alist[k] =  l[i]
				i += 1
			else:
				alist[k] = h[j]
				j += 1
			k += 1

		while i < len(l):
			alist[k] = l[i]
			i += 1
			k += 1

		while j < len(h):
			alist[k] = h[j]
			j += 1
			k += 1


	print('Merging', alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)