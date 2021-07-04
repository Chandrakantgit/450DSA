def maxandmin(arr): # with nlogn timecomplexity
    if len(arr) == 0:
        return None,None
    elif len(arr) == 1:
        return arr[0],arr[0]
    arr = arr.sort()
    max = arr[len(arr)-1]
    min = arr[0]
    return max,min

print(maxandmin([8,7]))