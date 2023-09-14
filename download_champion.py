import os.path

import requests
import json
import streamlit as st
from correct_json_champion import correct_json_champion

def download_champion():
    st.write("URL patch-notes : https://www.leagueoflegends.com/fr-fr/news/tags/patch-notes/")
    with open("version_lol.txt","r") as f:
        version = f.read()
    version = st.text_input("version", version)
    url_test = "http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion/Anivia.json"
    st.write("URL to Anivia.jon of the vesion : "+ url_test)
    try:
        r = requests.get(url_test, allow_redirects=True)
        if not "Access Denied" in str(r.content):
            with open("version_lol.txt","wb") as f:
                f.write(version.encode())
        else:
            st.error("URLs are not fund")
    except:
        st.error("URLs are not fund")
    from urls_folders import folder_project, folder_champion, url_champion, url_file_champion_json
    from urls_folders import folder_spell_image, url_spells, url_spell_passive

    if st.button("Download") or st.sidebar.button("Download..."):
        r = requests.get(url_file_champion_json, allow_redirects=True)
        with open(folder_project + "/" + "champion.json", 'wb') as f:
            f.write(r.content)

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