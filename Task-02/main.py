"""
Task 2
Create a 1000 x 1000 random numpy array.
Measure how long the creation takes.
Convert the array into bytes.
Recreate the array from the bytes.

References: time package, numpy package, np.frombuffer
"""

import numpy as np
import time

# Create a 1000 x 1000 random numpy array
start = time.time()
array = np.random.rand(1000, 1000)
end = time.time()

# Measure how long the creation takes
print(f"Time taken to create the array: {end - start} seconds")

# Convert the array into bytes
bytes_array = array.tobytes()

# Recreate the array from the bytes
recreated_array = np.frombuffer(bytes_array, dtype=array.dtype).reshape(array.shape)

# Check if the recreated array is equal to the original array
print("Original Array == Recreated Array : " + str(np.array_equal(array, recreated_array)))
