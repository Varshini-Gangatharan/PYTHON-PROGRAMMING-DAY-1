def max_guest(T, entering, leaving):
    max_guests = 0
    current_guests = 0
    for i in range(T):
        current_guests += entering[i] - leaving[i]
        max_guests = max(max_guests, current_guests)
    return max_guests
T = 5
entering = [7, 0, 5, 1, 3]
leaving = [1, 2, 1, 3, 4]
result = max_guest(T, entering, leaving)
print(result)
