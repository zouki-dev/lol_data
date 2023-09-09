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

#Passifs
# urgot, taric, anivia, zac, asol, azir, camille, corki, darius,mundo, fiora, gp, illaoi, irelia, ivern, jhin, jinx, viego, vex,ksante, kaisa, kalista, karma, katarina, kayle, khazix, kindred, kog, leona, lillia, lucian, malph, malz, maokai, milio, mf, morde, nilah (xp), ornn, poppy, quinn, rakan, reksai, renata, rengar, rumble, ryze, samira, sej, senna, swain, syndra, taric, tristana, twitch, urgot, varus, velkoz, vex, viego, viktor, vlad, xayah, xerath, yorick, zac, ziggs, zyra