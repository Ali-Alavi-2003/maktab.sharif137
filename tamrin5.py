def file_io(input_file= 'input.txt', output_file= 'output.txt'):
    def decorator(func):
        def wrapper(data):
            with open(input_file, 'w') as file:
                file.write(data)
            print(data)

            res = func(data)

            with open(output_file, 'w') as file:
                file.write(res)
            print(output_file)
            return res
        return wrapper
    return decorator


@file_io(input_file='input.txt', output_file='output.txt')
def process_data(data):
    return data.upper()

print(process_data('ali'))