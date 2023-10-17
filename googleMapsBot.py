from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#Class to hold the behaviour of a google maps bot
class googleMapsBrowserBot:

    #Create the browser bot
    def __init__(self,browser):
        self.__browser = browser #Browser to navigate on google maps
        self.__actions = ActionChains(self.__browser) #Action holder for the bot

    #Open the browser on the google maps page
    def open(self,maximize = True):
        self.__browser.get('https://www.google.com/maps')
        if maximize: self.__browser.maximize_window()

    #Closes the browser
    def close(self):
        self.__browser.quit()

    #Search for the given input on the google maps search box
    def search(self,input):
        assert type(input) == str
        search_bar = self.__browser.find_element(By.XPATH, '//*[@id="searchboxinput"]') #Find search box
        search_bar.send_keys(input + Keys.RETURN)

    #Clear search bar after input
    def clear_search(self):
        search_bar = self.__browser.find_element(By.XPATH, '//*[@id="searchboxinput"]') #Find search box
        search_bar.clear()

    #Toggles On and Off the satelite view
    def toggle_satelite_view(self):
        satelite_view = self.__browser.find_element(By.XPATH,'//*[@id="minimap"]/div/div[2]/button') #Find satelite view button
        satelite_view.click()

    #Clicks on option on the menu that appears when the browser hovers over the satellite view
    # 1: Show Relief
    # 2: Show traffic
    # 3: Show Public Transport
    # 4: Show On Bike Route
    # 5: More options
    def option_on_hovered_menu(self,index):
        #Hover satelite view
        satelite_view = self.__browser.find_element(By.XPATH,'//*[@id="minimap"]/div/div[2]/button') #Find satelite view button
        self.__actions.move_to_element(satelite_view).perform() 
        time.sleep(2)

        #Select button positioned at index
        selected_button = self.__browser.find_element(By.XPATH,f'//*[@id="layer-switcher-quick"]/div/div/div/ul/li[{index}]/button')
        selected_button.click()

    #Zoom in on the map
    def zoom_in(self):
        zoom_in_button = self.__browser.find_element(By.XPATH,'//*[@id="widget-zoom-in"]') #Find zoom in button
        zoom_in_button.click()

    #Zoom out on the map
    def zoom_out(self):
        zoom_out_button = self.__browser.find_element(By.XPATH,'//*[@id="widget-zoom-out"]') #Find zoom out button
        zoom_out_button.click()

    #Toggles side bar that appears when a search has been made
    def toggle_side_bar(self):
        #Toggles side bar tab
        side_bar = self.__browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[2]/button')
        side_bar.click()

    #Erases tags on the map
    def erase_tags(self):
        #Click more options on hovered menu
        self.option_on_hovered_menu(5)
        time.sleep(1)

        #Click checkbox to erase tags from the map
        tag_checkbox = self.__browser.find_element(By.XPATH,'//*[@id="layer-switcher"]/div/div/div/div[4]/ul/li[2]/button')
        tag_checkbox.click()
        time.sleep(1)

        #Close the more options menu
        close_button = self.__browser.find_element(By.XPATH,'//*[@id="layer-switcher"]/div/div/div/div[1]/header/button')
        close_button.click()

    #Centers the map by dragging the center to the left (works after a search)
    def center_map(self):
        #Center the image by dragging the map
        maps = self.__browser.find_element(By.XPATH,'//*[@id="scene"]/div[3]')
        #For some reason the first move_by_offset is not done, but if it is not written none of it works
        #TODO: Erase first move_by_offset without breaking the code
        self.__actions.click_and_hold(maps).move_by_offset(150, 100).pause(1).move_by_offset(-250, 0).release()
        self.__actions.perform()

    #Takes screenshot and saves it with the given name
    def take_screenshot(self,image_name):
        self.__browser.save_screenshot(image_name)