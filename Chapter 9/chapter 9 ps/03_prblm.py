import os

def generate_multiplication_tables():
    # Define the directory where tables will be stored
    folder_path = "Chapter 9/chapter 9 ps/tables"
    
    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Generate tables from 2 to 20
    for i in range(2, 21):
        file_path = os.path.join(folder_path, f"table_{i}.txt")
        with open(file_path, "w") as f:
            for j in range(1, 11):
                f.write(f"{i} x {j} = {i * j}\n")

    print("Multiplication tables from 2 to 20 have been generated and saved to individual files.")

# Call the function
generate_multiplication_tables()
