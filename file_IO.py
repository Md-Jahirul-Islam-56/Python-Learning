# # READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# # WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

# #more efficient method and does the closing automatically:
# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside the text file")

# readlines() method:
#The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# writelines() method:
#The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# # Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately
# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()

with open('myfile.txt', 'r+') as f:
  # Move to the 3rd byte in the file
  f.seek(3)

   # Save the current position
  current_position = f.tell()
  print(current_position)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)

  #To  cut the file down to just 5 bytes
  f.truncate(5)
    

with open('myfile.txt', 'r') as f:
  print(f.read())