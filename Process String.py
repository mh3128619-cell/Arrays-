def processstring(S):
  stack=[]

  for char in S:
    if char!="#":
       stack.append(char)

    elif stack:
      stack.pop()

  return "".join(stack)

def backspacecompare(S,T):
  result_S=processstring(S)
  result_T=processstring(T)

  print(result_S)
  print(result_T)

  return result_S==result_T

word1="ab#c"
word2="ad#c"

if backspacecompare(word1,word2):
  print(True)
else:
    print(False)
