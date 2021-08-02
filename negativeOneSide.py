# Approach to solve this question :
#     use 2 counters to iterate over array so one(i) takes the index of value is next to a -ve value.
#     This value would be exchanged by the negative value which j would find while iterating through the array. 
def negativeOneSide(arr):
    i = 0
    j = 0
    while(j<len(arr)):
        if arr[j] < 0 and j == i:
            i = i+1
        else:
            if arr[j]< 0 and j != i:
                arr[j],arr[i] = arr[i],arr[j]
                i = i + 1
        j = j+1
    return arr
print(negativeOneSide([78,8,56,90,-5]))
