a = {'a', 'b'}
b = {'b', 'c'}

print(set(a - b).union(set(b - a)))