def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num  

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i

numbers = [2, 11, 7, 15]
target_sum = 9
result = two_sum(numbers, target_sum)

print(f"Indices: {result}")  # Expected output: [0, 2]
