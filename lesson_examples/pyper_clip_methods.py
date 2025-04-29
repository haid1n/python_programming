# importing the library 
import pyperclip as pc 
  
text1 = "GeeksforGeeks"
  
# copying text to clipboard 
pc.copy(text1) 
  
# pasting the text from clipboard 
text2 = pc.paste() 
  
print(text2) 