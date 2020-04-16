def cached(func):
    old_args = {}

    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in old_args:
            old_args[key] = func(*args, **kwargs)
        return old_args[key]

    return wrapper
