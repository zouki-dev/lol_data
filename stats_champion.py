import streamlit as st
import numpy as np
import pandas as pd
import json
import os
import requests

folder_project = "."
folder_champion = folder_project+"/champion"
folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/spell/"

def stats_champion(folder_champion=folder_champion):
    champions = [champion[:-5] for champion in os.listdir(folder_champion)]
    champion = st.selectbox("Champions", champions)

    with open(folder_champion + "/" + champion + ".json", encoding='utf-8') as f:
        data_champion = json.load(f)["data"][champion]

    st.write(data_champion["stats"])
    with st.expander("json"):
        st.write(data_champion)