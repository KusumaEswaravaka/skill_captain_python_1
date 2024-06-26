# Define the initial list with some duplicate elements
initial_list = [1, 2, 3, 3, 4, 5]

# Function to convert a list to a set
def list_to_set(input_list):
    return set(input_list)

# Function to convert a set to a list
def set_to_list(input_set):
    return list(input_set)

# Convert the initial list to a set
converted_set = list_to_set(initial_list)
# Convert the set back to a list
converted_list = set_to_list(converted_set)

# Print the results
print(converted_set)
print(converted_list)
