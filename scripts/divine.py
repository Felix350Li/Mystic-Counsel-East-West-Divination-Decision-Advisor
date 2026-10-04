#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mystic-counsel 随机与命理计算工具（确定性输出，避免 AI 凭空编造）。
Deterministic random & numerology tools — never let the model invent draws.

用法 Usage:
  python divine.py coin                      # 金钱卦起一卦（6 爻 + 本卦/之卦名，含变爻）
  python divine.py tarot 3                   # 抽 3 张塔罗（含正/逆位），默认 1 张
  python divine.py celtic                    # 凯尔特十字 10 张（含位置含义）
  python divine.py numerology 2007-03-12     # 生命数字 + 详解
  python divine.py rand 1 100                # 取 [1,100] 区间随机整数

依赖：仅标准库 random / sys。
"""
import sys
import random

# ---------------- 易经八卦/六十四卦 ----------------
# 卦爻表示：1=阳, 0=阴；每卦三元组顺序为(下,中,上)
TRIGRAMS = {
    (1, 1, 1): "乾", (1, 1, 0): "兑", (1, 0, 1): "离", (1, 0, 0): "震",
    (0, 1, 1): "巽", (0, 1, 0): "坎", (0, 0, 1): "艮", (0, 0, 0): "坤",
}
# HEXAGRAMS[(上卦, 下卦)] = 卦名
HEXAGRAMS = {
    ((1,1,1),(1,1,1)): "乾为天", ((1,1,0),(1,1,1)): "天泽履", ((1,0,1),(1,1,1)): "天火同人", ((1,0,0),(1,1,1)): "天雷无妄",
    ((0,1,1),(1,1,1)): "天风姤", ((0,1,0),(1,1,1)): "天水讼", ((0,0,1),(1,1,1)): "天山遁", ((0,0,0),(1,1,1)): "天地否",
    ((1,1,1),(1,1,0)): "泽天夬", ((1,1,0),(1,1,0)): "兑为泽", ((1,0,1),(1,1,0)): "泽火革", ((1,0,0),(1,1,0)): "泽雷随",
    ((0,1,1),(1,1,0)): "泽风大过", ((0,1,0),(1,1,0)): "泽水困", ((0,0,1),(1,1,0)): "泽山咸", ((0,0,0),(1,1,0)): "泽地萃",
    ((1,1,1),(1,0,1)): "火天大有", ((1,1,0),(1,0,1)): "火泽睽", ((1,0,1),(1,0,1)): "离为火", ((1,0,0),(1,0,1)): "火雷噬嗑",
    ((0,1,1),(1,0,1)): "火风鼎", ((0,1,0),(1,0,1)): "火水未济", ((0,0,1),(1,0,1)): "火山旅", ((0,0,0),(1,0,1)): "火地晋",
    ((1,1,1),(1,0,0)): "雷天大壮", ((1,1,0),(1,0,0)): "雷泽归妹", ((1,0,1),(1,0,0)): "雷火丰", ((1,0,0),(1,0,0)): "震为雷",
    ((0,1,1),(1,0,0)): "雷风恒", ((0,1,0),(1,0,0)): "雷水解", ((0,0,1),(1,0,0)): "雷山小过", ((0,0,0),(1,0,0)): "雷地豫",
    ((1,1,1),(0,1,1)): "风天小畜", ((1,1,0),(0,1,1)): "风泽中孚", ((1,0,1),(0,1,1)): "风火家人", ((1,0,0),(0,1,1)): "风雷益",
    ((0,1,1),(0,1,1)): "巽为风", ((0,1,0),(0,1,1)): "风水涣", ((0,0,1),(0,1,1)): "风山渐", ((0,0,0),(0,1,1)): "风地观",
    ((1,1,1),(0,1,0)): "水天需", ((1,1,0),(0,1,0)): "水泽节", ((1,0,1),(0,1,0)): "水火既济", ((1,0,0),(0,1,0)): "水雷屯",
    ((0,1,1),(0,1,0)): "水风井", ((0,1,0),(0,1,0)): "坎为水", ((0,0,1),(0,1,0)): "水山蹇", ((0,0,0),(0,1,0)): "水地比",
    ((1,1,1),(0,0,1)): "山天大畜", ((1,1,0),(0,0,1)): "山泽损", ((1,0,1),(0,0,1)): "山火贲", ((1,0,0),(0,0,1)): "山雷颐",
    ((0,1,1),(0,0,1)): "山风蛊", ((0,1,0),(0,0,1)): "山水蒙", ((0,0,1),(0,0,1)): "艮为山", ((0,0,0),(0,0,1)): "山地剥",
    ((1,1,1),(0,0,0)): "地天泰", ((1,1,0),(0,0,0)): "地泽临", ((1,0,1),(0,0,0)): "地火明夷", ((1,0,0),(0,0,0)): "地雷复",
    ((0,1,1),(0,0,0)): "地风升", ((0,1,0),(0,0,0)): "地水师", ((0,0,1),(0,0,0)): "地山谦", ((0,0,0),(0,0,0)): "坤为地",
}

# ---------------- 塔罗牌 ----------------
MAJOR = ["愚人", "魔术师", "女祭司", "皇后", "皇帝", "教皇", "恋人", "战车", "力量",
         "隐士", "命运之轮", "正义", "倒吊人", "死神", "节制", "恶魔", "高塔", "星星",
         "月亮", "太阳", "审判", "世界"]
MAJOR_EN = ["The Fool","The Magician","The High Priestess","The Empress","The Emperor",
            "The Hierophant","The Lovers","The Chariot","Strength","The Hermit",
            "Wheel of Fortune","Justice","The Hanged Man","Death","Temperance","The Devil",
            "The Tower","The Star","The Moon","The Sun","Judgement","The World"]
SUITS = [("权杖", "Wands"), ("圣杯", "Cups"), ("宝剑", "Swords"), ("星币", "Pentacles")]
MINOR_RANKS = ["1","2","3","4","5","6","7","8","9","10","侍从","骑士","王后","国王"]
MINOR_RANKS_EN = ["Ace","2","3","4","5","6","7","8","9","10","Page","Knight","Queen","King"]

CELTIC_POSITIONS = ["现状 Present", "挑战 Challenge", "过去 Past", "未来 Future",
                    "当下态度 Above", "潜意识/环境 Below", "建议 Advice", "外力 External",
                    "希望与恐惧 Hopes/Fears", "结果 Outcome"]

NUMEROLOGY = {
    1: "独立/领导 The Leader", 2: "合作/协调 The Diplomat", 3: "表达/创造 The Creative",
    4: "务实/稳定 The Builder", 5: "自由/变化 The Explorer", 6: "责任/关爱 The Nurturer",
    7: "内省/智慧 The Seeker", 8: "权力/成就 The Achiever", 9: "慈悲/圆满 The Humanitarian",
    11: "主数·启示 The Illuminator", 22: "主数·建造 The Master Builder", 33: "主数·导师 The Master Teacher",
}


def build_tarot_deck():
    deck = []
    for i in range(22):
        deck.append(("大阿尔卡纳 Major", f"{MAJOR[i]} {MAJOR_EN[i]}"))
    for (s, s_en) in SUITS:
        for r, r_en in zip(MINOR_RANKS, MINOR_RANKS_EN):
            deck.append((f"{s} {s_en}", f"{s}{r} / {r_en} of {s_en}"))
    return deck  # 78 张


def _hexagram_name(six_yao):
    lower = tuple(six_yao[0:3])
    upper = tuple(six_yao[3:6])
    return HEXAGRAMS.get((lower, upper), "未知")


def coin_hexagram():
    """三枚硬币起卦，6 次成卦（下→上），返回每爻与本卦/之卦名。"""
    yaos = []  # (is_yang, is_old)
    for _ in range(6):
        total = sum(random.choice([2, 3]) for _ in range(3))
        if total == 6:
            yaos.append((0, 1))
        elif total == 7:
            yaos.append((1, 0))
        elif total == 8:
            yaos.append((0, 0))
        elif total == 9:
            yaos.append((1, 1))
    ben = _hexagram_name([y for y, _ in yaos])
    changed = [1 - y if old else y for y, old in yaos]
    zhi = _hexagram_name(changed) if any(o for _, o in yaos) else None
    return yaos, ben, zhi


def tarot_draw(n, reversals=True):
    deck = build_tarot_deck()
    drawn = random.sample(deck, min(n, len(deck)))
    out = []
    for arc, name in drawn:
        rev = reversals and random.choice([True, False])
        out.append((arc, name, "逆位 Reversed" if rev else "正位 Upright"))
    return out


def life_number_detail(date_str):
    digits = [int(c) for c in date_str if c.isdigit()]
    if not digits:
        return None
    s = sum(digits)
    while s > 9 and s not in (11, 22, 33):
        s = sum(int(c) for c in str(s))
    return s


def main():
    if len(sys.argv) < 2:
        print("usage: divine.py [coin | tarot N | celtic | numerology YYYY-MM-DD | rand LO HI]")
        return
    cmd = sys.argv[1]

    if cmd == "coin":
        yaos, ben, zhi = coin_hexagram()
        names = {6: "老阴", 7: "少阳", 8: "少阴", 9: "老阳"}
        for idx, (y, o) in enumerate(yaos, 1):
            sym = "———" if y else "— —"
            kind = ("老" if o else ("少")) + ("阳" if y else "阴")
            chg = " (变)" if o else ""
            print(f"第{idx}爻(下→上): {sym}  {kind}{chg}")
        print(f"\n本卦：{ben}")
        if zhi:
            print(f"之卦：{zhi}（含变爻）")
        else:
            print("无变爻，以本卦卦辞为准。")

    elif cmd == "tarot":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        for arc, name, pos in tarot_draw(n):
            print(f"{arc} · {name} · {pos}")

    elif cmd == "celtic":
        for pos, (arc, name, rev) in zip(CELTIC_POSITIONS, tarot_draw(10)):
            print(f"{pos}: {arc} · {name} · {rev}")

    elif cmd == "numerology":
        d = sys.argv[2] if len(sys.argv) > 2 else "2000-01-01"
        ln = life_number_detail(d)
        print(f"出生日期 {d} 的生命数字 Life Path Number：{ln}")
        if ln in NUMEROLOGY:
            print(f"含义 Meaning：{NUMEROLOGY[ln]}")

    elif cmd == "rand":
        lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        hi = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        print(random.randint(lo, hi))

    else:
        print("未知命令。可用：coin / tarot N / celtic / numerology YYYY-MM-DD / rand LO HI")


if __name__ == "__main__":
    main()
