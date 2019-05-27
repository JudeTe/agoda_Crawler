import warnings
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
from selenium.common.exceptions import *

count = 0

# 設定DataFrame的Column
df = pd.DataFrame(columns=['King Size','Price'])
lists = []
while True :
    # Ignore the Warnings
    warnings.filterwarnings("ignore")
    time1 = time.time()
    # 設定使Selenium不開啟Browser
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 設定在甚麼路徑選用Chrome Driver及使用何Option
    driver = Chrome("../chromedriver", chrome_options=chrome_options)
    src = 'https://www.agoda.com/zh-tw/bulag-b-b/hotel/nantou-tw.html?' \
          'asq=P%2FqHi77RAEmTXQB%2BCic%2B6agPvxj8O6zhY5EOLVQTgSMz7v6Ub' \
          'woxig5xJbJc49yVH%2FvQ6w4Th9r42HGSTEDOR9U4v0rtyXyTStYUFdiYc5' \
          'wV6Rt6%2FFaFKulceQ7ZWXa14paTD5VHq5sFdVCiCn7snlwoGGd1u6pXWlV' \
          '5RS6QRHWdfczl%2FvwGIeozP3K5i5OrDdkaMRXyBx7XL6YsKZQddw%3D%3D' \
          '&hotel=488056&cid=1732642&tag=41460a09-3e65-d173-1233-629e2' \
          '428d88e&gclid=Cj0KCQiAzKnjBRDPARIsAKxfTRCpxBdIjFocdetlrL5XH' \
          '0lozIhX9YQrkh2MIadXlu7QBv72TsH5j04aAirPEALw_wcB&tick=636861' \
          '686418&languageId=20&userId=abdefbb1-3c7d-486b-80ac-432119d' \
          '9321c&sessionId=wt2sfj0zdeujprlgq3s24zdf&pageTypeId=7&origi' \
          'n=TW&locale=zh-TW&aid=81837&currencyCode=TWD&htmlLanguage=z' \
          'h-tw&cultureInfoName=zh-TW&ckuid=abdefbb1-3c7d-486b-80ac-43' \
          '2119d9321c&prid=0&checkIn=2019-03-02&checkOut=2019-03-03&ro' \
          'oms=1&adults=2&childs=0&priceCur=TWD&los=1&textToSearch=%E6' \
          '%B8%85%E5%A2%83%E5%B8%83%E6%8B%89%E6%A0%BC%E6%99%AF%E8%A7%8' \
          '0%E6%B0%91%E5%AE%BF%20(Bulag%20B%26B)&productType=-1&travel' \
          'lerType=1'
    driver.get(src)
    # driver.refresh()
    # driver.find_element_by_id('paginationNext').click
    try :

        final_Price = driver.find_element_by_class_name('finalPrice')
        price = final_Price.text
        print(price)
        price = price.split('$')[1].split(',')[0] + price.split('$')[1].split(',')[1]
        price = int(price)
        s = pd.Series(['No-BF', price], index=['King Size', 'Price'])
        df = df.append(s, ignore_index=True)
        count += 1
        #每50筆即寫進資料庫
        if count % 50 == 0:
            df.to_csv('YunDeng0405.csv', encoding='utf-8', index=False)

    except StaleElementReferenceException :
        pass
        print('StaleElementReferenceException Occur')

    except NoSuchElementException :
        pass
        print('NoSuchElementException Occur')

    finally:
        time2 = time.time()
        print('Takes ' + str(time2 - time1) + ' Seconds')
        time.sleep(1)






















