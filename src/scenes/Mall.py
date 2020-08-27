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
    na = w.get("natsu")
    mina = w.get("mina")
    return w.scene('デート',
            w.cmd.change_stage("Mall"),
            "ここは将来働く店が入るモールなので、やや丁寧に描写",
            "ここだけしか現在と直結している場所がないので",
            "時代性を見せる",
            "2005年当時だから、あまり活況ではない",
            na.do("新しくできたところで、人も多く、賑わっている"),
            na.do("$minaと服を見て回ったり、参考書を見たりした後で、喫茶店に二人で入った"),
            na.do("大人の女性と二人きりで入った喫茶店では何を頼んでいいか分からない"),
            mina.talk("クリームソーダでも頼もうか？"),
            na.do("言われるがまま、クリームソーダを二つ注文した"),
            na.do("親にファミレスに連れて行ってもらっても、オムライスとかハンバーグとか、そういった定番を頼むだけ"),
            na.do("クリームソーダを自分で頼むのは、何かとハードルが高かった"),
            na.do("やってきたクリームソーダは思っていたものとは少し違い、",
                "不思議な葉っぱが乗っていた"),
            mina.talk("ミントが載せてある"),
            na.do("グリーンではなくて青いクリームソーダ"),
            na.do("少し大人の味がした"),
            )

