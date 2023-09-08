import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from PIL import Image
import requests
import numpy as np

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
        stX.write("Attack range : "+str(attackrange))

        spells = data_champion["spells"]
        for spell in spells:
            spell_name = spell["image"]["full"]

            im = Image.open(folder_spell_image+"/"+champion+"/"+spell_name)
            stX.image(im)

            if any([s!=spell['range'][0] for s in spell['range']]):
                stX.write("range: "+str(spell['range']))
            else:
                if spell['range'][0]>20 and spell['range'][0]<20000 :
                    stX.write("range : "+str(spell['range'][0]))
                else :
                    if spell['range'][0]>=20000:
                        stX.write("range :Global")
                    else:
                        stX.write("range : X")
                stX.write("CD : "+str(spell["cooldownBurn"]))

    for i, champion in enumerate(champions):
        plot_spell_img_and_range(champion, stX[i])

    with st.expander("json"):
        f = open(folder_champion+"/Ashe.json",encoding='utf-8')
        data_champion = json.load(f)["data"]["Ashe"]
        st.write(data_champion)

if __name__ == "__main__":
    spell_range()
