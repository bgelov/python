# merge 2d arrays and sum value by id

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = nums1 + nums2
        arr.sort()
        resultArr = []
        ids = [arr[i][0] for i in range(len(arr))]
        ids = list(map(int, set(ids)))
        ids.sort()
        for id in ids:
            sum = 0
            for a in arr:
                if a[0] == id:
                    sum += a[1]
            resultArr.append([id,sum])
        return resultArr
