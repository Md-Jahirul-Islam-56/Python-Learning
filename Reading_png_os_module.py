import os

# Specify the directory where you want to search for PNG files
directory = r'D:\Python\PNG_Test'


counter = 1

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with a '.png' extension
    if filename.endswith('.png'):
        # Create a new name for the file
        new_name = f'i_{counter}.png'

        print(filename)
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        print(old_file)
        new_file = os.path.join(directory, new_name)
        print(new_file)
        
        # Rename the file
        os.rename(old_file, new_file)
        
        print(f"Renamed: {filename} to {new_name}")
        counter += 1
   

# for filename in os.listdir(directory):
#     if filename.endswith('.png'):
#         print(f"PNG file found: {filename}")