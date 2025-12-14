# Problem1

# this is how to print multiple lines of code
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''') 

# Problem2
# write 5 table by using REPL (Read Evaluate Print Loop)
# I did it in command prompt

# Problem3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text for you if you want ")
engine.runAndWait()

# Problem4 
import os

# Specify the directory path you want to list
directory_path = "/windows"

try:
    # os.listdir() returns a list of all entries in the directory
    files_and_folders = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in files_and_folders:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access this directory.")



