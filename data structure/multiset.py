def majorityElement(nums: list[int]) -> int:
    majors = {}
    for num in nums:
        if num not in majors:
            majors[num] = 0
        majors[num] += 1

    major_count = 0
    for key in majors:
        if majors[key] > major_count:
            major_count = majors[key]
            result = key
    
    return result

nums = [2,5,5,5,5,6,3,5,3,2,6,6,7,4,8,5,5,5,2,1,1,1,2,2]
print(majorityElement(nums))