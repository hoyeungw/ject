from ject import pipe


def add_one(n): return n + 1


def times_two(n): return n * 2


add_one_then_times_two = pipe(add_one, times_two)

print(add_one_then_times_two(4))  # 10
