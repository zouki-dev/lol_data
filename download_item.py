import streamlit as st
import json
import os
import requests
import pandas as pd
from urls_folders import folder_project, folder_champion, url_champion, url_file_champion_json
from urls_folders import folder_spell_image, url_spells, url_spell_passive
from urls_folders import folder_item, url_item_all, url_item

folder_project = "."

def download_item(folder_project=folder_project,folder_item=folder_item,url_item_all=url_item_all,url_item=url_item):
    items = pd.read_csv("./item.csv")
    st.write(items)
    with open("./item.csv", "r") as f:
        st.sidebar.download_button("Download Data item.csv", f, file_name="item.csv")
        st.download_button("Download data item.csv ", f, file_name="item.csv")

    st.subheader("Updating... Wait for baloons")
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
