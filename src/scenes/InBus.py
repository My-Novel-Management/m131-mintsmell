# -*- coding: utf-8 -*-
'''
Stage: "バス車内"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def changing_sites(w: World):
    na = w.get("natsu")
    return w.scene('変わりゆく景色',
            w.cmd.change_stage("InBus"),
            w.plot_note("駅前の風景は随分変わってしまって、歯抜けのように廃屋が目立つ"),
            w.plot_note("あの頃から変わらずに「ソフトクリーム」と暖簾を出す米屋はそのままだった"),
            na.be("バスに乗っている"),
            na.do("車内には$Sが一人だけ",
                "あとは白髪の運転手が乗っている"),
            na.do("駅前からかつては商店街っぽい街並みがあったが、",
                "シャッターをしめたり、新しい家になっていたり、",
                "そのまま屋根がつぶれて廃屋になっていたり"),
            na.do("一部はデイサービスに変わったりしていた"),
            na.do("車の往来もほとんどない",
                "あっても軽がたまにすれ違う程度"),
            na.do("トラックの荷台には壊された家の廃材が詰まれていた"),
            na.do("懐かしいソフトクリームの登りを見つける"),
            na.do("夫婦でやっていた米屋だが、まだやっているのがほっとした"),
            na.do("壁のポスターは昭和のもののまま"),
            na.do("信号を左折し、山の方へとバスは入っていく"),
            )

