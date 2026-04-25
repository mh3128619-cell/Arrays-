def findmajor(numd):
  count={}
  n = len(numd) 
  for num in numd: 
    count[num]=1+count.get(num,0) 

    if count[num]>n//2:
      return num

  return -1

my_nums=[1,1,1,1,1,2,3,3,3,33,3,3,3,3,3,3]
print(findmajor(my_nums))
