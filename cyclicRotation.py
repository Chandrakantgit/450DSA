#function for cyclic rotation in an array
# The approach would be to save last element in a variable,
# then looping through the array to move a value to next index.
def cyclicRotation(arrr):
    arr = arrr
    a = arr[len(arr)-1]
    print(a)
    i=len(arr)-2
    while(i>-1):
        print(i)
        arr[i+1]= arr[i]
        i=i-1
        print(arr)


    arr[0] = a
    return arr

print(cyclicRotation([1,2,3,5,6,7,8,9,90]))