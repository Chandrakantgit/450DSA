def getMaxMin(low,high,arr):
    arr_max = arr[low]
    arr_min = arr[low]

    if low == high:
        return arr_max,arr_min

    elif low == high -1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
            return arr_max,arr_min
        elif arr[low] < arr[high]:
            arr_max = arr[high]
            arr_min = arr[low]
            return arr_max,arr_min
        else:
            arr_max = arr[low]
            arr_min = arr[high]
            return arr_max,arr_min

    else:
        mid = int((low+high)/2)
        arr_max1,arr_min1 = getMaxMin(low,mid,arr)
        arr_max2,arr_min2 = getMaxMin(mid+1,high,arr)

    return (max(arr_max1,arr_max2),min(arr_min1,arr_min2))

print(getMaxMin(0,6,[8,4,534,56,32,21,23]))