import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

Number = 1

while Number < 6:
    url = f'http://jdm-expo.com/3-vehicle-inventory?p={Number}'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    Names = soup.find_all("h2", class_="product-name")
    cars = [i.a["title"] for i in Names]
    f = open("jdmCarNames.csv", "a")
    write_obj = csv.writer(f)
    for i in cars:
        write_obj.writerow([i])
    write_obj.writerow(["Page End"])
    Number += 1
    sleep(15)
