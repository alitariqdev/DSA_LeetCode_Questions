
class Solution:
def removeOuterParentheses(self, s: str) -> str:
  result = []
  stack = []

  for ch in s:
      if len(stack) == 0:
          stack.append(ch)
          continue
      if ch == ")" and len(stack) == 1:
          stack.pop()
          continue
      if ch == ")":
          stack.pop()
          result.append(ch)
      if ch == "(":
          stack.append(ch)
          result.append(ch)
  
  return "".join(result)
      

  
