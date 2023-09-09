import streamlit as st
from spell_range import spell_range
from download_champion import download_champion
from stats_champion import stats_champion
from download_item import download_item
st.set_page_config(layout="wide")


scripts = ["spell_range", "download_champion", "stats_champion", "download_item"]
script = st.sidebar.selectbox("Select scrpit",scripts)

if script == "spell_range":
    spell_range()

if script == "download_champion":
    download_champion()

if script == "stats_champion":
    stats_champion()

if script == "download_item":
    download_item()