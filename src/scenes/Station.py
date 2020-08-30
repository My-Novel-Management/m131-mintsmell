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
            na.be("七月に入ったある休日だった",
                "$Sは姉に誘われて$minaと一緒に隣町に新しくできたショッピングモールに買い物に行こうと誘われて、",
                "駅前に一人でやってきた"),
            na.do("駅といっても三年前に無人になってしまい、本数も一時間に一本程度の簡素なものだ",
                "待合室には自販機が二つ並んでいて、地元のよく知らない作家の工芸品が展示されている"),
            mina.come("五分ほどで$minaさんが姿を見せたが、小走りでやってくると彼女は眉を寄せて顔の前で両手を合わせた"),
            mina.talk("なんか$sisさん急用ができたって"),
            na.think("別に怒りは湧いてこなかった",
                "姉はそういう人間で、神経質な母親が「よく主婦なんてやってるわね」と呆れるくらいだからだ"),
            mina.talk("折角だから二人で、行く？"),
            na.talk("えっと、あの、はい"),
            na.do("この日の彼女は普段とは違い、パンツスタイルでとても活動的に見えた"),
            )

