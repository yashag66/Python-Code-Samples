def bubble_sort(input_array):
	len_arr = len(input_array)
	for i in range(len_arr):
		for j in range(len_arr - i - 1):
			if(input_array[j] > input_array[j+1]):
				input_array[j] += input_array[j+1]
				input_array[j+1] = input_array[j] - input_array[j+1]
				input_array[j] = input_array[j] - input_array[j+1]

	return input_array

print(bubble_sort([23, 45, 11, 234, 5, 2, 8, 90]))