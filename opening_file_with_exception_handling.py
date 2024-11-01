### opening file with exception handling 

try:
    file = open('example.txt','r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file is not found")
except Exception as e:
    print(e)

finally:
    if 'file' in locals() and (not file.close()):
        file.close()
        print('File closed')


### opening file with with

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
