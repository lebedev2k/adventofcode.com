def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i
    print(numMap)
        # Find the complement

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []


print(twoSum([3,3], 6))