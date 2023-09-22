def display_multiples(n):
    for i in range(2, n // 2 + 1):
        multiples = []
        for j in range(n - 1, 1, -1):
            if j % i == 0:
                multiples.append(j)
            if j <= i:
                break
        multiples.sort(reverse=True)
        print(f"Multiples of {i} less than {n}: {multiples}")

try:
    n = int(input("Enter an integer 'n': "))
    if n < 2:
        print("Please enter a positive integer greater than or equal to 2.")
    else:
        display_multiples(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


