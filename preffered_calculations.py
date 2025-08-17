# ---- Functions ----

def odd_numbers_in_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"\nOdd numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

def even_numbers_in_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"\nEven numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

def prime_numbers_in_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"\nPrime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)

def multiply_numbers():
    result = 1
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            result *= number
            print("Current product:", result)
        except ValueError:
            print("Please enter a valid number.")
    print("Final product:", result)


# ---- Menu with while loop ----
while True:
    print("\nChoose an option:")
    print("1. Find odd numbers in range")
    print("2. Find even numbers in range")
    print("3. Find prime numbers in range")
    print("4. Multiply unlimited numbers")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        odd_numbers_in_range()
    elif choice == "2":
        even_numbers_in_range()
    elif choice == "3":
        prime_numbers_in_range()
    elif choice == "4":
        multiply_numbers()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")