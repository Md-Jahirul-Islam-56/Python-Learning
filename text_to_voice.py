import win32com.client 
#import sys
  
# Calling the Dispatch method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

# def multi_line(): #using sys module
#     multi_line_input = sys.stdin.read()
#     return multi_line_input

def multi_line():
    lines = []
    print("(type 'END' on a new line to stop):")

    # Loop to gather multiple lines
    while True:
        line = input()
        if line == "END":  # Custom end signal
            break
        lines.append(line)

    # Join all the lines into a single string
    multi_line_input = "\n".join(lines)
    return multi_line_input


while 1:
    a = input("Press 1 to continue\n")
    if(a == '1'):
        print("Enter the word you want to speak it out by computer") 
        s = multi_line()
        # s = input() 
        speaker.Speak(s)
    else:
        break