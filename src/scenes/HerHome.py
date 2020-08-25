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
    return w.scene('やさしい先生',
            w.cmd.change_stage("HerHome"),
            w.plot_note("当時から特に自分の意見を持たない子どもだった$natsuは、それに素直に従い、翌日には彼女の家にお邪魔した"),
            w.plot_note("$minaの教え方は丁寧で、$natsuのテストの点はすぐに上がった"),
            )

