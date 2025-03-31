from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# SET INFO
production = False
profile_name = 'Default'


# CRNS
if production:
    url = "https://csabine.w3.uvm.edu/"
    crns = []
    while True:
        crn = input("Enter a CRN (or 'done' to finish): ")
        if crn.lower() == 'done':
            break
        if crn.isdigit():
            crns.append(int(crn))
        else:
            print("Invalid CRN. Please enter a numeric value.")
else:
    url = "https://csabine.w3.uvm.edu/"
    crns = [13979, 200, 300, 5006, 7000]


# HEADER
header = """
  _    ___      ____  __           _    _ _______ ____  _____  ______ _____ _____  _____ _______ ______ _____  
 | |  | \ \    / /  \/  |     /\  | |  | |__   __/ __ \|  __ \|  ____/ ____|_   _|/ ____|__   __|  ____|  __ \ 
 | |  | |\ \  / /| \  / |    /  \ | |  | |  | | | |  | | |__) | |__ | |  __  | | | (___    | |  | |__  | |__) |
 | |  | | \ \/ / | |\/| |   / /\ \| |  | |  | | | |  | |  _  /|  __|| | |_ | | |  \___ \   | |  |  __| |  _  / 
 | |__| |  \  /  | |  | |  / ____ \ |__| |  | | | |__| | | \ \| |___| |__| |_| |_ ____) |  | |  | |____| | \ \ 
  \____/    \/   |_|  |_| /_/    \_\____/   |_|  \____/|_|  \_\______\_____|_____|_____/   |_|  |______|_|  \_\                                                                                                             
"""


# PRINT HEADER & CRNS
print(Fore.GREEN + header + "\n")
print(Fore.LIGHTRED_EX + "Class Registration Numbers:")
crn_string = ""
for crn in crns:
    crn_string += str(crn) + " "
print(crn_string)
print("\n")


# INIT WEBDRIVER WITH OPTIONS
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument(f"profile-directory={profile_name}")
driver = webdriver.Chrome(options=chrome_options)


# RUN PROG
try:
    driver.get(url)
    time.sleep(1)
    input_boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='text'][name='CRN_IN']")
    while len(input_boxes) <= 5:
        time.sleep(1.5)
        print(Fore.YELLOW + "Waiting for reroute to register page...")
        input_boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='text'][name='CRN_IN']")

    print(Fore.YELLOW + "Registering for classes...")
    print("\n")

    for i, number in enumerate(crns):
        if i < len(input_boxes):
            input_boxes[i].send_keys(str(number))
        else:
            break

    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='REG_BTN'][value='Submit Changes']")
    submit_button.click()
    
finally:
    print(Fore.GREEN + "Completed Registration...")
    print(Fore.GREEN + "Closing Browser...")
    print(Fore.RESET)
    driver.quit()