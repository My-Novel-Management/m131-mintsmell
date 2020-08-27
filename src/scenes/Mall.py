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
    return w.scene('二人きりで',
            w.cmd.change_stage("Mall"),
            w.plot_note("夏休みに入り、$minaに誘われて隣町の大型ショッピングモールに出かけた"),
            w.plot_note("姉と三人の予定が、二人きりになり、その時に$minaが既に結婚が決まっていて、少しの間だけ自分がやりたかった塾の仕事をさせてもらっていると知る"),
            w.plot_note("それからも度々、二人で出かけるようになった"),
            w.plot_note("$natsuはいつも$minaの話を聞く役だったけれど、美味しいデザートを食べられて満足だった"),
            na.be("駅前で待ち合わせをしていた"),
            mina.come("だがそこにやってきたのは$Sだけで、姉の姿はなく、"),
            mina.talk("なんか$sisさん急用ができたって"),
            na.talk("そうなんですね", "何も聞いてないけど"),
            na.do("自分の携帯電話には何も連絡がなかった"),
            mina.talk("折角だから$meと二人で、行く？"),
            na.talk("えっと、あの、はい"),
            na.do("こうして二人で隣町のショッピングモールに出かけた"),
            w.br(),
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

