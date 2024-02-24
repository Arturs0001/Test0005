import requests

import lxml

from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    url = f"https://cash-backer.club/shops?page={j}"


    responce = session.get(url, headers=header)
    # print(responce)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "lxml")
        allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")
        products = allProduct.find_all("div", class_="card-body")

        for i in range(len(products)):
            try:
                title = products[i].find("div", class_='shop-title').text
                price = products[i].find("div", class_='shop-rate').text
                with open("videogamesaturn.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} ---> {price}\n")
            except:
                print(f"{title} кешбека неть")