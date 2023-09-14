import streamlit as st

with open("version_lol.txt", "r") as f:
    version = f.read()


folder_project = "."
folder_champion = folder_project+"/champion"
url_champion = "http://ddragon.leagueoflegends.com/cdn/"+version+"/data/en_US/champion/"
url_file_champion_json = "http://ddragon.leagueoflegends.com/cdn/"+version+"/data/en_US/champion.json"

folder_spell_image = folder_project+"/spell_image"
url_spells = "http://ddragon.leagueoflegends.com/cdn/"+version+"/img/spell/"
url_spell_passive = "http://ddragon.leagueoflegends.com/cdn/"+version+"/img/passive/"

folder_item = folder_project+"/item"
url_item_all = "http://ddragon.leagueoflegends.com/cdn/"+version+"/data/en_US/item.json"
url_item = "http://ddragon.leagueoflegends.com/cdn/"+version+"/img/item/"
