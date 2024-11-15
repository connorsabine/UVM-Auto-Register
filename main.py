from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# inital variables
# user_data_dir = r'C:\Users\conno\AppData\Local\Google\Chrome\User Data' # windows
user_data_dir = r'/Users/connorsabine/Library/Application Support/Google/Chrome' # mac
profile_name = 'Default'
url = 'https://uvm-register-mock.replit.app' # Registrar's website URL
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
crn_string = ""
for crn in crns:
    crn_string += str(crn) + " "
print(crn_string)
print("\n")


# init webdriver with options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_name}")
driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get(url)
    time.sleep(1)
    input_boxes = driver.find_elements(By.TAG_NAME, 'input')
    while len(input_boxes) <= 5:
        time.sleep(1.5)
        print(Fore.YELLOW + "Waiting for reroute to register page...")
        input_boxes = driver.find_elements(By.TAG_NAME, 'input')

    print(Fore.YELLOW + "Registering for classes...")
    print("\n")

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
    print(Fore.GREEN + "Completed Registration...")
    # print(Fore.GREEN + "Press ENTER to Close Browser...")
    # input() # Wait for input to close browser
    print(Fore.GREEN + "Closing Browser...")
    print(Fore.RESET)
    driver.quit()