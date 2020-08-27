# -*- coding: utf-8 -*-
'''
Stage: "駅"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def first_date(w: World):
    na = w.get("natsu")
    mina = w.get("mina")
    return w.scene('二人きりで',
            w.cmd.change_stage("Station"),
            w.plot_note("夏休みに入り、$minaに誘われて隣町の大型ショッピングモールに出かけた"),
            w.plot_note("姉と三人の予定が、二人きりになり、その時に$minaが既に結婚が決まっていて、少しの間だけ自分がやりたかった塾の仕事をさせてもらっていると知る"),
            w.plot_note("それからも度々、二人で出かけるようになった"),
            w.plot_note("$natsuはいつも$minaの話を聞く役だったけれど、美味しいデザートを食べられて満足だった"),
            "この出来事が人生の分岐点",
            "姉が適当な人だと、ここまでに打っておく",
            "今まではお嬢様っぽさがあったが、ここから徐々に本当の$minaの姿が見え隠れ",
            "服装も今までとちょっと違ったアクティブな感じに",
            "髪もまとめて活動的なイメージを",
            na.be("駅前で待ち合わせをしていた"),
            mina.come("だがそこにやってきたのは$Sだけで、姉の姿はなく、"),
            mina.talk("なんか$sisさん急用ができたって"),
            na.talk("そうなんですね", "何も聞いてないけど"),
            na.do("自分の携帯電話には何も連絡がなかった"),
            mina.talk("折角だから$meと二人で、行く？"),
            na.talk("えっと、あの、はい"),
            na.do("こうして二人で隣町のショッピングモールに出かけた"),
            )

