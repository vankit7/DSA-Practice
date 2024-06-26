import os
import sys
output_dir = '/home/ankit/Documents/python/test/'
output_file = 'output.txt'
input_file = 'input.txt'
output_path = os.path.join(output_dir, output_file)
input_path = os.path.join(output_dir, input_file)

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Redirect stdout to the file
sys.stdout = open(output_path, 'w')
sys.stdin = open(input_path, 'r')

age = int(input("Enter your age: \n"))

# Check if the user is an adult and print the appropriate message
if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")