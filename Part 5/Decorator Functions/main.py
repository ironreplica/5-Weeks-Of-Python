# Learning about decorator functions
# Trevor childs 7/30/2024

def repeat(num_repeat):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for i in range(num_repeat):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat
@repeat(num_repeat=10)
def stutter(name):
    print(f'Hello {name}.')

stutter("Trevor")