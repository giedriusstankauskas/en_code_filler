from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# IMPORTANT! Enter your EN login details and level number where you want to fill codes
login_name = "your login name"
login_password = "your login password"
lvl_number = 22


def login_to_en(l_name, l_pass):
    login_input = driver.find_element(By.NAME, 'Login')
    password_input = driver.find_element(By.NAME, 'Password')
    sign_in_button = driver.find_element(By.NAME, 'EnButton1')

    login_input.send_keys(l_name)
    password_input.send_keys(l_pass)
    sign_in_button.click()


def press_show_button():
    show_button = driver.find_element(By.XPATH, '//*[@id="AnswersTable_ctl00_lnkShowAnswers"]')
    show_button.click()


def create_word_list(filename):
    list_of_words = []
    with open(filename, "r") as file:
        for line in file.readlines():
            list_of_words.append(line.split("\n")[0])
    return list_of_words


def write_words_to_en(w_list, count, sector_name):
    for word in w_list:
        for i in range(count):
            add_sector_button = driver.find_element(By.ID, 'AnswersTable_ctl00_lnkCreateSector')
            add_sector_button.click()
            sector_name_input = driver.find_element(By.NAME, 'txtSectorName')
            sector_name_input.send_keys(sector_name)
            time.sleep(1)
            sector_name_input.send_keys(Keys.TAB)
            answer_input = driver.switch_to.active_element
            answer_input.send_keys(word)
            answer_input = driver.switch_to.active_element
            answer_input.send_keys(Keys.TAB)
            answer_input = driver.switch_to.active_element
            answer_input.send_keys(Keys.TAB)
            answer_input = driver.switch_to.active_element
            answer_input.send_keys(f"700{word}")
            answer_input.send_keys(Keys.ENTER)
            time.sleep(1)


# These options are for chrome to work in background without opening browser
# chrome_options = Options()
# chrome_options.add_argument("--headless")


# IMPORTANT! Specify chromedriver location on your device
chrome_driver_path = "/Users/username/Development/chromedriver"

s = Service(executable_path=chrome_driver_path)  # add options=chrome_options to work headless
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get(f"https://vilnius.en.cx/Administration/Games/LevelEditor.aspx?gid=73917&level={lvl_number}")

# IMPORTANT!
# if you need to fill codes only once, then leave '1' in write_words_to_en function, else, if you need to fill
# same codes twice or more times, then chane the number accordingly


# Log in to EN
login_to_en(login_name, login_password)

# Find and clicks "Show" button
press_show_button()

# Create code list from file, in this case from 'codes.txt'
word_list = create_word_list("codes.txt")

# Fill codes to EN as many times as indicated
write_words_to_en(word_list, 1, "2")


driver.quit()
