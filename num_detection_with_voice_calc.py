import speech_recognition as sr
import re
import win32com.client
from functools import reduce
import time

# Initialize the speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()

# Initialize the recognizer
r = sr.Recognizer()

# Function to extract numbers from text
def extract_numbers(text):
    # if text == "decimal":

    # Find all sequences of digits in the text
    numbers = re.findall(r'\d+', text)
    # Convert the list of string digits to integers
    return list(map(int, numbers))

# Function to extract operations from text
def extract_operations(text):
    # Normalize the text to lowercase
    text = text.lower()

    # Check for specific operation keywords
    if any(word in text for word in ["add", "addition", "plus"]):
        return "add"
    elif any(word in text for word in ["sub", "subtract", "subtraction", "minus"]):
        return "sub"
    elif any(word in text for word in ["multiply","into","multiplication"]):
        return "mult"
    elif any(word in text for word in ["divide","division"]):
        return "div"
    else:
        return None

# Main function to process speech input
def listen_for_numbers():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        speaker.speak("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=0.5)

        print("Say...\n1. Add/Addition/Plus for Addition\n2. sub/subtract/subtraction/minus for Subtraction\n3. multiply/into/multiplication for multiplication\n4. Divide/division for division\n\t\t....with two numbers with it.")
       # speaker.speak("Say...Add or Addition or Plus for Addition and sub or subtract or subtraction or minus for Subtraction  and multiply or into or multiplication for multiplication and Divide or division for division and two numbers with it.")
        time.sleep(5)
        print("Listening for numbers and operations...")
        # Capture the speech
        my_audio = r.listen(source)
        
        try:
            # Convert speech to text using Google Web Speech API
            speech_text = r.recognize_google(my_audio)
            print(speech_text)
            print(f"Recognized Text: {speech_text}")
            speaker.speak(f"Recognized Text: {speech_text}")
            
            # Extract numbers and operations from the recognized text
            numbers = extract_numbers(speech_text)
            operation = extract_operations(speech_text)
            
            if numbers and operation:
                if operation == "add":
                    result = reduce(lambda x, y: x + y, numbers)
                    print(f"Sum of the numbers: {result}")
                    speaker.speak(f"The sum of the numbers is {result}")

                elif operation == "sub":
                    result = reduce(lambda x, y: x - y, numbers)
                    print(f"Subtraction of the numbers: {result}")
                    speaker.speak(f"The result of subtracting the numbers is {result}")

                elif operation == "mult":
                    result = reduce(lambda x, y: x * y, numbers)
                    print(f"Multiplication of the numbers: {result}")
                    speaker.speak(f"The result of multiplication of the numbers is {result}")
                
                elif operation == "div":
                    result = reduce(lambda x, y: x / y, numbers)
                    print(f"Division of the numbers: {result}")
                    speaker.speak(f"The result of division of the numbers is {result}")
            else:
                if not numbers:
                    print("No numbers found.")
                    speaker.speak("No numbers found in your speech.")
                if not operation:
                    print("No valid operation found.")
                    speaker.speak("No valid operation found in your speech.")
        
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            speaker.speak("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speaker.speak("Could not request results from Google Speech Recognition service")

if __name__ == "__main__":

        voice_input = input("For Male voice: press 1\nFor Female voice: press 2\n")
        if voice_input == "1":
            speaker.Voice = voices.Item(0)
        if voice_input == "2":
            speaker.Voice = voices.Item(1)
    
        while True:

            user_input = input("\nPress e for exit...\n")

            if user_input == "e" or user_input == "E":
                break

            else:
                print("Welcome to Voice Calculator...")
                speaker.speak("Welcome to Voice Calculator")

                listen_for_numbers()

                print("Thanks for using the voice calculator.")
                speaker.speak("Thanks for using the voice calculator")
                
    