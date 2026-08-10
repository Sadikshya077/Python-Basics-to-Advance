from selenium import webdriver
website = ' ' #Fetch URL of website
path = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome()

driver.get(website)


### For clicking in website.
# ------------------------------------------------------------------------------
# click_button = driver.find_element_by_xpath('xpath name ') #Syntax //tag_name [@AttributeName = " Value "]
# click_button.click()
# ------------------------------------------------------------------------------

### Extract Data. [ Tabular ]

# ------------------------------------------------------------------------------
# var1 = driver.find_elements_by_tag_name('tr')

# col1 = [] # initialize list to extract
# col2 = []
# col3 = []

# for var2 in var1 :
#     col_var_1 = var2.find_element_by_xpath('./td[1]').text #Extract first column
#     col1.append(col_var_1)

#     col_var_2 = var2.find_element_by_xpath('./td[2]').text #Extract second column
#     col2.append(col_var_2)

#     col_var_3 = var2.find_element_by_xpath('./td[3]').text #Extract third column
#     col2.append(col_var_3)

#     # print(col_var_1)   # To see the print content
# ------------------------------------------------------------------------------

### Export Data.

# # ------------------------------------------------------------------------------
# import pandas as pd

# df = pd.DataFrame({'pd_col1' : col1, 'pd_col2' : col2,'pd_col3' : col3})
# df.to_csv('Data.csv', index = False)
# # print(df)

driver.quit()