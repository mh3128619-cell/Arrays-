def isanagram(s,t):
  if len(s)!=len(t):
    return False

  countS,countT={},{}

  for i in range(len(s)) :
    countS[s[i]]=1+countS.get(s[i],0)
    countT[t[i]]=1+countT.get(t[i],0)

  return countS == countT

print("is anagram(anagram,nagram):")
print(isanagram("anagram","nagram"))
print("is anagram(rat,car):")
print(isanagram("rat","car"))
