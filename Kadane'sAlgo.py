#This is basically kadane's Algorithm.
def largestSum(array):
    max_ending_here = 0
    max_so_far =0
    for x in array:
        max_ending_here = max_ending_here + x
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

print(largestSum([1,2,4,-2]))