# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('natsu', 'ナツオ', '', 30,(1,1), 'male', '会社員', "me:僕"),
            ("mina", "ミナト", "", 29,(1,1), "female", "塾講師", "me:私"),
            ("kimi", "キミエ", "", 29,(1,1), "female", "高校教師", "me:わたし"),
            ("sis", "ユミ", "", 21,(1,1), "female", "洋菓子店", "me:私"),
            ("deliver", "配達員", "", 25,(1,1), "male", "配達"),
            ("yoshi", "ヨシムラ", "", 40,(1,1), "male", "家具屋"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Yamanashi", "山梨", "", (120,50)),
            ("Home", "ナツオの家", "Yamanashi"),
            ("ParentsHome", "ナツオの実家", "Yamanashi"),
            ("HerHome", "ミナの家", "Yamanashi"),
            ("Station", "田舎町の駅", "Yamanashi"),
            ("Mall", "商業施設", "Yamanashi"),
            ("Shop", "ナツオの店", "Yamanashi"),
            ("VacantHouse", "廃屋", "Yamanashi"),
            ("BusStop", "バス停", "Yamanashi"),
            ("InBus", "バス車内", "Yamanashi"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("煎餅", "｜煎餅《せんべい》"),
            ("臙脂", "｜臙脂《えんじ》"),
            ("蠢([かきくけこい])", "｜蠢《うごめ》\\1"),
            ),
        }

