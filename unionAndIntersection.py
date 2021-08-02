a = [8,3,2,5,6,1,0]
b = [7,9,3,4,6]

# a and b are two sets,to find their intersection and union we have to convert them into sets.
# Then you know which operators should be used for union and intersection(also it can only be used in sets.)

def uniAndIntersection(a,b):
    aa = set(a)
    bb = set(b)
    union = aa | bb         # | is operator for union
    intersection = aa & bb  # & is operator for intersection
    return list(union),list(intersection)

print(uniAndIntersection(a,b))
