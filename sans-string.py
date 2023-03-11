import re
import tkinter as tk
from tkinter import filedialog

# prompt the user to select a file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title='Select Transcript File')
if not file_path:
    print('File selection cancelled.')
    exit()

# read the transcript file
with open(file_path, 'r') as file:
    transcript = file.readlines()

# prompt the user for the text string to remove
root.withdraw()
remove_string = tk.simpledialog.askstring('Remove String', 'Enter the text string to remove:')
if not remove_string:
    print('Text string selection cancelled.')
    exit()

# remove any line that contains the specified text string and add a blank line
transcript_without_string = []
for line in transcript:
    if remove_string not in line:
        transcript_without_string.append(line)
    else:
        transcript_without_string.append('\n')

# prompt the user to select a save location and filename
root.withdraw()
file_types = [('Text files', '*.txt'), ('All files', '*.*')]
save_path = filedialog.asksaveasfilename(title='Save Transcription Without String', defaultextension='.txt', filetypes=file_types)
if not save_path:
    print('Save location selection cancelled.')
    exit()

# write the transcript without the specified text string to a new file
with open(save_path, 'w') as file:
    file.writelines(transcript_without_string)
