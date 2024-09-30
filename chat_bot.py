import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
  api_key="Enter your API key",
)

def is_last_message_from_sender(chat_log, sender_name="Navdha"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Click on the chrome icon at coordinates (1102, 1048)
pyautogui.click(1102, 1048)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (592, 216) to (1835, 896) to select the text
    #pyautogui.click(614, 423, button='left')
    pyautogui.moveTo(611, 225)
    pyautogui.dragTo(1835, 896, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1835, 896)
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1835, 896)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Eish who speaks hindi as well as english. You are from India and you are a B.tech Student. You need to analyze chat history and give Output as the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1111, 959)
        pyautogui.click(1111, 959)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')