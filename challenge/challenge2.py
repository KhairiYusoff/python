def reverse_string(s):
    # Extract non-space characters and reverse them
    reversed_chars = [char for char in s if char != ' '][::-1]
    
    # Initialize an empty list to build the result
    result = []
    
    # Counter for the reversed_chars list
    j = 0
    
    # Iterate through the original string
    for char in s:
        if char == ' ':
            # If the current character is a space, add it to the result
            result.append(' ')
        else:
            # Otherwise, add the next character from reversed_chars
            result.append(reversed_chars[j])
            j += 1
    
    # Join the result list into a string and return it
    return ''.join(result)

# Test the function
test_string = "hello world"
print(reverse_string(test_string))  # Expected output: "dlrow olleh"
