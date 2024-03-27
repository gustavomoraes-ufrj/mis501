numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 0:
        print("Zero encountered, breaking loop")
        break
else:
    print("No zeros encountered in the list")


num = 0
while num < 5:
    print(num)
    num += 1
else:
    print("Loop completed without hitting break")


num = 131
for i in range(2, num/2):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
