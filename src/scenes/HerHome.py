# -*- coding: utf-8 -*-
'''
Stage: "ミナトの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def kindness(w: World):
    na, mina = w.get("natsu"), w.get("mina")
    sis = w.get("sis")
    return w.scene('やさしい先生',
            w.cmd.change_stage("HerHome"),
            w.plot_note("当時から特に自分の意見を持たない子どもだった$natsuは、それに素直に従い、翌日には彼女の家にお邪魔した"),
            w.plot_note("$minaの教え方は丁寧で、$natsuのテストの点はすぐに上がった"),
            na.come(),
            mina.be(),
            na.do("翌日、彼女の家にお邪魔した"),
            na.do("新築のマンションの一室で、ひと部屋に大きなテーブルがあり、そこに数名の生徒がいた"),
            na.do("紅茶はミントティーで、彼女が焼いたというクッキーが皿に盛られていた"),
            na.do("授業は三人対$minaで行われた"),
            na.do("一人一人に丁寧に教えてくれる"),
            na.do("$S自身は算数も理科も国語も躓いたりはしていなかったけれど、英語に手間取っていた"),
            na.do("違う言語を学ぶ理由がよく分からなかったからだ"),
            na.do("あまり考えすぎずにただ言われるがままに覚えるのもいいと教えられ、とりあえず覚えてそのまま答えを書くことにした"),
            na.do("そのお陰か英語の点数以外も成績が伸びて、両親は喜んだ"),
            na.do("結果的に半年くらいお世話になった"),
            )

