import mymath as mm

a = mm.basic.square(5)
b = mm.basic.double(10)
c = mm.stats.mean([1, 2, 3, 4, 5])
d = mm.stats.median([1, 2, 3, 4, 5])

print(f"Square of 5: {a}")
print(f"Double of 10: {b}")
print(f"Mean of [1, 2, 3, 4, 5]: {c}")
print(f"Median of [1, 2, 3, 4, 5]: {d}")