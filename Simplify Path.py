def simplify_path(path):
    parts = path.split("/")
    stack = []
    
    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
                print("Popping to go up one directory")
        elif part != "." and part != "":
            stack.append(part)
            print(f"Pushing new directory: {part}")

    return "/" + "/".join(stack)

test_path = "/home/user/../pictures/./"
result = simplify_path(test_path)

print("-" * 20)
print(f"Simplified path: {result}")
