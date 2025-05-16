# books-parser
# Парсер книжного магазина Books to Scrape
Простой веб-скрейпер, собирающий данные о книгах (название, цена, ссылка) с сайта Books to Scrape и сохраняющий их в CSV.

## Возможности
- Собирает названия, цены и ссылки с главной страницы.
- Сохраняет данные в `books.csv`.
- Легко расширяем для дополнительных данных.

## Технологии
- Python, requests, BeautifulSoup, pandas

## Установка
1. Клонируйте репозиторий: `git clone https://github.com/yourusername/books-parser`
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Установите зависимости: `pip install -r requirements.txt`
5. Запустите: `python pars.py`

## Вывод
Данные сохраняются в `books.csv`.
