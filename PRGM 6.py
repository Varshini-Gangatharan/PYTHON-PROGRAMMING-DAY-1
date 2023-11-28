def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        current_area = width * h
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
array = [1, 5, 4, 3]
result = max_area(array)
print("Output:", result)
