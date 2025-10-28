import numpy as np

# Step 1: Take data input from the user
data = np.array(list(map(int, input("Enter dataset values (space-separated): ").split())))

# Step 2: Display basic details
print("\n--- Data Summary ---")
print("Data:", data)
print("Total elements:", data.size)
print("Shape:", data.shape)

# Step 3: Perform data analysis
print("\n--- Analysis ---")
print("Sum:", np.sum(data))
print("Mean (Average):", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))

# Step 4: Conditional Analysis
print("\n--- Conditional Filters ---")
above_avg = data[data > np.mean(data)]
below_avg = data[data < np.mean(data)]

print("Values above average:", above_avg)
print("Values below average:", below_avg)

# Step 5: Transformation
print("\n--- Data Transformation ---")
print("Squared values:", np.square(data))
print("Normalized data (0-1 range):", (data - np.min(data)) / (np.max(data) - np.min(data)))
