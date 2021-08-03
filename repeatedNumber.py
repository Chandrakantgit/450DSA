# This is a solution to the question but has O(n^2) time complexity,but it is a solution.
def repeatedNumber(array):
    tempArr = set(array)
    for x in tempArr:
        if array.count(x) == 2:
            return x
    return -1

print(repeatedNumber([2,5,4,3]))