import win32com.client

# Initialize the speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# List the available voices
voices = speaker.GetVoices()

print("Available voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")

# Select a specific voice by index
# Example: Select the second available voice (index 1)
voice_index = 1
speaker.Voice = voices.Item(voice_index)

g = "good night"
# Speak using the selected voice
speaker.Speak("This is for you...")

for i in range(10):

    speaker.Speak(f" {g}")
