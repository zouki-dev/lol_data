import streamlit as st
import numpy as np
import pandas as pd
import json
import os
import requests
from urls_folders import folder_project, folder_champion, url_champion, url_file_champion_json
from urls_folders import folder_spell_image, url_spells, url_spell_passive
from urls_folders import folder_item, url_item_all, url_item


def stats_champion(folder_champion=folder_champion):
    champions = [champion[:-5] for champion in os.listdir(folder_champion)]
    champion = st.selectbox("Champions", champions)

    with open(folder_champion + "/" + champion + ".json", encoding='utf-8') as f:
        data_champion = json.load(f)["data"][champion]

    st.write(data_champion["stats"])
    with st.expander("json"):
        st.write(data_champion)