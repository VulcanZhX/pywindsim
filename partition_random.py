import numpy as np

def generate_random_int_array(total_sum, size):
    # Generate random integers
    random_array = np.random.randint(1, total_sum, size=size)
    
    # Scale the array to sum to the desired total_sum
    scaled_array = np.floor(random_array / np.sum(random_array) * total_sum).astype(int)
    
    # Adjust the array to ensure the sum is exactly total_sum
    difference = total_sum - np.sum(scaled_array)
    for i in range(difference):
        scaled_array[i % size] += 1
    
    return scaled_array

# Example usage
total_sum = 100
size = 10
random_int_array = generate_random_int_array(total_sum, size)

print(random_int_array)
print("Sum of elements:", np.sum(random_int_array))