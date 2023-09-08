import os.path

import requests
import json
import streamlit as st

folder_project = "."
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
            data_champion = json.loads(f.read())
        # st.write(data_champion)

        # correct champion json
        if champion == "Xayah":
            data_champion["data"][champion]["spells"][0]['range'] = [1100]
            data_champion["data"][champion]["spells"][2]['range'] = [25000]
            data_champion["data"][champion]["spells"][3]['range'] = [1060]
        if champion == "Aatrox":
            data_champion["data"][champion]["spells"][0]['range'] = "625 /475 front, 100 behind /200 +300 radius"

            data_champion["data"][champion]["spells"][2]['range'] = [825]
            data_champion["data"][champion]["spells"][3]['range'] = [300]
        if champion == "Milio":
            data_champion["data"][champion]["spells"][1]['range'] = "650/700, gives ally 10/12.5/15/17.5/20% bonus range"
        if champion == "Kayle":
            data_champion["data"][champion]["stats"]["attackrange"] = "175/525/625 at lvl 1/6/16"
        if champion == "Gnar":
            data_champion["data"][champion]["stats"]["attackrange"] = "175 /400+6/lvl(500 max)"
        if champion == "Nidalee":
            data_champion["data"][champion]["stats"]["attackrange"] = "125/525"
        if champion == "Elise":
            data_champion["data"][champion]["stats"]["attackrange"] = "125/550"
        if champion == "Jayce":
            data_champion["data"][champion]["stats"]["attackrange"] = "125/500"
        if champion == "Jinx":
            data_champion["data"][champion]["stats"]["attackrange"] = "525, 605/635/665/695/725"

        with open(folder_champion+"/"+champion+".json", "w") as f:
            json.dump(data_champion,f)

        spells = data_champion["data"][champion]["spells"]
        for spell in spells:
            spell_name = spell["image"]["full"]
            r = requests.get(url_spells + spell_name, allow_redirects=True)
            if not os.path.exists(folder_spell_image+"/"+champion):
                os.mkdir(folder_spell_image+"/"+champion)
            open(folder_spell_image+"/"+champion + "/" + spell_name, 'wb').write(r.content)

    st.balloons()