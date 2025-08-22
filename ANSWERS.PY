try:
    # Open the file for reading
    with open("input.txt", "r") as file:
        data = file.read()

    # Count words
    word_count = len(data.split())

    # Convert to uppercase
    modified_data = data.upper()

    # Write to a new file
    with open("output.txt", "w") as file:
        file.write("=== PROCESSED TEXT ===\n")
        file.write(modified_data + "\n\n")
        file.write(f"Word Count: {word_count}\n")

    print("Success! 'output.txt' created.")

except Exception as e:
    print(f"Error: {e}")



# Error Handling Lab


try:
    # Ask the user for a filename
    filename = input("\nEnter the filename to process: ")

    with open(filename, "r") as file:
        data = file.read()

    word_count = len(data.split())
    modified_data = data.upper()

    new_file = "modified_" + filename
    with open(new_file, "w") as file:
        file.write("=== PROCESSED TEXT ===\n")
        file.write(modified_data + "\n\n")
        file.write(f"Word Count: {word_count}\n")

    print(f"Success! '{new_file}' created.")

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"Unexpected error: {e}")