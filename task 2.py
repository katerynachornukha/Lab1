import requests
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

# Функція отримання даних із сайту
def get_rate(start, end):
    url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    parameters = {
        'start': start.strftime("%Y%m%d"),
        'end': end.strftime("%Y%m%d"),
        'sort': 'exchangedate',
        'order': 'desc',
        'json': ''
    }
    # Виконання та перевірка успішності запиту
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, "Помилка у виконанні запиту"

# Визначення дат початку та кінця тижня
start = datetime(2024, 9, 16)
end = datetime(2024, 9, 22)
# Виконання функції
exchange_rate = get_rate(start, end)

# Виведення даних
if exchange_rate:
    current_date = None
    for record in exchange_rate:
        exchangedate = record['exchangedate']
        if exchangedate != current_date:
            current_date = exchangedate
            print(f"\nКурс валют на {current_date}:")
            sorted_records = sorted(exchange_rate, key=lambda x: locale.strxfrm(x['txt']))
            for sorted_record in sorted_records:
                if sorted_record['exchangedate'] == current_date:
                    print(f"  1 {sorted_record['txt']} ({sorted_record['cc']}) = {sorted_record['rate']} грн.")
else:
    print("Помилка! Дані не було отримано.")
