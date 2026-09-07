def movezeroes(nums):
  left=0

  for right in range(len(nums)):
    if nums[right] !=0 :
      nums[left], nums[right]=nums[right],nums[left]
      left +=1

  return nums

test=[9,3,1,0,0,1,3,0,5,6,7,0]
print(movezeroes(test))
