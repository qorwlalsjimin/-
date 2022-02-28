목록 = [1, 52, 273, 32, 99, 101]
max = 목록[0]
min = 목록[0]

for i in 목록:
    if i < min :
        min = i
    if i > max:
        max = i

print(max)
print(min)