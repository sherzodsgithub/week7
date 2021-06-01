from webdriver_functions_mine import *

# launch_website('https://courses.letskodeit.com/practice')


# scenario for go back, forward, refresh
#
# launch_website('http://automationpractice.com/index.php')
# woman_tab = "//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/a[1]"
# click_element_by_xpath(woman_tab)
# go_back_to_previous_page()
# refresh_browser()
# go_next_page()
# close_browser()

 # *********** Scenario: Login to "http://automationpractice.com/index.php"
# web_url = "http://automationpractice.com/index.php"
# username = "haha@email.com"
# pswd = "manaman"

# identify all locators(xpath, optional: id, css selector):
sign_in_link = "//a[contains(text(),'Sign in')]"
# sign_in_link = "//a[contains(text(),'Sign in')" >>>to see if try/except block working
email_input = "//input[@id='email']"
password_input = "//input[@id='passwd']"
sign_in_button = "//button[@id='SubmitLogin']"
sign_out_link = "//header/div[2]/div[1]/div[1]/nav[1]/div[2]/a[1]"

# steps:
launch_website('http://automationpractice.com/index.php')
click_element_by_xpath(sign_in_link)
time.sleep(2)
enter_text_by_xpath(email_input,"haha@email.com")
enter_text_by_xpath(password_input,"manaman")
click_element_by_xpath(sign_in_button)
time.sleep(10)
print("Successfully signed in")
print("Signing out now...")
click_element_by_xpath(sign_out_link)
close_browser()
