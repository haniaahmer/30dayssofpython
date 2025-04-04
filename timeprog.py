import time
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get the current local time
current_time = time.localtime()

# Format time in different styles
time_24hr = time.strftime("%H:%M:%S", current_time)  # 24-hour format
time_12hr = time.strftime("%I:%M:%S %p", current_time)  # 12-hour format with AM/PM
date_today = time.strftime("%A, %B %d, %Y", current_time)  # Example: Monday, February 26, 2025

# Determine greeting based on hour
hour = current_time.tm_hour

if 5 <= hour < 12:
    greeting = "Good Morning!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon!"
elif 18 <= hour < 22:
    greeting = "Good Evening!"
else:
    greeting = "Good Night!"

# Speak the greeting
engine.say(greeting)

# Run the speech engine
engine.runAndWait()

# Print the formatted time and greeting
print(f"{greeting}\nCurrent Time (24-hour format): {time_24hr}\nCurrent Time (12-hour format): {time_12hr}\nDate & Time: {date_today}")
