# -*- coding: utf-8 -*-
'''
Stage: "バス車内"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def changing_sites(w: World):
    return w.scene('変わりゆく景色',
            w.cmd.change_stage("InBus"),
            w.plot_note("駅前の風景は随分変わってしまって、歯抜けのように廃屋が目立つ"),
            w.plot_note("あの頃から変わらずに「ソフトクリーム」と暖簾を出す米屋はそのままだった"),
            )

