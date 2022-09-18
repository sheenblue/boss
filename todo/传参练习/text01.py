def func_a(func, *args, **kwargs):
    print(func(*args, **kwargs))
    print(*args, **kwargs)


def func_b(*args):
    return args


if __name__ == '__main__':
    func_a(func_b, 'a', 2,'b')