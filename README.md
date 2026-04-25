# Arrays-
def two_sum_optimized(nums, target):
    seen = {}  # (Dictionary)

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return "Not Found"
print(two_sum_optimized([2, 11, 15, 7], 9))
