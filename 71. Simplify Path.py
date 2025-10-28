class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        my_list = path.split("/")

        for i in my_list:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        result = "/" +  "/".join(stack)
        return result
        
