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
from scenes import BusStop
from scenes import HerHome
from scenes import Home
from scenes import InBus
from scenes import Mall
from scenes import ParentsHome
from scenes import Station
from scenes import VacantHouse


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
MAJOR, MINOR, MICRO = 0, 9, 0
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
def ep_a_summerday(w: World):
    return w.episode("ある夏の日",
            "ミントは強く、地下茎で繁殖するので、隣の家までも容易に増殖してしまう",
            Home.mint(w),
            w.plot_setup("結婚して三年目の夫婦"),
            w.plot_setup("$natsuは庭でミントを育てていた"),
            w.plot_setup("田舎の複合商業施設内の服屋を経営している"),
            w.plot_setup("刺激のない日々を送っている"),
            w.plot_setup("夏になるといつも妻に黙って田舎に旅行で出かける"),
            w.plot_turnpoint("庭のミントを掃除していてあの夏のことを思い出す"),
            )

def ep_summer_memory(w: World):
    return w.episode('あの夏の出来事',
            ParentsHome.meet_mina(w),
            w.plot_develop("$natsuは妻に夏の出来事を語る（嘘を混ぜて）"),
            w.plot_develop("中学の夏、塾のお姉さんとキスをしたことがショックだったと話す"),
            HerHome.kindness(w),
            w.plot_develop("$minaの塾で色々と教わる"),
            w.plot_develop("夏休み、$minaと二人で出かけた"),
            Station.first_date(w),
            Mall.first_date(w),
            BusStop.first_kiss(w),
            w.plot_develop("そのお姉さんは自殺してしまった"),
            w.plot_develop("その話を妻にすると、彼女は「色々と噂があった」と前置きし、",
                "その「いろいろ」を語ってくれた"),
            Home.after_talk(w),
            "田舎の町特有の情報網",
            w.plot_develop("大人たちは誰も彼女の本当の姿を理解していなかったんじゃないか、と言い出す妻"),
            w.plot_turnpoint("妻は当時の噂を知っていたと告白した"),
            "近所の女性とバス停で出会ったならどっちかがバスに乗るはずだった、ということ",
            )

