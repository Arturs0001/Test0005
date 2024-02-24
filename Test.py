import requests
from bs4 import BeautifulSoup

url_base = "https://kups.club"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.session()

for j in range(1, 20):
    print(f"PAGE = {j}")
    url = f"https://kups.club/?page={j}"

    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row mt-4")
        products = allProduct.find_all("div", class_="card h-100")

        for i in range(len(products)):
            try:
                title = products[i].find("h3", class_='card-title').text
                print(title)
                img = products[i].find("a", class_='text-black link-default').text
                print(img)
                price = products[i].find("p", class_='card-text').text
                print(price)
                with open("videogamesaturn.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} {img}---> {price}\n")
            except:
                print("Произошла ошибка")
