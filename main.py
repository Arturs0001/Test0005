import requests

import lxml

from bs4 import BeautifulSoup

url = "https://www.saturn.de/de/category/games-neuheiten-2664.html"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    url = f"https://www.saturn.de/de/category/games-neuheiten-2664.html?page={j}"


    responce = session.get(url, headers=header)
    # print(responce)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "lxml")
        allProduct = soup.find("div", class_="sc-572c0887-0 oLQeQ")
        products = allProduct.find_all("div", class_="sc-dea36e50-0 eErGKu")

        for i in range(len(products)):
            try:
                title = products[i].find("p", class_='sc-f1f881c4-0 iUOwzQ').text
                price = products[i].find("span", class_='sc-f1f881c4-0 cKDSAw sc-b5c27d99-2 fWQVGc').text
                with open("videogamesaturn.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} ---> {price}\n")
            except:
                print(f"{title} скидки неть")

