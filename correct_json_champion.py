import streamlit as st
def str_single(l):
    if type(l) != list:
        return str(l)
    if any([e!=l[0] for e in l]):
        return str(l)
    else:
        return str(l[0])

def correct_json_champion(data_champion, champion):
    # correct champion json
    #Stopped at Kindred, Aphelios kaisa w and e cd, katarina cd, not updated

    #Spell range
    if champion == "Xayah":
        data_champion["data"][champion]["spells"][0]['range'] = [1100]
        data_champion["data"][champion]["spells"][2]['range'] = [25000]
        data_champion["data"][champion]["spells"][3]['range'] = [1060]
    if champion == "Aatrox":
        data_champion["data"][champion]["spells"][0]['range'] = "625 /475 front, 100 behind /200 +300 radius"
        data_champion["data"][champion]["spells"][2]['range'] = [825]
        data_champion["data"][champion]["spells"][3]['range'] = [300]
    if champion == "Elise":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Human)\nRange : 475 (Spider)"
        data_champion["data"][champion]["spells"][1]['range'] = str_single(data_champion["data"][champion]["spells"][1]['range']) + " (Human)\nRange : X  (Spider)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (Human)\nRange : 700 (Spider)"
    if champion == "Ekko":
        data_champion["data"][champion]["spells"][3]['range'] = "Global / 375 radius dammage"
    if champion == "Gnar":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Mini)\nRange : 1150 (Mega)"
        data_champion["data"][champion]["spells"][1]['range'] = str_single(data_champion["data"][champion]["spells"][1]['range']) + " (Mini)\nRange : 550 (Mega)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (Mini)\nRange : 675 (Mega)"
    if champion == "Janna":
        data_champion["data"][champion]["spells"][0]['range'] = "1100-1700 based on s charged"
    if champion == "Jayce":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Hammer)\nRange : 1050/1600 (Cannon)"
        data_champion["data"][champion]["spells"][1]['range'] = str_single(data_champion["data"][champion]["spells"][1]['range']) + " (Hammer)\nRange : X (Cannon)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (Hammer)\nRange : 650 target range + 750 width (Cannon)"
    if champion == "Jinx":
        data_champion["data"][champion]["spells"][0]['range'] = "Increased to 605/635/665/695/725"
    if champion == "Karma":
        data_champion["data"][champion]["spells"][3]['range'] = "X"
    if champion == "Kayn":
        data_champion["data"][champion]["spells"][1]['range'] = "700/ 900"
        data_champion["data"][champion]["spells"][2]['range'] = "300 /500"
    if champion == "KogMaw":
        data_champion["data"][champion]["spells"][1]['range'] = "For 8s attack range = 630/650/670/690/710"
    if champion == "Leblanc":
        data_champion["data"][champion]["spells"][3]['range'] = "X"
    if champion == "Leona":
        data_champion["data"][champion]["spells"][0]['range'] = "X"
    if champion == "Milio":
        data_champion["data"][champion]["spells"][1]['range'] = "650/700, gives ally 10/12.5/15/17.5/20% bonus range"
    if champion == "Lillia":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " / Global"
    if champion == "Lulu":
        data_champion["data"][champion]["spells"][3]['range'] = str_single(data_champion["data"][champion]["spells"][3]['range']) + " / 400 radius"
    if champion == "Maokai":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (lasts 30s)"
    if champion == "MissFortune":
        data_champion["data"][champion]["spells"][3]['range'] = [1460]
    if champion == "Nidalee":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Human)\nRange : X (Cougar)"
        data_champion["data"][champion]["spells"][1]['range'] = str_single(data_champion["data"][champion]["spells"][1]['range']) + " (Human)\nRange : 375/750 (Cougar)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (Human)\nRange : 310 (Cougar)"
    if champion == "Olaf":
        data_champion["data"][champion]["spells"][3]['range'] = "X"
    if champion == "Seraphine":
        data_champion["data"][champion]["spells"][3]['range'] = "1200, remaining distance resets each champion hit"
    if champion == "Sett":
        data_champion["data"][champion]["spells"][0]['range'] = "Next two AA have 175 range"
        data_champion["data"][champion]["spells"][1]['range'] = "725 (lasts 3s)"
        data_champion["data"][champion]["spells"][3]['range'] = str_single(data_champion["data"][champion]["spells"][3]['range']) + " / 600 radius"
    if champion == "Sion":
        data_champion["data"][champion]["spells"][0]['range'] = "500-850 (based on channeling time, up to 2s)"
    if champion == "Sylas":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (dash) + 800 (if hit)"
    if champion == "Syndra":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " / 800 to 1300 (sphere)"
    if champion == "TahmKench":
        data_champion["data"][champion]["spells"][2]['range'] = " X "
    if champion == "Tryndamere":
        data_champion["data"][champion]["spells"][3]['range'] = " X "
    if champion == "TwistedFate":
        data_champion["data"][champion]["spells"][1]['range'] = "100 radius (red)"
    if champion == "Twitch":
        data_champion["data"][champion]["spells"][3]['range'] = "Increased to 850, bolts travel 250 further (1100)"
    if champion == "Udyr":
        data_champion["data"][champion]["spells"][2]['range'] = "Recast : AA range increased to 200"
    if champion == "Vayne":
        data_champion["data"][champion]["spells"][1]['range'] = " X "
    if champion == "Vex":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Narrows after 500)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " + Radius 200-300(based on cast distance)"
    if champion == "Viego":
        data_champion["data"][champion]["spells"][3]['range'] = str_single(data_champion["data"][champion]["spells"][3]['range']) + " + 300 radius"
    if champion == "Viktor":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " + 500 (Laser)"
    if champion == "Warwick":
        data_champion["data"][champion]["spells"][3]['range'] = "250% MS"
    if champion == "XinZhao":
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " /1000 (against marked targets)"
    if champion == "Yasuo":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Q1,Q2)\nRange Q3 : 1100 (tornado)"
    if champion == "Yone":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (Q1,Q2)\nRange Q3 : 400 (dash) / 1100 (tornado)"
        data_champion["data"][champion]["spells"][2]['range'] = "300 (initial dash) / Global"
        data_champion["data"][champion]["spells"][3]['range'] = str_single(data_champion["data"][champion]["spells"][3]['range']) + " + blinks 200 behind last ennemy hit"
    if champion == "Yuumi":
        data_champion["data"][champion]["spells"][2]['range'] = " X"
    if champion == "Zac":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " + Attack range becomes 200 for next AA \n The 2 target are 300 displaced toward each other"
        data_champion["data"][champion]["spells"][2]['range'] = "1200/1350/1500/1650/1800 (250 radius)"
    if champion == "Zeri":
        data_champion["data"][champion]["spells"][2]['range'] = "300 + terrain (if within 50 of any)"
    if champion == "Ziggs":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " (cast) / 1400 (max)"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " + 240 radius"
    if champion == "Zoe":
        data_champion["data"][champion]["spells"][0]['range'] = str_single(data_champion["data"][champion]["spells"][0]['range']) + " +800 (from Zoe)"
        data_champion["data"][champion]["spells"][1]['range'] = "2200/Global"
        data_champion["data"][champion]["spells"][2]['range'] = str_single(data_champion["data"][champion]["spells"][2]['range']) + " (+ terrain +50)"


    #Attack range
    if champion == "Elise":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " / 125"
    if champion == "Gnar":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " / 400 to 500 (6/lvl)"
    if champion == "Jayce":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " / 500"
    if champion == "Kayle":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + "/525/625 at lvl 1/6/16"
    if champion == "KSante":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " +25 against marked ennemies"
    if champion == "Nidalee":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " / 125"
    if champion == "Rengar":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + "/ 745 in bush"
    if champion == "Senna":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " + 20/20stacks"
    if champion == "Sett":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " (left) 175 (right)"
    if champion == "Shyvana":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " / 175/190/205 (Dragon)"
    if champion == "Tristana":
        data_champion["data"][champion]["stats"]["attackrange"] = str_single(data_champion["data"][champion]["stats"]["attackrange"]) + " to 661 (+8/lvl)"

    #CD
    if champion == "Aatrox":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = "14/12/10/8/6  (4s between cast)"
    if champion == "Riven":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (4s between cast)"
    if champion == "Amumu":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (3s between charges)"
    if champion == "Akali":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  (3s recast)"
    if champion == "Akshan":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  3 casts before going on CD (takedowns reduce CD to 0.5s)"
    if champion == "BelVeth":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " per-direction CD (can be reset by W)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (hitting an ennemy with W resets the dash CD of the target's direction)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (lasts 1.5s)"
    if champion == "Camille":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (3.5s to recast after 0.25s)"
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + "  (lasts 2.5/3.25/4s)"
    if champion == "Elise":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " (Human) \nCD : 6 (Spider)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (Human) \nCD : 10 (Spider)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (Human) \nnCD : 22/21/20/19/18 (Spider)"
    if champion == "Ezreal":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (if Q hits an ennemy, CDs are reduced by 1.5s)"
    if champion == "Fiora":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (reduced by 50% if target hit)"
    if champion == "Gnar":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " (Mini) \nCD : 20/17.5/15/12.5/10 (Mega)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (Mini) \nCD : 7 (Mega)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (Mini) \nCD : 22/19.5/17/14.5/12 (Mega)"
    if champion == "Gragas":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  (reduced by 3s if ennemy hit)"
    if champion == "Gwen":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + "  (lasts 4s before going on CD)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  (first AA reduces CD by 25/35/45/55/65%)"
    if champion == "Heimerdinger":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (20s recharge, up to 3 charge)"
    if champion == "Kayn":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  (assassin reduces CD to 10s)"
    if champion == "Kindred":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (W reduces CD to 4/3.5/3/2.5/2)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + "  (lasts 8.5s)"
    if champion == "Hecarim":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  (Stacks which reduce CD)"
    if champion == "Ivern":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  (Reapplied without slow if no ennemy damaged)"
    if champion == "Jayce":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " (Hammer) \nCD : 8 (Cannon)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (Hammer) \nCD : 13/11.4/9.8/8.2/6.6/5 (Cannon)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (Hammer) \nCD : 16 (Cannon)"
    if champion == "KaiSa":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + "  Evolved : hitting an ennemy reduces CD by 75%"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + "  Evolved : AA reduce CD by 0.5s"
    if champion == "Katarina":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + "  Takedowns within 3s reduce all CDs by 15s"
    if champion == "Kled":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "  3s to recast if ennemy hit"
    if champion == "Leona":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + "  lasts 3s"
    if champion == "MasterYi":
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + "  Lasts 7s (Takedown extend duration by 7s + reduce basic CDs by 70%"
    if champion == "Mordekaiser":
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + "  Lasts 7s"
    if champion == "Nidalee":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " (Human) \nCD : 6 (Cougar)"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (Human) \nCD : 6 (Cougar)"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (Human) \nCD : 6 (Cougar)"
    if champion == "Ornn":
        data_champion["data"][champion]["spells"][1]['range'] = [500]
        data_champion["data"][champion]["spells"][2]['range'] = "800 / 650 (dash)"
        data_champion["data"][champion]["spells"][3]['range'] = "3000 (1st) / 2550 (2nd)"
    if champion == "Pyke":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " /1100 (based on channeling time)"
    if champion == "Qiyana":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (target) / up to 300 (dash)"
    if champion == "Rakan":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " /1000 (Xayah)"
    if champion == "Rammus":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = " X"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = " X"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (lasts 1.2/1.4/1.6/1.8/2)"
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = "800 up to 1700 (based on MS)"
    if champion == "Sivir":
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + "\nAA reduce basic spells CD by 0.5"
    if champion == "Sylas":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (3.5s to recast)"
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + " (can hold an ult for 90s) \nOn-ult CD : 200% of the target's CD)"
    if champion == "Talon":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " \nOn-terrain CD : 160/135/110/85/60"
    if champion == "Taric":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][0]['cooldownBurn']) + " (15s recharge up to 1/2/3/4/5 charges)\nAfter using a spell, the next 2 AA reduce basic CD by 1s)"
    if champion == "Vayne":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = " Passiv (last 3.5s)"
    if champion == "Vex":
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + " (4s to recast on mark) \nIf takedown within 6s of mark, resets (12s to use)"
    if champion == "Vi":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = " Passiv"
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (charges up to 2)\nRecharge : 12/11/10/9/8"
    if champion == "Viego":
        data_champion["data"][champion]["spells"][3]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][3]['cooldownBurn']) + " \nCD resets to 1.5s during a possession"
    if champion == "XinZhao":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][1]['cooldownBurn']) + " (marks ennemy for 3s)"
    if champion == "Yone":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (lasts 5s)"
    if champion == "Yuumi":
        data_champion["data"][champion]["spells"][1]['cooldownBurn'] = "10/5/0 at lvl 1/6/11\nCan be recast while Yuumi is attached\n5s CD if Yuumi is CCd" + " "
    if champion == "Zeri":
        data_champion["data"][champion]["spells"][0]['cooldownBurn'] = "Depends on AS, capped at 1.5"
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + "\nLasts 5s (CD reduced by Q AA and critW)"
    if champion == "Zilean":
        data_champion["data"][champion]["spells"][2]['cooldownBurn'] = str_single(data_champion["data"][champion]["spells"][2]['cooldownBurn']) + " (reduces Q+E CD by 10s)"

    return data_champion