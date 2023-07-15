def findSubArraysInTheRange(array, min_range, max_range):
    
    subarrays= []
    
    for i in range(min_range, max_range + 1):
        subarrays.append(array[i])

    return subarrays

array=list(map(int,input().split()))
min_range,max_range=map(int,input("Enter ranges: ").split())
print(findSubArraysInTheRange(array, min_range, max_range))