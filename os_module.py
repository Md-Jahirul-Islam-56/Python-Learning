
#--------------------------------------------Creating and Renaming a folder-----------------------------------------

# import os

# if not os.path.exists("Folder for OS Module"):
#     os.mkdir("Folder for OS Module") #To create a folder

# for i in range(0, 100):
#     if not os.path.exists(f"Folder for OS Module/Test {i+1}"):
#         os.mkdir(f"Folder for OS Module/Test {i+1}") #100 folders is created inside 
 

# for i in range(0, 100):
#     os.rename(f"Folder for OS Module/Test {i+1}", f"Folder for OS Module/Tutorial {i+1}") #All folders are renamed

#----------------------------------------------To delete file---------------------------------------------

# for i in range(0, 100):
#     os.rmdir(f"Folder for OS Module/Test{i+1}") #to delete empty files

# import shutil

# # Delete a directory and all its contents
# shutil.rmtree("Folder for OS Module")


#---------------------------------------making txt file:----------------------------------------------------

# import os

# # Check if the folder exists, if not, create it
# if not os.path.exists("Folder for OS Module"):
#     os.mkdir("Folder for OS Module")  # To create the main folder

# # Create 100 .txt files named "Test 1.txt" to "Test 100.txt"
# for i in range(0, 100):
#     with open(f"Folder for OS Module/Test {i+1}.txt", 'w') as f:
#         f.write(f"This is Test file {i+1}")

# # Rename the .txt files from "Test X.txt" to "Tutorial X.txt"
# for i in range(0, 100):
#     os.rename(f"Folder for OS Module/Test {i+1}.txt", f"Folder for OS Module/Tutorial {i+1}.txt")


#---------------------------------------To look inside folders-----------------------------------------------

# folders = os.listdir("Folder for OS Module")

# #To change the directory 
# # print(os.getcwd())
# # os.chdir("/Users")
# # print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Folder for OS Module/{folder}"))
    

#--------------------------------------------Opening a file with os module-----------------------------------------

# import os

# # Open the file in read-only mode
# f = os.open(r"D:\Python\Introduction_to_Python\myfile.txt", os.O_RDONLY)

# # Read the contents of the file
# contents = os.read(f, 1024)

# # Decode bytes to string
# decoded_contents = contents.decode('utf-8')

# # Print the decoded contents
# print(decoded_contents)

# # Close the file
# os.close(f)



# import os

# # Open the file in write-only mode
# f = os.open(r"D:\Python\Introduction_to_Python\myfile.txt", os.O_WRONLY)

# # Write to the file
# os.write(f, b"Hello, world!")

# # Close the file
# os.close(f)



# import os

# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']



# import os

# # Run the "dir" command and get the output as a file-like object
# f = os.popen("dir")

# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Close the file-like object
# f.close()