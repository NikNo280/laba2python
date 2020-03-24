def cached(func):
    old_args = [None, None]
    def wrapper(*args, **kwargs):
        if(old_args[0] == args):
            return old_args[1]
        else:
            old_args.clear()
            old_args.append(args)
            old_args.append(func(*args, **kwargs))
            return old_args[1]
    return wrapper

@cached
def add(a, b):
     return  a + b

