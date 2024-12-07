def function_with_uncommon_error_solution(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return float('inf')  # Return infinity or another appropriate value

result = function_with_uncommon_error_solution(0)
print(result)  # Output: inf