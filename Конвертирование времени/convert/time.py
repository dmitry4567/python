seconds = int(input())

hours = seconds // 3600
minutes = (seconds % 3600) // 60

print(str(hours) + " час(а/ов) и " + str(minutes) + " минут(a/ы)")
