import pyautogui
import pyperclip
import time

# Click on the icon at (1102, 1048)
pyautogui.click(1102, 1048)
time.sleep(1)  # Wait a second to ensure the click is registered

# Move to the start position (592, 216) and drag to (1835, 896)
pyautogui.moveTo(592, 216)
pyautogui.dragTo(1835, 896, duration=1)  # Dragging duration set to 1 second

# Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1835, 896)
time.sleep(1)  # Wait a moment for the clipboard to be populated

# Get the copied text from the clipboard
copied_text = pyperclip.paste()

print("Copied Text:", copied_text)
