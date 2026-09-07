def singlenumber(nums):
  res = 0
  for num in nums:
    res ^= num
  return res

test = [0, 1, 1, 0, 3]
print(singlenumber(test))
