# -*- coding: utf-8 -*-
'''
Stage: "ナツオの実家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def meet_mina(w: World):
    return w.scene('$minaとの出会い',
            w.cmd.change_stage("ParentsHome"),
            w.plot_note("$natsuは妻にある夏の出来事を話して聞かせる"),
            w.plot_note("$natsuには姉がいた"),
            w.plot_note("結婚式の時に見かけただけで特に関わり合いがない程度の関係だ"),
            w.plot_note("ある日、その姉が友人を連れてやってきた"),
            w.plot_note("$natsuが小学校三年の時で、歳の離れた姉は二十歳の$minaを連れてきた"),
            w.plot_note("$minaは近所でも少し評判になっていた、個人塾をやっている女性だ"),
            w.plot_note("おしとやかで、花嫁修業をしに母方の実家で色々と習い事をしながら、",
                "自分でも塾をして子ども相手に教えている"),
            w.plot_note("$minaは$natsuも一度体験入塾をしてほしいと言ってくる"),
            )

