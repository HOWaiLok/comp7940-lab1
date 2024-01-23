x = 52633
factors = []
for i in range(1, x):
    if x % i == 0:
        factors.append(i)
print(f"The factors for {x} is {factors}")

def print_factor(x):
    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)
    print(f"The factors for {x} is {factors}")

print_factor(52633)


def find_factor(x):
    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)
    return factors

l = [52633, 8137, 1024, 999]
result = []
for i in l:
    result.extend(find_factor(i))
result = list(set(result))
result.sort()
print("The factors are", result)
