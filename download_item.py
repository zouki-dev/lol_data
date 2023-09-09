import streamlit as st
import json
import os
import requests
import pandas as pd

folder_project = "."
folder_item = folder_project+"/item"
url_item_all = "http://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/item.json"
url_item = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/item/"

def download_item(folder_project=folder_project,folder_item=folder_item,url_item_all=url_item_all,url_item=url_item):
    st.subheader("write a csv item.csv")

    items = pd.read_csv("./item.csv")
    st.write(items)

    r = requests.get(url_item_all, allow_redirects=True)
    open(folder_project + "/" + "item.json", 'wb').write(r.content)

    with open(folder_project + "/" + "item.json", encoding='utf-8') as f:
        data_items = json.load(f)["data"]

    keys = [key for key in data_items.keys()]
    items_name = [data_items[key]["name"] for key in keys]
    items_stat = [data_items[key]["stats"] for key in keys]
    items_gold = [data_items[key]["gold"]["base"] for key in keys]
    items_image_name = [data_items[key]["image"]["full"] for key in keys]
    urls_item = [url_item+item_image_name for item_image_name in items_image_name]

    data_output = pd.DataFrame({"item_name":items_name, "item_gold":items_gold, "item_stat":items_stat, "path_item":[folder_item + "/" + item_name for item_name in items_name]})
    data_output.to_csv(folder_project+"/item.csv")

    for item_name, url_item in zip(items_name, urls_item):
        try:
            r = requests.get(url_item, allow_redirects=True)
            st.write(item_name)
            open(folder_item + "/" + item_name + ".png", 'wb').write(r.content)
        except:
            pass
    st.write(items_name)
    st.write(items_stat)
    st.write(data_items[keys[0]])

