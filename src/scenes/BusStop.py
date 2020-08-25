# -*- coding: utf-8 -*-
'''
Stage: "駅前のバス停"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def first_kiss(w: World):
    return w.scene('はじめてのキス',
            w.plot_note("ある豪雨の日、バス停でたまたま$minaと二人切りになった"),
            w.plot_note("お姉さんは「キスしたことある？」と聞いてきて、キスをしてきた"),
            w.plot_note("それは全然知らない大人のキスで、目の前が真っ白になった"),
            w.br(),
            w.plot_note("けれどそれから一週間後にお姉さんは自殺した"),
            )


def last_summer(w: World):
    return w.scene("最後の夏",
            w.plot_note("$natsuは妻が本当は全部知っているのかもしれないと思い、恐れつつも実家があった田舎町に向かう"),
            w.plot_note("妻には「今年で最後だ」と言っておいた"),
            w.plot_note("駅前からバスに乗る。一時間に一本も来ない田舎だ"),
            )
