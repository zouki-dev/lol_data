import os.path

import requests
import json
import streamlit as st
from correct_json_champion import correct_json_champion

folder_project = "."
folder_champion = folder_project+"/champion"
url_champion = "http://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/champion/"
url_file_champion_json = "http://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/champion.json"

folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/spell/"
url_spell_passive = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/passive/"

def download_champion(folder_champion=folder_champion, url_champion=url_champion, url_file_champion_json=url_file_champion_json):
    r = requests.get(url_file_champion_json, allow_redirects=True)
    open(folder_project + "/" + "champion.json", 'wb').write(r.content)

    with open(folder_project+"/champion.json", encoding="utf8") as f:
        data_champion_all = json.load(f)["data"]
        champions = [champion for champion in data_champion_all]

    st.subheader("nb_champion : " + str(len(champions)))
    for i,champion in enumerate(champions):
        if not os.path.exists(folder_spell_image+"/"+champion):
            os.mkdir(folder_spell_image+"/"+champion)
        st.text(str(i)+ " "+ champion)
        r = requests.get(url_champion + champion+".json", allow_redirects=True)

        open(folder_champion + "/" + champion+".json", 'wb').write(r.content)

        with open(folder_champion+"/"+champion+".json", "r", encoding="utf8") as f:
            data_champion = json.loads(f.read())
        # st.write(data_champion)

        correct_json_champion(data_champion, champion)

        with open(folder_champion+"/"+champion+".json", "w") as f:
            json.dump(data_champion,f)

        spells = data_champion["data"][champion]["spells"]
        for spell in spells:
            spell_name = spell["image"]["full"]
            r = requests.get(url_spells + spell_name, allow_redirects=True)
            open(folder_spell_image+"/"+champion + "/" + spell_name, 'wb').write(r.content)

        image_passive_name = data_champion["data"][champion]["passive"]["image"]["full"]
        r2 = requests.get(url_spell_passive + image_passive_name, allow_redirects=True)
        open(folder_spell_image + "/" + champion + "/" + image_passive_name, 'wb').write(r2.content)
    st.balloons()