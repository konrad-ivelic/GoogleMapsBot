from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from PIL import Image
import time
import sys

#Recover coordinates file from command window
coordinates_file = sys.argv[1]

#Browser on Google Chrome
browser = webdriver.Chrome()

#Open the google maps page
url = 'https://www.google.com/maps'
browser.get(url)
browser.maximize_window() #Maximize window to full size
time.sleep(2)

#Find elements
search_bar = browser.find_element(By.NAME, 'q')  
satelite_view = browser.find_element(By.XPATH,'//*[@id="minimap"]/div/div[2]/button')
zoom_in = browser.find_element(By.XPATH,'//*[@id="widget-zoom-in"]')

#Turn on satelite_view
satelite_view.click()

#Actions for the browser to perform
actions = ActionChains(browser)

#Go over all the coordinates in the file and take a screenshot for each of them
counter = 1
with open(coordinates_file,"r") as file:
    #For each coordinate in the file
    for line in file.readlines():

        #Search coordinates
        coordinates = line[:-1]
        search_bar.send_keys(coordinates + Keys.RETURN)
        time.sleep(2)

        #Zoom thrice
        zoom_in.click()
        time.sleep(1)
        zoom_in.click()
        time.sleep(1)
        zoom_in.click()
        time.sleep(1)

        #Close side bar tab
        side_bar = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[2]/button')
        side_bar.click()
        time.sleep(1)

        #Hover satelite view
        actions.move_to_element(satelite_view)
        actions.perform()
        time.sleep(2)

        #Click more button to get more options
        more_button = browser.find_element(By.XPATH,'//*[@id="layer-switcher-quick"]/div/div/div/ul/li[5]/button')
        more_button.click()
        time.sleep(1)

        #Click checkbox to erase tags from the map
        tag_checkbox = browser.find_element(By.XPATH,'//*[@id="layer-switcher"]/div/div/div/div[4]/ul/li[2]/button')
        tag_checkbox.click()
        time.sleep(1)

        #Close the hovered window
        close_button = browser.find_element(By.XPATH,'//*[@id="layer-switcher"]/div/div/div/div[1]/header/button')
        close_button.click()
        time.sleep(1)

        #Center the image by dragging the map
        maps = browser.find_element(By.XPATH,'//*[@id="scene"]/div[3]')
        #For some reason the first move_by_offset is not done, but if it is not written none of it works
        #TODO: Erase first move_by_offset without breaking the code
        actions.click_and_hold(maps).move_by_offset(150, 100).pause(1).move_by_offset(-250, 0).release()
        actions.perform()

        #Take and save screenshot
        image_name = f"image{counter}.png"
        browser.save_screenshot(image_name)

        #Open side bar again to do a new search
        side_bar.click()
        time.sleep(1)

        #Clear text box and add 1 to the counter
        search_bar.clear()
        counter += 1

#Close the browser
browser.quit()