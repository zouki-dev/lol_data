import streamlit as st
from spell_range import spell_range
from download_champion import download_champion
from stats_champion import stats_champion
from download_item import download_item
st.set_page_config(layout="wide")


scripts = ["Spell CD / Range", "Update patch-note champion", "stats_champion.json", "download_item"]
script = st.sidebar.selectbox("Select scrpit",scripts)

if script == "Spell CD / Range":
    spell_range()

if script == "Update patch-note champion":
    download_champion()

if script == "stats_champion.json":
    stats_champion()

if script == "download_item":
    download_item()