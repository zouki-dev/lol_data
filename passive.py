import streamlit as st
from PIL import Image

folder_project = "."
folder_champion = folder_project+"/champion"
folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/spell/"

def passive(stX, champion, data_champion, folder_spell_image=folder_spell_image):
    passive_name = data_champion["passive"]["image"]["full"]
    im = Image.open(folder_spell_image + "/" + champion + "/" + passive_name)
    stX.image(im)

    if champion == "Anivia":
        stX.text("CD : Plop")