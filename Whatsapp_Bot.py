#import
from selenium import webdriver

#connect
driver = webdriver.Chrome(r'')
driver.get('https://web.whatsapp.com/')

#users
names = input('enter the names with comma(,): ')
lst = names.split(',')
names = list(lst)

msg = input('enter msg: ')
count = int(input('How many times: '))
input('enter anykey...')

# (for loop) for users and work
for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    send_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        send_box.send_keys(msg)
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        button.click()
#end