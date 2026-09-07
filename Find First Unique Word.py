def find_first_unique(word):
    count_table = {}
    
    for char in word:
        if char in count_table:
            count_table[char] += 1
        else:
            count_table[char] = 1
            
    print(f"Hash Table after counting: {count_table}")
    
    for char in word:
        if count_table[char] == 1:
            return char 
            
    return None 

my_word = "leelcode"
result = find_first_unique(my_word)

if result:
    print(f"✅ The first unique character in '{my_word}' is: {result}")
else:
    print("❌ No unique characters found in this word.")
