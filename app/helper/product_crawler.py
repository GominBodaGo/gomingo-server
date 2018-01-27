import requests
from bs4 import BeautifulSoup
from app.model.Item import Item
from app import db
import time


ii = 0
for i in range(1, 30):
    time.sleep(1)
    r = requests.get("http://www.coupang.com/np/rocketdelivery/categories/69627?page=" + str(i))
    soup = BeautifulSoup(r.text, 'html.parser')
    wrapper_li_list = soup.find_all("li", {"class": "baby-product renew-badge"})

    for wrapper_li in wrapper_li_list:
        ii += 1
        if ii % 10 == 0:
            print("now " + str(ii))

        now_name = wrapper_li.find("div", {"class": "name"}).text.strip()
        now_price = wrapper_li.find("strong", {"class": "price-value"})
        try:
            now_price = int(now_price.text.replace(',',''))
            temp_item_row = Item(name = now_name, price = now_price, categoryId = 2)
            db.session.add(temp_item_row)

        except Exception as e:
            print(str(e))
            pass



    db.session.commit()
    print("process end")
