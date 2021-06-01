from webdriver_functions_mine import *

# launch_website('https://courses.letskodeit.com/practice')
launch_website('http://automationpractice.com/index.php')
woman_tab = "//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/a[1]"
click_element_by_xpath(woman_tab)
go_back_to_previous_page()
refresh_browser()
go_next_page()
close_browser()

