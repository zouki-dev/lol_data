import os.path

import requests
import json
import streamlit as st

folder_project = "D:/python/lol_data"
folder_champion = folder_project+"/champion"
url_champion = "http://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/champion/"
url_file_champion_json = "http://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/champion.json"

folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/spell/"

def download_champion(folder_champion=folder_champion, url_champion=url_champion, url_file_champion_json=url_file_champion_json):
    r = requests.get(url_file_champion_json, allow_redirects=True)
    open(folder_project + "/" + "champion.json", 'wb').write(r.content)

    with open(folder_project+"/champion.json", encoding="utf8") as f:
        data_champion_all = json.load(f)["data"]
        champions = [champion for champion in data_champion_all]

    st.subheader("nb_champion : " + str(len(champions)))
    for i,champion in enumerate(champions):
        st.text(str(i)+ " "+ champion)
        r = requests.get(url_champion + champion+".json", allow_redirects=True)

        open(folder_champion + "/" + champion+".json", 'wb').write(r.content)

        with open(folder_champion+"/"+champion+".json", "r", encoding="utf8") as f:
            data_champion = json.loads(f.read())["data"][champion]
        # st.write(data_champion)

        spells = data_champion["spells"]
        for spell in spells:
            spell_name = spell["image"]["full"]
            r = requests.get(url_spells + spell_name, allow_redirects=True)
            if not os.path.exists(folder_spell_image+"/"+champion):
                os.mkdir(folder_spell_image+"/"+champion)
            open(folder_spell_image+"/"+champion + "/" + spell_name, 'wb').write(r.content)

    st.balloons()