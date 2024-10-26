#____________________________________NOT FINISHED!! WORKING ON IT!!__________________________________________



# #___________________________________OPENING FROM INSTALLED WHATSAPP_______________________________________

# import pyautogui
# import time
# import os

# # Give yourself time to open WhatsApp desktop and position the window properly
# time.sleep(5)

# # Step 1: Open the WhatsApp window (you may need to adjust this part manually)

# # Path to WhatsApp executable file
# whatsapp_path = "C:\\Users\\YourUsername\\AppData\\Local\\WhatsApp\\WhatsApp.exe"

# # Open WhatsApp Desktop application
# os.startfile(whatsapp_path)

# # Give some time for WhatsApp to open
# time.sleep(5)

# # Step 2: Locate the contact search bar and type the contact's name
# pyautogui.hotkey('ctrl', 'f')  # Opens the search bar
# time.sleep(1)
# contact_name = "Contact Name"
# pyautogui.write(contact_name)
# time.sleep(1)
# pyautogui.press('enter')

# # Step 3: Click the attachment (paperclip) button
# time.sleep(1)
# attach_button_location = pyautogui.locateCenterOnScreen('attach_icon.png')  # Screenshot the attachment button and save it as attach_icon.png
# if attach_button_location:
#     pyautogui.click(attach_button_location)

# # Step 4: Click the 'Document' option (or the file option)
# time.sleep(1)
# document_button_location = pyautogui.locateCenterOnScreen('document_icon.png')  # Screenshot the document button and save it as document_icon.png
# if document_button_location:
#     pyautogui.click(document_button_location)

# # Step 5: Type the file path in the file dialog box
# time.sleep(2)
# file_path = os.path.abspath("path_to_your_file")  # Change to your file path
# pyautogui.write(file_path)
# pyautogui.press('enter')

# # Step 6: Send the file
# time.sleep(2)
# send_button_location = pyautogui.locateCenterOnScreen('send_icon.png')  # Screenshot the send button and save it as send_icon.png
# if send_button_location:
#     pyautogui.click(send_button_location)

# # Done!





# #___________________________________OPENING FROM WEB BROWSER_______________________________________

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import os

# # Path to the operadriver.exe (change this to the correct path)
# opera_driver_path = "C:\\Users\\33152\\OneDrive\\Desktop\\operadriver_win64\\operadriver.exe"  

# # Set the path to the Opera browser launcher
# opera_options = webdriver.ChromeOptions()
# opera_options.binary_location = r"C:\Users\33152\AppData\Local\Programs\Opera GX\opera.exe"  

# # Initialize the Opera WebDriver using OperaDriver
# driver = webdriver.Opera(executable_path=opera_driver_path, options=opera_options)

# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com")

# # Wait for the user to scan the QR code
# input("Press Enter after scanning the QR code...")

# # Find and open the chat of the contact
# contact_name = "Buniya"  # Replace with the contact's name
# search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
# search_box.send_keys(contact_name)
# search_box.send_keys(Keys.ENTER)

# # Locate and click the attachment button (paperclip icon)
# attach_button = driver.find_element(By.XPATH, '//div[@title="Attach"]')
# attach_button.click()

# # Attach and send a file
# file_input = driver.find_element(By.XPATH, '//input[@accept="*"]')
# file_input.send_keys(os.path.abspath(r"D:\Pictures\varsity logo.png"))  # Replace with the file path you want to send

# # Send the file
# time.sleep(2)
# send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
# send_button.click()

# # Close the browser after sending
# time.sleep(5)
# driver.quit()
