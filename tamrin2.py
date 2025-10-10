def convert_to_string(func):
    def wrapper(input_value):
        strint_value = str(input_value)
        print(f'{strint_value} : {type(strint_value)}')
        return func(strint_value)

    return wrapper


def print_input_lengths(func):
    def wrapper(input_value):
        string_length = len(str(input_value))
        print(f'len: {string_length}')
        return func(input_value)

    return wrapper


@convert_to_string
@print_input_lengths
def process_data(value):
    return value


print(process_data(['ali', 5, True]))
