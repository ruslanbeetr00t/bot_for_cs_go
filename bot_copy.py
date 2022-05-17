import json
import time
import requests
from setting import API, user_agent, default_price, coin, currency
import pprint


def read_my_inventory_json_file():
    with open('skin_full_info.json', 'r', encoding='utf-8') as file_json:
        my_inventory = json.load(file_json)
        return my_inventory


def bot_work():
    inventory = read_my_inventory_json_file()
    for item in inventory:
        url_search_item_by_hash_name_specific = f'https://...={API}&hash_name={item["market_hash_name"]}'
        response = requests.post(url=url_search_item_by_hash_name_specific, headers=user_agent)
        if response.status_code == 200:
            enemy_item = response.json()["data"][0]
            time.sleep(3)
            if int(enemy_item["id"]) != int(item["item_id"]):
                if int(enemy_item["price"]) > int(item["min_price"] * default_price) and int(enemy_item["price"]) < int(item["max_price"] * default_price):
                    my_price = int(enemy_item["price"]) - coin
                    url_set_price = f'https://...={API}&item_id={item["item_id"]}&price={my_price}&cur={currency}'
                    response = requests.post(url=url_set_price, headers=user_agent)
                    if response.status_code == 200:
                        if response.json()["success"] is True:
                            print(f'{response.json()}:-{item["market_hash_name"]}, {time.ctime()}')
                            time.sleep(1)
                            if item == inventory[-1]:
                                return bot_work()
                elif int(enemy_item["price"]) > int(item["max_price"]):
                    print(f'...:- {response.json()["data"][0]["market_hash_name"]}')
                else:
                    return bot_work(), time.sleep(10)
            else:
                if int(enemy_item["id"]) == int(item["item_id"]):
                    print(f'ЦЕЙ предмет на Першому МІСЦІ в РЕЙТЕНГУ:- {item["market_hash_name"]} :- {time.ctime()}')
                    continue




if __name__ == "__main__":
    bot_work()
