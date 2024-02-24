import requests

import lxml

from bs4 import BeautifulSoup

url = "https://kups.club"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    url = f"https://kups.club/?page={j}"


    responce = session.get(url, headers=header)
    # print(responce)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "lxml")
        allProduct = soup.find("div", class_="row mt-4")
        products = allProduct.find_all("div", class_="card h-100")

        for i in range(len(products)):
            try:
                title = products[i].find("a", class_='text-black link-default').text
                img = products[i].find("img", class_='mr-2').text
                price = products[i].find("p", class_='card-text').text
                with open("videogamesaturn.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} {img}---> {price}\n")
            except:
                print(f"{title} скидки неть")
                print(f"{img} скидки неть")
