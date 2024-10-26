import speech_recognition as sr
import win32com.client
#import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
# def SpeakText(command): #using pyttsx3 module
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command) 
#     engine.runAndWait()

def SpeakText(command):#using win32com.client module
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    speaker.Speak(command)    

# Loop infinitely for the user to speak
while True: 
    a = input("Press 1 to continue\n")
    if(a == '1'):   
        try:
            # Use the microphone as source for input.
            with sr.Microphone() as source2:
                # Adjust the recognizer sensitivity to ambient noise
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Say something...")
                
                # Listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using Google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say:", MyText)
                SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown error occurred")
    else:
        break
