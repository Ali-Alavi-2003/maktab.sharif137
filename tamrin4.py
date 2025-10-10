def nested_sum(my_list):
    sum_list = 0

    for i in my_list:
        if isinstance(i, list):
            sum_list += nested_sum(i)
        else:
            sum_list += i
    return sum_list

print(nested_sum([1, [2, 3], [4, 5]]))