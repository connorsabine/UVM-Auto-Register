from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# inital variables
user_data_dir = r'C:\Users\conno\AppData\Local\Google\Chrome\User Data'
profile_name = 'Default'
url = 'https://ba006969-6d09-499e-bfc6-18961c9254fa-00-36ovu8c3ldxon.picard.replit.dev/' # Registrar's website URL
crns = [11597,10639,10100,11941,12940] # CRNs to enter into the form


# header
header = """
  _    ___      ____  __           _    _ _______ ____  _____  ______ _____ _____  _____ _______ ______ _____  
 | |  | \ \    / /  \/  |     /\  | |  | |__   __/ __ \|  __ \|  ____/ ____|_   _|/ ____|__   __|  ____|  __ \ 
 | |  | |\ \  / /| \  / |    /  \ | |  | |  | | | |  | | |__) | |__ | |  __  | | | (___    | |  | |__  | |__) |
 | |  | | \ \/ / | |\/| |   / /\ \| |  | |  | | | |  | |  _  /|  __|| | |_ | | |  \___ \   | |  |  __| |  _  / 
 | |__| |  \  /  | |  | |  / ____ \ |__| |  | | | |__| | | \ \| |___| |__| |_| |_ ____) |  | |  | |____| | \ \ 
  \____/    \/   |_|  |_| /_/    \_\____/   |_|  \____/|_|  \_\______\_____|_____|_____/   |_|  |______|_|  \_\                                                                                                             
"""


# print header
print(Fore.GREEN + header + "\n")
print(Fore.LIGHTRED_EX + "Class Registration Numbers:")
for i, crn in enumerate(crns):
    print(Fore.LIGHTRED_EX + "CRN", i+1, ":", crn)


# init webdriver with options
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_name}")
driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get(url)
    time.sleep(1)
    input_boxes = driver.find_elements(By.TAG_NAME, 'input')

    print(Fore.YELLOW + "Registering for classes...")

    # iter through crns and input into form
    for i, number in enumerate(crns):
        if i < len(input_boxes):
            input_boxes[i].send_keys(str(number))
        else:
            break

    # submit form
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()
    
finally:
    print(Fore.GREEN + "Completed Registration.")
    print(Fore.RESET)
    driver.quit()