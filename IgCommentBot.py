from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# YOUR USERNAME
name = "angeloyolowlife"

# YOUR PASSWORD
passw = "Eseculitogotmesimping"

# YOUR URL
url = "https://www.instagram.com/p/CqDpQo4piyE/"

# YOUR COMMENT
yourcomment = "hello"

# WAITING TIME (SECONDS) BETWEEN EACH COMMENT
waitingtime = 10

# DEALING WITH COOKIES?
savedcookies = False

# driver config
# if you use a different browser, read the selenium python documentation and change this line
driver = webdriver.Firefox()


def declinecookies():
    #find the decline cookies button
    button_cookie = driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)")
    sleep(1)   

    #click it
    button_cookie.click()
    sleep(2)



def login():
    #enter user name
    driver.find_element(By.NAME, 'username').send_keys(name)
    sleep(0.3)

    #enter password
    driver.find_element(By.NAME, 'password').send_keys(passw)
    sleep(0.3)

    #login!
    boton_login = driver.find_element(By.XPATH, "//button[@type='submit']")
    boton_login.click()

    sleep(2)

def comments():
    # go to the post you want
    driver.get(url)
    sleep(4)

    #find the place to write
    button_write = driver.find_element(By.CSS_SELECTOR, "textarea.x1i0vuye")
    sleep(0.8)

    #write the comment
    button_write.send_keys(yourcomment)
    sleep(0.9)

    # send the comment!
    button_publish = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/section/div/form/div/div[2]/div')
    button_publish.click()

    counter = 1
    textcounter = "Number of comments: " + str(counter)
    print(textcounter)
    i = 1
    
    # infinite loop
    while (True):

        # waiting... }:)
        sleep(waitingtime)

        #find the place to write

        #button_write = driver.find_element(By.XPATH, '//*[@class ="_aidk"]//textarea')
        button_write = driver.find_element(By.CSS_SELECTOR, "textarea.x1i0vuye")
        
        #sleep(0.8)

        #write the comment
        button_write.send_keys(yourcomment)
        sleep(0.9)

        # post again
        button_publish.click()

        counter += 1
        textcounter = "Number of comments: " + str(counter)
        print(textcounter)


def main():
    #go to the instagram login page
    driver.get('https://www.instagram.com/accounts/login/')
    print("instagram login page opened")

    sleep(1)

    #decline cookies?
    if savedcookies == False:
        declinecookies()
        print("cookies declined successfully")
    else:
        print("no cookies to be declined")

    #login
    login()
    print("logged in successfully")

    sleep(5)

    #start to spam!
    print("Starting to comment...")
    comments()

#----------
main()


    

