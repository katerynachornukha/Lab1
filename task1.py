import matplotlib.pyplot as plt
import requests
import json
from requests import request

# https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240920&valcode=usd&json

reply = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240920&valcode=usd&json ")

reply_json = json.loads(reply.text)

output_dict = {}
for item in reply_json:
    print(item)
    output_dict[item['exchangedate']] = item['rate']
    print(output_dict)

#print(output_dict)
#print(output_dict_key())
fig, ax = plt.subplots()
#value_list = sorted(output_dict.items())
plt.plot(output_dict.keys(), output_dict.values())
plt.show()
