def check_brackets(text):
    bag = []
    print(f"--- Checking string: {text} ---")
    
    for c in text:
        if c == "(":
            bag.append(c)
            print(f"Found '(', pushing to stack. Stack: {bag}")
        elif c == ")":
            if len(bag) == 0:
                print("Found ')' but stack is empty! Mismatch.")
                return False
            bag.pop()
            print(f"Found ')', popping from stack. Stack: {bag}")
            
    if len(bag) == 0:
        print("Stack is empty, all brackets matched!")
        return True
    else:
        print(f"Stack not empty: {bag}... Mismatch!")
        return False

print(check_brackets("(())"))
print("\n" + "="*30 + "\n")
print(check_brackets("(()"))
print("\n" + "="*30 + "\n")
print(check_brackets(")("))
print("\n" + "="*30 + "\n")
print(check_brackets("()("))
