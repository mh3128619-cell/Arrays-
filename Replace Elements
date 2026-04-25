def replaceElements(arr):
  max_right = -1
  for i in range(len(arr) - 1, -1, -1):
    current_value = arr[i]
    arr[i] = max_right
    if current_value > max_right:
      max_right = current_value
  return arr


print(replaceElements([17,18,5,4,6,1]))
