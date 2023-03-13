# 2570. Merge Two 2D Arrays by Summing Values
# Oleg Belov
def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    ids = {}
    arr = nums1 + nums2
    for num in arr:
        if num[0] not in ids.keys():
            ids[num[0]] = num[1]
        else:
            ids[num[0]] = ids.get(num[0]) + num[1]

    result = []
    [result.append([id, ids[id]]) for id in ids]
    result.sort()
    return result



nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]

print(mergeArrays(nums1, nums2))

