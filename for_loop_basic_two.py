# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
biggie_size([-1, 3, 5, -5])
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            count += 1
    list[len(list) - 1] = count
    return list
count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum
sum_total([1,2,3,4])
sum_total([6,3,-2])
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# Average - Create a function that takes a list and returns the average of all the values.
def average(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg
average([1,2,3,4])
# Example: average([1,2,3,4]) should return 2.5

# Length - Create a function that takes a list and returns the length of the list.
def length(list):
    return len(list)
length([37,2,1,-9])
length([])
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
    if len(list) == 0:
        return False
    else: 
        min = list[0]
        for i in range(1, len(list)):
            if list[i] < min:
                min = list[i]
        return min
minimum([37,2,1,-9])
minimum([])
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(list):
    if len(list) == 0:
        return False
    else: 
        max = list[0]
        for i in range(1, len(list)):
            if list[i] > max:
                max = list[i]
        return max
maximum([37,2,1,-9])
maximum([])
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
    sumTotal = 0
    min = list[0]
    max = list[0]

    for i in range(0, len(list)):
        sumTotal += list[i]
        if list[i] < min:
            min = list[i]
        elif list[i] > max:
            max = list[i]
    avg = sumTotal / len(list)
    dict = {
        'sumTotal': sumTotal, 
        'average':avg, 
        'minimum': min, 
        'maximum': max, 
        'length': len(list)
        }
    return dict
ultimate_analysis([37,2,1,-9])
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(list):
    for i in range(0, int(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list) - i - 1]
        list[len(list) - i - 1] = temp
    return list
reverse_list([37,2,1,-9])
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]