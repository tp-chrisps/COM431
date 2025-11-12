import math
data = [i*i for i in range(101)]
print(data)
def binarysearch(list, item):
    low = 0
    high = len(list)
    exists = True
    mid = math.floor((low + high) // 2)
    while list[mid] != item and exists:
        if item < list[mid]:
            high = mid - 1
            print(f"low {high}")
        else:
            low = mid + 1
            print(f"high {low}")
        if high < low:
            exists = False
        mid = math.floor((low + high) // 2)
    if exists:
        print(f"Found {item} at index {mid}")
    else:
        print(f"{item} not found")

num = int(input("Enter a number: "))
binarysearch(data, num)