global_var = 10
def increment_local_var():
    local_var = 5
    return local_var + 1

print(increment_local_var())  # Output: 6
print(global_var)             # Output: 10