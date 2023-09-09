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
    if len(champions)==0:
        stX=st
    else:
        stX = st.columns(len(champions))

    def plot_spell_img_and_range(champion, stX, folder_champion=folder_champion, url_spells=url_spells, folder_spell_image=folder_spell_image):
        stX.subheader(champion)
        with open(folder_champion+"/"+champion+".json",encoding='utf-8') as f:
            data_champion = json.load(f)["data"][champion]
        attackrange = data_champion["stats"]["attackrange"]
        stX.text("Attack range : "+str(attackrange))

        spells = data_champion["spells"]
        for spell in spells:
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

    for i, champion in enumerate(champions):
        plot_spell_img_and_range(champion, stX[i])
        with open(folder_champion+"/"+champion+".json",encoding='utf-8') as f:
            data_champion = json.load(f)["data"][champion]

        stX[i].subheader("Passive")
        passive(stX[i], champion, data_champion, folder_spell_image=folder_spell_image)

    with st.expander("json"):
        f = open(folder_champion+"/Ashe.json",encoding='utf-8')
        data_champion = json.load(f)["data"]["Ashe"]
        st.write(data_champion)

if __name__ == "__main__":
    spell_range()
