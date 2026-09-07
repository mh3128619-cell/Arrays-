def removeduplicates(text):
  stack=[]
  for char in text:
    if stack and stack[-1]==char :
      print(stack[-1])
      stack.pop()

    else :
      stack.append(char)
  return "".join(stack)

word="abbaca"
result=removeduplicates(word)
print(result)
