import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By  # Add this import
import time
def read():
    a=open("credentials.txt","r")
    credentials_list=a.readlines()
    return credentials_list
def automator():
    x=read()
    driver = webdriver.Safari()#change it to chrome or some other browser while running on windows or linux
    #fix required here
    driver.get("http://192.168.254.1:8090/httpclient.html")
    username=x[0]
    password=x[1]
    time.sleep(0.5)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(0.5)

automator()
