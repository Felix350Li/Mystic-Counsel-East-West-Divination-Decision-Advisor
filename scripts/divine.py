#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mystic-counsel 随机与命理计算工具（确定性输出，避免 AI 凭空编造）。

用法：
  python divine.py coin                         # 金钱卦起一卦（6 爻，含变爻）
  python divine.py tarot 3                      # 抽 3 张塔罗（含正/逆位），默认 1 张
  python divine.py numerology 2007-03-12        # 计算生命数字
  python divine.py rand 1 100                   # 取 [1,100] 区间随机整数

依赖：仅标准库 random / sys，无需安装任何包。
"""
import sys
import random

# ---------------- 塔罗牌数据 ----------------
MAJOR = [
    "愚人", "魔术师", "女祭司", "皇后", "皇帝", "教皇", "恋人", "战车",
    "力量", "隐士", "命运之轮", "正义", "倒吊人", "死神", "节制", "恶魔",
    "高塔", "星星", "月亮", "太阳", "审判", "世界",
]
SUITS = ["权杖", "圣杯", "宝剑", "星币"]
MINOR_RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "侍从", "骑士", "王后", "国王"]


def build_tarot_deck():
    deck = [("大阿尔卡纳", MAJOR[i]) for i in range(22)]
    for suit in SUITS:
        for rank in MINOR_RANKS:
            deck.append((suit, f"{suit}{rank}"))
    return deck  # 22 + 56 = 78 张


def coin_hexagram():
    """三枚硬币起卦，6 次成卦（从下爻到上爻）。
    单枚：2=阴(背)，3=阳(字)；三枚和：6=老阴(变)、7=少阳、8=少阴、9=老阳(变)。"""
    lines = []
    for i in range(6):
        tosses = [random.choice([2, 3]) for _ in range(3)]
        total = sum(tosses)
        if total == 6:
            lines.append(("— —", "老阴", "变→阳"))
        elif total == 7:
            lines.append(("———", "少阳", ""))
        elif total == 8:
            lines.append(("— —", "少阴", ""))
        elif total == 9:
            lines.append(("———", "老阳", "变→阴"))
    return lines


def tarot_draw(n, reversals=True):
    deck = build_tarot_deck()
    drawn = random.sample(deck, min(n, len(deck)))
    result = []
    for arc, name in drawn:
        rev = reversals and random.choice([True, False])
        result.append((arc, name, "逆位" if rev else "正位"))
    return result


def life_number(date_str):
    digits = [int(c) for c in date_str if c.isdigit()]
    if not digits:
        return None
    s = sum(digits)
    while s > 9:
        s = sum(int(c) for c in str(s))
    return s


def main():
    if len(sys.argv) < 2:
        print("usage: divine.py [coin | tarot N | numerology YYYY-MM-DD | rand LO HI]")
        return
    cmd = sys.argv[1]
    if cmd == "coin":
        for idx, (sym, kind, chg) in enumerate(coin_hexagram(), 1):
            print(f"第{idx}爻(下→上): {sym}  {kind}  {chg}")
    elif cmd == "tarot":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        for arc, name, pos in tarot_draw(n):
            print(f"{arc} · {name} · {pos}")
    elif cmd == "numerology":
        d = sys.argv[2] if len(sys.argv) > 2 else "2000-01-01"
        ln = life_number(d)
        print(f"出生日期 {d} 的生命数字：{ln}")
    elif cmd == "rand":
        lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        hi = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        print(random.randint(lo, hi))
    else:
        print("未知命令。可用：coin / tarot N / numerology YYYY-MM-DD / rand LO HI")


if __name__ == "__main__":
    main()
