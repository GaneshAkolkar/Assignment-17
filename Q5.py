def all_same(items):
    return all(x == items[0] for x in items)

tuple1 = (1, 1, 1, 1)
result = all_same(tuple1)
print(result)
