# -*- coding: utf-8 -*-
'''
Stage: "ナツオの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def mint(w: World):
    return w.scene('庭のミント',
            w.cmd.change_camera("natsu"),
            w.cmd.change_stage("Home"),
            w.cmd.change_time("afternoon"),
            w.plot_note("隣からうちでもミントが生えて邪魔と言われたと妻に言われてしまう"),
            w.plot_note("結婚を機に一戸建てを購入した。どうしても庭が欲しかった"),
            w.plot_note("地方都市の郊外の商業施設の、服屋を営んでいる"),
            w.plot_note("実家から少し離れた街"),
            w.plot_note("妻も同じ田舎町出身だが、二人ともあまり実家の町は好きじゃなかった"),
            w.plot_note("妻に「今年も行くの？」と聞かれる"),
            w.plot_note("いつも実家に一人で出かける"),
            w.plot_note("庭のミントの草刈りをしていると急な豪雨が降り出す"),
            w.plot_note("家に入ると、妻がミントティーを出してくれた"),
            w.plot_note("夏場の豪雨を目にして$natsuはあの夏のことを思い出す"),
            )


def after_talk(w: World):
    return w.scene("思い出語りを聞いた後で",
            w.cmd.change_stage("Home"),
            w.plot_note("近所の人たちは「そんな子じゃなかったのに」と言った"),
            w.plot_note("妻はミントティーを出して、全て分かっているようなことを言う"),
            w.plot_note("妻から色々な彼女に関する噂を語られる"),
            w.plot_note("それは全然知らない面ばかりだったが、妻は全部ただの噂だと"),
            w.plot_note("「本当の姿なんて大切な人にすら見せないんだから」と言われる"),
            w.plot_note("妻は「ところでその日、バスに乗ってどこに行こうとしてたの？」と尋ねる"),
            )
