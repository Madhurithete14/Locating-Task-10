import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
driver.implicitly_wait(10)

# data
no_of_followers = "166K"
no_of_following = "6"


def get_followers():
    followers = driver.find_element(By.XPATH, "(//button[contains(text(),' followers')]//span)[2]").text
    print('Total Number of followers: ', followers)
    # compare count of xpath followers is equal to no_of_followers given
    assert followers == no_of_followers


def get_following():
    following = driver.find_element(By.XPATH, "(//button[contains(text(),'following')]//span)[2]").text
    print('Total Number of followers: ', following)
    # compare count of xpath followings is equal to no_of_followers given
    assert following == no_of_following


get_followers()
get_following()
time.sleep(5)
driver.close()