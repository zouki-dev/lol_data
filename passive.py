import streamlit as st
from PIL import Image
from urls_folders import folder_project, folder_champion, url_champion, url_file_champion_json
from urls_folders import folder_spell_image, url_spells, url_spell_passive
from urls_folders import folder_item, url_item_all, url_item


def passive(stX, champion, data_champion, folder_spell_image=folder_spell_image):
    passive_name = data_champion["passive"]["image"]["full"]
    im = Image.open(folder_spell_image + "/" + champion + "/" + passive_name)
    stX.image(im)

    if champion == "Anivia":
        stX.text("CD : Plop")

#Passifs
# urgot, taric, anivia, zac, asol, azir, camille, corki, darius,mundo, fiora, gp, illaoi, irelia, ivern, jhin, jinx, viego, vex,ksante, kaisa, kalista, karma, katarina, kayle, khazix, kindred, kog, leona, lillia, lucian, malph, malz, maokai, milio, mf, morde, nilah (xp), ornn, poppy, quinn, rakan, reksai, renata, rengar, rumble, ryze, samira, sej, senna, swain, syndra, taric, tristana, twitch, urgot, varus, velkoz, vex, viego, viktor, vlad, xayah, xerath, yorick, zac, ziggs, zyra