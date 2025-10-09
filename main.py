from datetime import datetime
hour = datetime.now().hour


def restrict_hours(start=0, end=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if start <= hour < end:
                print('OK')
                return func(*args, **kwargs)
            else:
                print('wrong')
                return None

        return wrapper

    return decorator


@restrict_hours(start=9, end=17)
def do_work():
    return do_work

do_work()