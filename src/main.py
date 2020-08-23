#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "ミントの匂いと雨の痕"
MAJOR, MINOR, MICRO = 0, 1, 0
COPY = "あの夏の出来事は、一生消えない"
ONELINE = "約8000字の青春恋愛短編。あの夏、豪雨の中でキスをしたお姉さんは自殺した"
OUTLINE = "真面目で良家のお嬢さんという感じだった近所の塾の先生が、ある夏の豪雨のバス停で、キスをした。そのお姉さんが自殺したと聞いた"
THEME = "理解できなかったことが思い出として刻まれ続ける"
GENRE = "恋愛／青春／文学"
TARGET = "10-30years"
SIZE = "8K"
CONTEST_INFO = "妄想コンテスト「ひと夏の思い出」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ヒューマンドラマ", "恋愛", "片思い", "年上の女"]
RELEASED = (8, 20, 2020)


# Episodes
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            w.plot_note("夏場の豪雨を目にして$natsuはあの夏のことを思い出す"),
            w.plot_note("豪雨のバス停、近所で塾をやっていたお姉さんと二人切りになった"),
            w.plot_note("お姉さんは「キスしたことある？」と聞いてきて、キスをしてきた"),
            w.plot_note("それは全然知らない大人のキスで、目の前が真っ白になった"),
            w.plot_note("けれどそれから一週間後にお姉さんは自殺した"),
            w.plot_note("近所の人たちは「そんな子じゃなかったのに」と言った"),
            w.plot_note("その話を（キスの部分を省いて）妻に話す"),
            w.plot_note("妻はミントティーを出して、全て分かっているようなことを言う"),
            "田舎の町特有の情報網",
            w.plot_note("妻から色々な彼女に関する噂を語られる"),
            w.plot_note("それは全然知らない面ばかりだったが、妻は全部ただの噂だと"),
            w.plot_note("「本当の姿なんて大切な人にすら見せないんだから」と言われる"),
            w.plot_note("でもあの夏のバス停で体験したミントの強烈な匂いは真実だった"),
            w.plot_note("今年も夏がやってくる"),
            w.plot_note("あの夏、二人だけの約束をした"),
            w.plot_note("真実を、大切ではない$natsuにだけ伝えていた"),
            w.plot_note("その廃屋には、彼女の宝物が隠されている"),
            w.plot_note("$natsuは彼女の服を取り出して、それを虫干しする"),
            w.plot_note("夏のあの日、お姉さんと一緒にいた$natsuは女装をさせられていた"),
            w.plot_note("それがお姉さんの隠れた趣味だった"),
            w.plot_note("結婚すると言っていたお姉さんはその趣味を諦めることになると悩んでいた"),
            w.plot_note("今でも誰にも見せずに、ときおり女装をしている"),
            w.plot_note("あの夏のミントの匂いを、思い出すために"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "ミントの種を妻が買ってきたのを見て、思い出す",
            "豪雨の中で、思いを寄せる近所の塾のお姉さんが、突然キスしてきた",
            "そのキスがあまりにも自分が知らない大人のもので、そんなことをする女性だと思っていなかった",
            "そのショックがずっと残っている",
            "ミントの匂いがすごいするバス停だった",
            "そのお姉さんは自殺した",
            "誰も全然心当たりも何もないらしい",
            "みんなの評判も主人公が思っている通りだった",
            "何も原因が思い当たらなくて、そんな話を妻にする",
            "すると妻はこんなことを言い出す「その人の本当の姿なんて誰も知らないだけじゃないの？」",
            "本当の姿なんて大切な人にすら見せない、と",
            "妻のことが急に恐ろしく感じた",
            "ミントティーを淹れてきた妻",
            "それを飲んだ夫に「あのときのキスの味？」と、知らないはずなのに尋ねる",
            "それは単なる主人公の勘違いだった",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・主人公の男子",
            "学生時代に近所の真面目そうなお姉さんに豪雨の中でされたキスが忘れられない",
            "・自殺した近所の塾講師のお姉さん",
            "評判もよく、なぜ自殺したのか理由がわからない、という話の女性",
            "・主人公の家族。母親と父親、それに妹か何か。祖父母も",
            "・自殺したお姉さんを知る友人か男友達か",
            "・主人公の妻",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "見かけによらない、意外な内面を見せつけられた時に脳が理解することを拒否する",
            "本当の姿なんて誰にも見せない。大切な人にも見せない。でも見てもらいたい",
            "そんなアンビバレントな感情を持て余している",
            )

def motif_note(w: World):
    return w.writer_note("モチーフメモ",
            "自殺",
            "ゲリラ豪雨", "夏", "入道雲",
            "夕立",
            "塾の先生",
            "年上の女性",
            "バス停",
            "塾", "勉強", "マニュアル",
            "思考放棄",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

