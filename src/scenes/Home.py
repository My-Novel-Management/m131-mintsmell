# -*- coding: utf-8 -*-
'''
Stage: "ナツオの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def mint(w: World):
    na = w.get("natsu")
    kimi = w.get("kimi")
    return w.scene('庭のミント',
            w.cmd.change_camera("natsu"),
            w.cmd.change_stage("Home"),
            w.cmd.change_time("afternoon"),
            w.plot_note("隣からうちでもミントが生えて邪魔と言われたと妻に言われてしまう"),
            w.plot_note("結婚を機に一戸建てを購入した。どうしても庭が欲しかった"),
            w.plot_note("地方都市の郊外の商業施設の、服屋を営んでいる"),
            w.plot_note("実家から少し離れた街"),
            w.plot_note("妻も同じ田舎町出身だが、二人ともあまり実家の町は好きじゃなかった"),
            w.plot_note("妻に「今年も行くの？」と聞かれる"),
            w.plot_note("いつも実家に一人で出かける"),
            w.plot_note("庭のミントの草刈りをしていると急な豪雨が降り出す"),
            w.plot_note("家に入ると、妻がミントティーを出してくれた"),
            w.plot_note("夏場の豪雨を目にして$natsuはあの夏のことを思い出す"),
            )


def after_talk(w: World):
    na = w.get("natsu")
    kimi = w.get("kimi")
    return w.scene("思い出語りを聞いた後で",
            w.cmd.change_stage("Home"),
            w.plot_note("近所の人たちは「そんな子じゃなかったのに」と言った"),
            w.plot_note("妻はミントティーを出して、全て分かっているようなことを言う"),
            w.plot_note("妻から色々な彼女に関する噂を語られる"),
            w.plot_note("それは全然知らない面ばかりだったが、妻は全部ただの噂だと"),
            w.plot_note("「本当の姿なんて大切な人にすら見せないんだから」と言われる"),
            w.plot_note("妻は「ところでその日、バスに乗ってどこに行こうとしてたの？」と尋ねる"),
            na.be(),
            kimi.be(),
            na.do("思い出を話し終えた"),
            na.do("外の雨の勢いは弱まり、涼しいくらいの小雨に変わっている"),
            kimi.talk("それで？"),
            na.talk("分からないことって、いつまでも人生のどこかに引っかかっていて、",
                "それをこういうタイミングでふと思い出すってこと、ないか？"),
            kimi.talk("その人って自殺したんでしょ？",
                "だからずっとあなたの心に引っかかりがあるってことかしら？"),
            na.think("死んだことに関しては人生に何も影響ないとは思わないが、",
                "うまく説明できなかった"),
            kimi.talk("結局自殺ってよく分からないじゃない",
                "ちょっとしたきっかけがあれば誰でもその一歩を踏み出しちゃう可能性ってある気もするし、",
                "本人がどんなことで悩んでたとか、そういうのって周囲は分からないじゃない"),
            kimi.talk("そもそも自分の大切な部分とか、本音とか、誰にでも話すってことはないのは分かるけど、",
                "大切な人にだって、いいえ、だからこそ話さないとかもあるものね"),
            na.talk("お前もそうなのか？"),
            kimi.talk("隠し事の一つや二つはあるものです",
                "あなただって今年もまた出かけるんでしょ？"),
            na.do("答えられずに口ごもる"),
            kimi.talk("別に何してるとか聞きませんから安心して下さいよ",
                "たまには一人で息抜きしたい時だってあるんでしょうから"),
            na.talk("別に$meはそんなつもりじゃあ"),
            kimi.talk("ところでその日、バスに乗ってどこに行くつもりだったんですか？"),
            na.talk("え？"),
            kimi.talk("だってあなたの家の近所だったんですよね、そのお姉さんの家"),
            na.do("妻の目が笑っていた"),
            )
