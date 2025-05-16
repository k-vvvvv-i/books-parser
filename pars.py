import requests
from bs4 import BeautifulSoup
import pandas as pd

# Настройки
URL = "http://books.toscrape.com/"

def parse_books():
    # Отправляем запрос
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Находим все карточки товаров
    books = soup.find_all("article", class_="product_pod")
    
    # Собираем данные
    data = []
    for book in books:
        # Название
        name = book.find("h3").find("a")["title"]
        
        # Цена
        price = book.find("p", class_="price_color").text.replace("£", "")
        
        # Ссылка
        link = "http://books.toscrape.com/" + book.find("h3").find("a")["href"]
        
        data.append({
            "Name": name,
            "Price (GBP)": price,
            "Link": link
        })
    
    # Сохраняем в CSV
    df = pd.DataFrame(data)
    df.to_csv("books.csv", index=False, encoding="utf-8")
    print(f"Сохранено {len(data)} книг в books.csv")

if __name__ == "__main__":
    parse_books()