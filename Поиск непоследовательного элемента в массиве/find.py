arr = [-1, 0, 2, 3, 4, 5]

indexes = []
for i in range(1, len(arr)):
    if arr[i] > arr[i-1] + 1:
        indexes.append(i)
if not indexes:
    print("Не найдено")
elif len(indexes) == 1:
    print(indexes[0])
else:
    print(indexes)
