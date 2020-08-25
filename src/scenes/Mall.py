# -*- coding: utf-8 -*-
'''
Stage: "ショッピングモール"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def first_date(w: World):
    return w.scene('二人きりで',
            w.plot_note("夏休みに入り、$minaに誘われて隣町の大型ショッピングモールに出かけた"),
            w.plot_note("姉と三人の予定が、二人きりになり、その時に$minaが既に結婚が決まっていて、少しの間だけ自分がやりたかった塾の仕事をさせてもらっていると知る"),
            w.plot_note("それからも度々、二人で出かけるようになった"),
            w.plot_note("$natsuはいつも$minaの話を聞く役だったけれど、美味しいデザートを食べられて満足だった"),
            )

