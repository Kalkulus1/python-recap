def calculate_average_and_total(nested_list):
    total = 0
    count = 0

    for item in nested_list:
        if isinstance(item, list):
            sub_total, sub_count = calculate_average_and_total(item)
            total += sub_total
            count += sub_count
        else:
            total += item
            count += 1
    return total, count

    
    

nested_list = [1, 2, [3, 3, [4], 5], 4, 6, 1, 1]
# nested_list = [1, 2, 1, 1]
total, count = calculate_average_and_total(nested_list)

print("Total:", total)
print("Average:", total/count)