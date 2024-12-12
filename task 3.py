import requests
from datetime import datetime
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

# Функція отримання даних із сайту
def get_rate(start, end):
    url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    parameters = {
        'start': start.strftime("%Y%m%d"),
        'end': end.strftime("%Y%m%d"),
        'sort': 'exchangedate',
        'order': 'asc',
        'json': ''
    }
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

# Будування графіків
if exchange_rate:
    currency_data = {}

    # Зберігаємо дані для кожної валюти
    for record in exchange_rate:
        currency = record['cc']
        if currency not in currency_data:
            currency_data[currency] = {'dates': [], 'rates': [], 'name': record['txt']}
        currency_data[currency]['dates'].append(record['exchangedate'])
        currency_data[currency]['rates'].append(record['rate'])

    # Створюємо графіки для кожної валюти
    for currency, data in currency_data.items():
        if data['rates']:
            fig, ax = plt.subplots(figsize=(12, 6))
            plt.plot(data['dates'], data['rates'], marker='*', ms=12, mfc='c', mec='b', label=f"{data['name']} ({currency})", lw=3, c='#FC777B')
            plt.title(f"Зміна курсу {data['name']} ({currency})")
            plt.xlabel('Дата')
            plt.ylabel('Курс (грн.)')
            plt.xticks(rotation=20)
            plt.grid()
            plt.legend()
            plt.tight_layout()
            fig.canvas.manager.set_window_title(f"Курс {currency}")
    plt.show()

else:
    print("Помилка! Дані не було отримано.")