def ep_lost_summer(w: World):
    return w.episode("夏よ、さようなら",
            w.plot_resolve("$natsuは休日に一人、廃屋を訪れる"),
            BusStop.last_summer(w),
            InBus.changing_sites(w),
            w.plot_resolve("廃屋には$minaに女装ごっこをさせられた衣装が隠してあり、それを時折虫干ししていた"),
            VacantHouse.her_hideout(w).omit(),
            VacantHouse.secret_room(w).omit(),
            w.plot_resolve("$natsuは当時$minaと女装ごっこをしていた秘密（セーラー服）を燃やして処分した"),
            VacantHouse.the_summer_truth(w),
            VacantHouse.goodbye_summer(w),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_a_summerday(w),
            ep_summer_memory(w),
            ep_lost_summer(w),
            w.symbol("（了）"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "夏の思い出、というとやはり「恋愛」に関するものが浮かぶ",
            "けれどその多くは短い恋であり、切なさが漂うものだと思う",
            "思い出は少しせつないくらいの方が味があり、楽しいだけのものはフィクションだと似合わない",
            "今回はストレートに「夏の恋の思い出」をベースとして、そこに多少の秘密要素と青春の苦味、人間の裏の顔をミックスし、",
            "作品として仕立て上げる",
            "人間は誰に対しても何かしら秘密を持っている",
            "あれこれオープンにしなければいけないような風潮のある現代だからこそ、秘密を大事にする、というのは一つの大きな課題となるだろう",
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

def about_charas(w: World):
    return (chara_natsu(w),
            chara_mina(w),
            chara_kimi(w),
            )

def chara_natsu(w: World):
    return w.chara_note("$natsuの履歴書",
            "山梨の田舎町に生まれる",
            "両親は役場の職員と、学校の嘱託職員で、兄弟は一人歳の離れた姉がいた",
            "幼い頃からちやほやされながら、あまり自立心なく育つ",
            "五歳の頃に近所に越してきた$minaは姉と仲良くなり、それから$natsuともちょくちょく遊ぶようになった",
            "遊ぶといっても相手をしてもらう程度だ",
            "個人で塾をやっていた$minaは周囲からの評判もよかったが、$natsuには丁寧で優しい先生といった感じの接し方はしてくれなかった",
            "ある日、$minaと出会い、彼女に連れられて郊外のショッピングモールに出かけた",
            "そこで$natsuは彼女に「女性もの」の衣装を購入してもらう",
            "彼女は$natsuに「あなた絶対似合うと思う」と言われ、着てみることになる",
            "今まで言われた通りにする、よくいえば「いいこ」だった$natsuにとって、それはちょっとした冒険のつもりだった",
            "それから$minaとは女装させられるという関係が続く",
            "小学六年の夏、$natsuにはうっすらと髭が生え始める",
            "$minaはそれを丁寧にそり、それでもちょっと残念そうに「大人になっちゃうのね」と",
            "大人のキスをする？と問われて、興味があった$natsuは彼女とキスをする",
            "女装した$natsuをもてあそぶという$minaの性癖は黙っているように言われていた",
            "キスの日から一週間後、$minaは自殺した",
            "周囲からは親に決められた結婚相手が嫌だったとか、色々と噂されていた",
            "女装という遊びはそれで幕を下ろす",
            "大学を出た$natsuは地元に戻ることはなく、そのままアパレル系の会社に就職する",
            "地方の店舗を転勤しながらショップ店長として経験を積み、田舎へと戻ってくる",
            "親の紹介で地元の高校教師である$kimiと結婚し、現在三年目を迎えている",
            "$natsuは毎年夏になると、ある場所に通っていた",
            "そこは$minaとの思い出を集めた、彼女の別荘。空き家だったものがそのままになっている",
            "彼女が死んだ後もそのままで、手付かずで残されていたが、そこに$natsuの女装衣装が残っていた",
            )

def chara_mina(w: World):
    return w.chara_note("$minaの履歴書",
            "昔からの大地主で地元の名家だった家に生まれる",
            "多くの土地を持ち、不動産の他に農場経営にも手を出して成功していた",
            "兄弟はおらず、一人娘として欲しいものはなんでも与えられて育つ",
            "ただその代わりに子どもの頃から習い事は沢山させられ、それに対して否ということは禁じられていた",
            "学校は中学から女子校で大学を出たら花嫁修業の期間を経て結婚する手はずになっていた",
            "結婚相手は親が決めた取引先の息子",
            "一度会ったが悪い人ではなかった",
            "ただ凡庸で刺激に欠けているだけで",
            "$minaは親に隠れて刺激を求めていた",
            "それが性癖を変化させ、女の子らしい遊びから遠ざかっていた衝動から、男の子を女装させて遊ぶというものに発展した",
            "小さくてかわいい男の子と多く出会えるように塾を開く",
            "場所は母親の地元にさせてもらった",
            "そこは幼い頃に祖母から教わった、隠れ家があったからだ",
            "その塾で$natsuと出会い、彼を女装させることに決めた",
            "彼は見事に女装にはまり、関係を持つに至る",
            "けれどある日、彼に髭が生えているのを見て、大人になる、成長する、という悲しさに気づいた",
            "$minaは自分もやがては衰えて死ぬことを理解し、自分で死ぬことを選択した",
            )

def chara_kimi(w: World):
    return w.chara_note("$kimiの履歴書",
            "地元で中学と高校の教師をしていた両親の下に生まれる",
            "兄弟は全員女で四人。$kimiはその二番目だった",
            "女だらけの世界で学校に入ってもずっと女子ばかりでつるんでいた",
            "女性特有の話術と空気読みの世界で育ち、聡明で、口数の少ない方だった$kimiは自分を押し殺して何とかうまく世渡りしていた",
            "女子大を出て教師になる",
            "学校という退屈な空間で、常に心は刺激を求めていた",
            "仕事以外の情報が欲しくて昔からの友人たちとSNSでつながり、よく連絡を取り合っている",
            "そのうちに両親を通じて見合い話が持ち上がり、$kimiはそれに乗った",
            "特に取り柄がなさそうだったが、その中性っぽい顔つきと人畜無害で何も考えてなさそうなところが気に入り、結婚した",
            )

def stage_note(w: World):
    return w.writer_note("場所メモ",
            "メインの舞台は「地方都市、特に田舎っぽさの残る」",
            "民家も繁華街もあるけれど、少しいけば雑木林や廃屋があり、過疎化も進む",
            "バスは時間帯によっては一時間に一本なかったりする",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "見かけによらない、意外な内面を見せつけられた時に脳が理解することを拒否する",
            "本当の姿なんて誰にも見せない。大切な人にも見せない。でも見てもらいたい",
            "そんなアンビバレントな感情を持て余している",
            "田舎の町特有の、あるいは女子特有の情報網で、そういう話が共有されていた",
            "知らないこと、知らないところで、勝手にその人の個性が作られてしまっている",
            "思い出というのは一つの「誰かの妄想」でもある",
            "自分が、あるいは他人の言葉で形作られたフィクション。それが思い出",
            "真実とは遠いことも多い",
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
            *about_charas(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

