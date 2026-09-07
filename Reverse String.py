def reverse_string(text):
    stack = []
    
    for char in text:
        stack.append(char)
        print(f"Adding '{char}' to stack: {stack}")
        
    print("-" * 15)
    
    reversed_text = ""
    while len(stack) > 0:
        removed_char = stack.pop()
        reversed_text += removed_char
        print(f"Removing '{removed_char}' from stack. Remaining: {stack}")
        
    return reversed_text

word_to_reverse = "Gimi"
final_result = reverse_string(word_to_reverse)

print("-" * 15)
print(f"Original: {word_to_reverse}")
print(f"Reversed: {final_result}")
