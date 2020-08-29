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
    na = w.get("natsu")
    mina, sis = w.get("mina"), w.get("sis")
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
            "冒頭には回想に入る説明を少し",
            na.be(),
            "実家は木造の古い家で、曾祖父さんの代に建てたものを直して使っていた",
            "近所も古い家が多く、またどの家も畑を持っている。そんな田舎町",
            na.explain("実家は古い木造家屋で、冷房は嫌いだという両親によって夏場は窓を開けて扇風機の風で過ごすという環境を強いられていた",
                "$Sは夏休みの宿題を一日何ページを決めてやってしまうタイプで、その日も日中に日陰になる裏庭側の和室の卓袱台にドリルを広げて一人黙々と鉛筆を握っていたことを思い出す"),
            sis.come("#姉が帰ってくる"),
            sis.talk("ただいま"),
            "姉の性格が分かる外見（服装とか目つきくらいでいい）",
            na.do("十歳離れた姉は百メートル離れていても彼女と分かる甲高い声で帰宅の挨拶をすると、",
                "そのままどたどたと足音をさせて部屋までやってくる"),
            mina.come(),
            mina.talk("おじゃまします"),
            "ここで「お嬢様っぽい」第一印象になるよう",
            na.do("百七十の長身の姉の隣には、テレビＣＭから抜け出てきたような白いワンピース姿の女性が立っていた", "&"),
            na.do("とても美人でおしとやかで、お嬢様っぽくて、笑うときも口元を隠すような"),
            # TODO
            na.do("白い襟付きのブラウスがよく似合っていた"),
            sis.talk("近所で塾を始めた$minaさん",
                "今生徒を探してるんだって",
                "あんたどう？"),
            na.do("そんな出会いだった"),
            )

