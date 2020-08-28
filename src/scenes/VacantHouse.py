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
    na, mina = w.get("natsu"), w.get("mina")
    return w.scene('彼女の隠れ家',
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("$minaとよく遊んだ「隠れ家」は、彼女の叔母の土地らしいが、",
                "既に草だらけになり、廃屋になっていた"),
            w.plot_note("売地となっているそこに侵入し、廃屋の中に向かう"),
            "歩いてきて、売地になっているのは見せること",
            "廃墟になっている、というふうな説明も",
            na.come("徒歩でやってくる"),
            na.do("石塀で囲まれた廃屋"),
            na.do("表には「売地」と赤い字の看板が立っていた"),
            na.do("石塀の向こう側に伸びた松や栃の木が見える"),
            na.do("鉄柵のほつれたところを開け、中に入っていく"),
            "余裕があったら廃屋の描写",
            )


def secret_room(w: World):
    na, mina = w.get("natsu"), w.get("mina")
    return w.scene("秘密を収めた部屋",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("廃屋の一室、ドレスルーム。いくつもの姿見が並ぶ。そこだけ誰かが住んでいるみたいに掃除されている"),
            w.plot_note("衣装ケースに彼女に買ってもらった服や、$minaの小さい頃の服が仕舞われていた"),
            w.plot_note("$natsuは毎年ここにやってきてそれらを虫干ししていた"),
            "部屋の描写は丁寧にする",
            "温度や湿度、暗さ、匂いなども",
            na.come("部屋に入ってくる"),
            na.do("その部屋だけは毎年$natsuが掃除をして綺麗にしている"),
            na.do("衣装ケースが並び、姿見がいくつもある"),
            na.do("カーテンは黴びている"),
            na.do("床のカーペットも変色し、一部は軋む"),
            na.do("頭部だけのマネキンにウィッグが被せて並べてあった"),
            na.do("カーテンを開けて、裏庭へのサッシを開ける"),
            na.do("ミントが鬱蒼と茂って匂いがすごかった"),
            )


def the_summer_truth(w: World):
    na, mina = w.get("natsu"), w.get("mina")
    return w.scene("あの夏の真実",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("あの豪雨の日も、バス停ではなく二人はここにいた"),
            w.plot_note("$natsuは$minaのセーラー服を着せられ、髪を梳かしてもらっていた"),
            w.plot_note("女装した少年を愛でる。それが$minaの隠れた趣味で、",
                "結婚することになってそれがもうできなくなることに苦しんでいた"),
            w.plot_note("あの日キスをしながら「これが最後だね」と寂しそうに笑っていた"),
            w.plot_note("それから一日として合わず、$natsuはたまたま風邪を引いて塾に行けなかった"),
            w.plot_note("一週間後、$minaは自殺した"),
            "ここでネタバラシ",
            "お姉さんの隠し事を教える",
            "読者に対しての秘密の暴露",
            na.be(),
            na.think("夏の日の真実を思い返していた"),
            na.think("妻にはバス停で、と語ったが、すぐにバレた通り、本当はこの別荘にいた"),
            na.think("彼女の「隠れ家」に招待され、そこで初めて彼女の性癖をばらされた"),
            na.think("$minaは男の子に女装をさせて遊ぶのが好きだった"),
            na.think("あの日もいつものようにフリルのついた服を着せながら「かわいいね」と髪を梳かしていた"),
            na.think("けれど、$minaは顔をよく見ていて、そこに髭を見つけた"),
            mina.talk("そっか、男の子だものね"),
            mina.do("残念そうにそう言いながらその伸び始めた一本の髭を化粧挟みでカットする"),
            mina.talk("ねえ、キス、したことある？"),
            na.think("ない、と答えると、$minaは顔を掴んで動けないようにして、そのまま唇を重ねた"),
            mina.talk("$meも、ないんだ"),
            mina.do("そう言って笑う"),
            na.think("したことない、というのに、そのキスは何度も口の中を出入りするような大人のキスだった"),
            na.think("外は酷い雨で、その音だけが記憶に残っている"),
            na.think("翌日、酷い風邪を引いて塾を休んだ"),
            na.think("それから一週間後に$minaは自殺をした"),
            )


def goodbye_summer(w: World):
    na, mina = w.get("natsu"), w.get("mina")
    return w.scene("さようなら思い出",
            w.cmd.change_stage("VacantHouse"),
            w.plot_note("$natsuはセーラー服を着た自分を見ていた"),
            w.plot_note("それを脱ぎ、庭に出て燃やす"),
            w.plot_note("庭はミントで溢れていた"),
            w.plot_note("ここからミントをもらい、自宅の庭に植えたのだ"),
            w.plot_note("全ての服を燃やして、$minaの思い出を消し去った"),
            w.plot_note("ミントの匂いが酷くて、$natsuは吐いた"),
            na.be(),
            "セーラー服に着替えた、大人になってしまった自分",
            "成長することを選んだ主人公と、成長しないこと、結婚しないことを選択した彼女の差",
            "みにくくなったというだろうか？　と",
            na.do("姿見に映るセーラー服姿の自分を見ていた"),
            na.think("まだ若く肌もつるりとしていた頃の、よく似合っていたのとは違い、",
                "大人になり、男になり、なんとも不格好になってしまっている"),
            na.think("$minaはこれを想像して嘆いたのだろうか、と考える"),
            na.do("服を脱いで綺麗に畳む"),
            na.do("裏庭に出て、少し草をむしる"),
            na.do("かつては使われていた焼却炉に服を入れ、火をつけた"),
            na.do("次々に焼却処分していく"),
            na.do("周囲はミントの匂いに溢れていた"),
            )
