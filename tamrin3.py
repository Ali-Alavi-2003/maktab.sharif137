def comparison(value: list):
    value_dict = {}
    for i in value:
        if i in value_dict:
            value_dict[i] += 1
        else:
            value_dict[i] = 1
    max_item = ""
    max_count = 0
    for item , count in value_dict.items():
        if count > max_count:
            max_count = count
            max_item = item
    print(f'max item: {max_item} \n and max count: {max_count}')

comparison(['ali', 'ali', 'reza', 'hossein'])