# -*- coding: utf-8 -*-
'''
Stage: "廃屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_hideout(w: World):
    return w.scene('彼女の隠れ家',
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("$minaとよく遊んだ「隠れ家」は、彼女の叔母の土地らしいが、",
                "既に草だらけになり、廃屋になっていた"),
            w.plot_note("売地となっているそこに侵入し、廃屋の中に向かう"),
            )


def secret_room(w: World):
    return w.scene("秘密を収めた部屋",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("廃屋の一室、ドレスルーム。いくつもの姿見が並ぶ。そこだけ誰かが住んでいるみたいに掃除されている"),
            w.plot_note("衣装ケースに彼女に買ってもらった服や、$minaの小さい頃の服が仕舞われていた"),
            w.plot_note("$natsuは毎年ここにやってきてそれらを虫干ししていた"),
            )


def the_summer_truth(w: World):
    return w.scene("あの夏の真実",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("あの豪雨の日も、バス停ではなく二人はここにいた"),
            w.plot_note("$natsuは$minaのセーラー服を着せられ、髪を梳かしてもらっていた"),
            w.plot_note("女装した少年を愛でる。それが$minaの隠れた趣味で、",
                "結婚することになってそれがもうできなくなることに苦しんでいた"),
            w.plot_note("あの日キスをしながら「これが最後だね」と寂しそうに笑っていた"),
            w.plot_note("それから一日として合わず、$natsuはたまたま風邪を引いて塾に行けなかった"),
            w.plot_note("一週間後、$minaは自殺した"),
            )


def goodbye_summer(w: World):
    return w.scene("さようなら思い出",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("$natsuはセーラー服を着た自分を見ていた"),
            w.plot_note("それを脱ぎ、庭に出て燃やす"),
            w.plot_note("庭はミントで溢れていた"),
            w.plot_note("ここからミントをもらい、自宅の庭に植えたのだ"),
            w.plot_note("全ての服を燃やして、$minaの思い出を消し去った"),
            w.plot_note("ミントの匂いが酷くて、$natsuは吐いた"),
            )
