def calculate_average(numbers):
    if not numbers:
        return None  # Return None to indicate no numbers
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#Example usage without potential error:
my_list = [10,20,30,40,50]
average = calculate_average(my_list)
print(f"The average is: {average}")
