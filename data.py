from selenium import webdriver
from bs4 import BeautifulSoup
import time
import math

def get_data():
    
    opts = FirefoxOptions()
    opts.add_argument('--headless')
    wd = webdriver.Firefox(firefox_options=opts)
    wd.get('https://axie.live')
    html = wd.find_element_by_tag_name('html').get_attribute('innerHTML')
    # wd.quit()

    # # print(html)
    soup = BeautifulSoup(html, features="lxml")

    data = soup.find_all('span', {'class':'flex'})

    # data = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,]
    final_list = [data[i:i+4] for i in range(0,len(data), 4)]

    titles = ['Ronin Transactions', 'Deposit ETH', 'Withdraw ETH', 'Deposit AXS', 'Withdraw AXS', 'Deposit SLP', 'Withdraw SLP', 'Send ETH (mainnet)', 'Send AXS (mainnet)', 'Send SLP (mainnet)']

    message = '''____________________________________________\n'''
    spaces_op = ''
    spaces_op_2 = ''
    for j in range(int((len(titles[0])-len('Operation'))/2)):
        spaces_op += ' '
    for j in range((len(titles[0])-len('Operation'))-int((len(titles[0])-len('Operation'))/2)):
        spaces_op_2 += ' '
    message += '|'+ spaces_op + ' Operation '+ spaces_op_2 +'| Rapid | Fast | Medium | Slow |\n'

    # final_list = final_list[:]

    for i in range(len(titles)):
        prices = ''
        for j in final_list[i]:
            # prices += j.getText()+' | '
            prices += str(j)+' | '
        spaces = ' '
        spaces_2 = ' '
        for j in range(int((len(titles[0])-len(titles[i]))/2)):
            spaces += ' '
        for j in range((len(titles[0])-len(titles[i]))-int((len(titles[0])-len(titles[i]))/2)):
            spaces_2 += ' '
        message += '|'+ spaces + titles[i]+ spaces_2+ '|'+ prices+'\n'

    message += '____________________________________________'

    return message