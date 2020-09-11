largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n = int(num)
        if smallest is None or n < smallest:
            smallest = n
        elif largest is None or n > largest:
            largest = n

    except:
        print("Invalid input")
        continue

print("Maximum", largest)
print("Minimum", smallest)
