def get_top_k_elements(nums, k):
    count_map = {}
    
    for n in nums:
        count_map[n] = count_map.get(n, 0) + 1
        
    print(f"1. Hash Table (Number : Frequency): {count_map}")

    sorted_elements = sorted(count_map.keys(), key=lambda x: count_map[x], reverse=True)
    
    print(f"2. Elements after sorting from most to least frequent: {sorted_elements}")

    result = sorted_elements[:k]
    return result

my_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k_value = 2

final_result = get_top_k_elements(my_list, k_value)

print("-" * 30)
print(f"✅ The top {k_value} most frequent elements are: {final_result}")
