import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from PIL import Image
import requests
import numpy as np
from passive import passive

folder_project = "."
folder_champion = folder_project+"/champion"
folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/spell/"

def spell_range(folder_champion=folder_champion, folder_spell_image=folder_spell_image, url_spells=url_spells):
    champions = [champion[:-5] for champion in os.listdir(folder_champion)]
    champions = np.sort(champions)

    champions = st.multiselect("Champions :", champions)

    def plot_spell_img_and_range(champion, stX, spell_id, folder_champion=folder_champion, url_spells=url_spells, folder_spell_image=folder_spell_image):
        with open(folder_champion + "/" + champion + ".json", encoding='utf-8') as f:
            data_champion = json.load(f)["data"][champion]
        spells = data_champion["spells"]
        spell = spells[spell_id]
        spell_name = spell["image"]["full"]

        im = Image.open(folder_spell_image+"/"+champion+"/"+spell_name)
        stX.image(im)

        if any([s!=spell['range'][0] for s in spell['range']]):
            stX.text("Range : "+str(spell['range']))
        else:
            if spell['range'][0]>20 and spell['range'][0]<20000 :
                stX.text("Range : "+str(spell['range'][0]))
            else :
                if spell['range'][0]>=20000:
                    stX.text("Range : Global")
                else:
                    stX.text("Range : X")
        stX.text("CD : "+str(spell["cooldownBurn"]))

    if len(champions) == 0:
        n_champion = 1
    else:
        n_champion = len(champions)
    for n_line in range(4):
        stX = st.columns(n_champion)
        for i, champion in enumerate(champions):
            if n_line == 0:
                stX[i].subheader(champion)
                with open(folder_champion + "/" + champion + ".json", encoding='utf-8') as f:
                    data_champion = json.load(f)["data"][champion]
                attackrange = data_champion["stats"]["attackrange"]
                stX[i].text("Attack range : " + str(attackrange))
            plot_spell_img_and_range(champion, stX[i], spell_id=n_line)

    st.markdown("""---""")
    stX = st.columns(n_champion)
    for i, champion in enumerate(champions):
        with open(folder_champion+"/"+champion+".json",encoding='utf-8') as f:
            data_champion = json.load(f)["data"][champion]
        passive(stX[i], champion, data_champion, folder_spell_image=folder_spell_image)

if __name__ == "__main__":
    spell_range()
