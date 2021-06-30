def reverseArray(arr):
    #below is the inbuilt function
    # arr.reverse()  
    # return arr
    a = len(arr)//2
    print(a)
    print(len(arr)%2)
    if len(arr)%2 != 0 :
        for i in range(1,a+1):
            print(i)
            (arr[a+i],arr[a-i])= (arr[a-i],arr[a+i])

            print(arr)
        return arr
    elif len(arr)%2 == 0:
        start = 0 
        end = len(arr)-1
        for x in range(len(arr)//2):
            arr[start],arr[end] = arr[end],arr[start]
            start = start + 1
            end = end -1
        return arr

print(reverseArray([2,8,9,0,6,9,7,8,5,8,8]))
