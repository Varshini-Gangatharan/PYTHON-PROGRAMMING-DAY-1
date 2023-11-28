def modify_string(s):
    result = ""
    for char in s:
        frequency = s.count(char)
        distance = (ord(char) - ord('a') + frequency) % 26
        modified_char = chr(ord('a') + distance)
        result += modified_char
    return result
input_string = "ghee"
output_string = modify_string(input_string)
print(output_string)  
