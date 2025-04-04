import pyttsx3
engine = pyttsx3.init()
name=input("Enter your name: ")
print("good morning",name)
print(f"good morning {name}")
engine.say(f"good morning{name}!")
engine.runAndWait()