# keywords: HTML (DOM),
#   locator: xpath(querying), cssSelector(querying) can be customized using tags and attributes
#   locators on html: id, name, link_name, partial_link_name, class_name



# Google search scenario:
# 1. Open the browser, launch the website google.com (Given condition in Gherkin scenario)
# 2. type 'selenium python' in the search and hit Enter (Actions - When)
# 3. Verify the result is more 20 mln (Test here, check point - Then)
# 4. Verify that it take less than a second for the search (Test here, check point - Then)
# 5. close the browser


import time

from selenium.webdriver.common.keys import Keys

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print('Open the browser and google website')
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
print("identifying google search box")
time.sleep(3)

search_text_box.clear()
search_text_box.send_keys("selenium python")
print("cleared the search box then typed 'python selenium' in the search box.")
time.sleep(3)

search_text_box.send_keys(Keys.RETURN)
print("hit the enter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)
# "About 26,500,000 results (0.53 seconds)"
# verify the result num > 20 mil
result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',','')
result_num = int(result_num_str)
assert result_num > 20000000,"Result num less than 20 mln"
print("Verifying result number passed")


# Verifying the performance if it is less than a second
result_time_str = result_msg_list[3]
result_time_str = result_msg_list[3].replace('(','')
result_time = float(result_time_str)
assert result_time < 1,"it took more than a second"
print("Verifying the time of performance Passed")


print("Now closing the browser.")
driver.close()


