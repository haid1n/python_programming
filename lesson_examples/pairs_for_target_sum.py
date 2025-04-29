# Give the target pair(s) of numbers for the sum
def pairs_for_target_sum(array, target_sum):
	# Arranges the elements in ascending order
	array.sort()

	left = 0

	right = len(array) - 1

	while (left <= right):
		# Start picking element from the left
		if (array[left] + array[right] < target_sum):
			left = left + 1

		# Start picking element from the right
		elif (array[left] + array[right] > target_sum):
			right = right - 1

		# Give the pair of numbers for the target sum
		elif (array[left] + array[right] == target_sum):
			print(f"Values of array are {array[left]} and {array[right]}")

			right = right - 1

			left = left + 1


array = [5,7,4,3,9,8,19,23]

sum1 = 17

pairs_for_target_sum(array, sum1)
