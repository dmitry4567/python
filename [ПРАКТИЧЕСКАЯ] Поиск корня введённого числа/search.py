def find_root(num):
    for i in range(1, num // 2 + 2):
        if i * i == num:
            return i
        elif i * i > num:
            return "Слишком сложно, не могу."

print(find_root(1))