# Mystic Counsel · 中西方命理占卜与决策参谋
*East–West Metaphysics & Decision Counsel*

一个 [WorkBuddy](https://www.workbuddy.cn) 的 skill，融合东方玄学（易经 / 紫微斗数 / 风水）
与西方占卜（塔罗牌 / 占星 / 数字命理），**中英双语**为用户提供文化向的命运解读与决策参考。

> ⚠️ 所有内容仅供娱乐、文化研究与自我反思，**不替代**医疗、投资、法律或任何重大人生决策的专业建议。

---

## 🇨🇳 中文

### ✨ 功能覆盖

| 体系 | 能力 |
|---|---|
| 🀄 易经八卦 | 金钱卦起卦、六十四卦速查、变爻（本卦/之卦）分析、体用框架 |
| 🌟 紫微斗数 | 十四主星、十二宫、四化（禄权科忌）、常见格局解读 |
| 🏠 风水 | 五行生克、后天八卦方位、家居/办公布局、常见煞化解 |
| 🃏 塔罗牌 | 78 张牌义（含小阿尔卡纳）、三张/凯尔特十字阵、正逆位 |
| ♈ 西方占星 | 太阳/月亮/上升、十大行星、十二宫位、相位 |
| 🔢 数字命理 | 毕达哥拉斯生命数字（含主数 11/22/33）、天赋数 |
| 🌉 文化桥接 | 中西概念对照：卦象↔塔罗、五行↔四元素、主星↔行星 |
| 🧭 决策框架 | 把玄学意象转译为有边界、可执行的行动建议 |

### 🎯 为什么更准、更贴合实际

- **先锚定现实再解读**：解读前会问你的现状与具体问题，不泛泛而谈
- **区分象/义/行**：牌面卦象是事实（来自脚本），解读是推断，建议是行动，绝不混淆
- **拒绝空话**：不用"你最近压力大"这种放之四海皆准的话，用条件式让你自己验证
- **交叉印证**：重大决策可用第二套体系复核，结论一致更可信

### 📦 安装

**方式一 · 用户级**（对所有项目生效）：将 `mystic-counsel/` 放入 `~/.workbuddy/skills/`
（Windows：`C:\Users\<你>\.workbuddy\skills\`）。

**方式二 · 项目级**（团队共享）：放入 `<项目根>/.workbuddy/skills/`。

**方式三 · 技能中心**：在 WorkBuddy 技能中心直接安装。

### 🔧 随机工具（确定性，避免 AI 瞎编）

```bash
python scripts/divine.py coin                    # 金钱卦起一卦（6 爻，含变爻与卦名）
python scripts/divine.py tarot 3                 # 抽 3 张塔罗（含正/逆位）
python scripts/divine.py celtic                  # 凯尔特十字 10 张（含位置含义）
python scripts/divine.py numerology 2007-03-12   # 生命数字 + 详解
python scripts/divine.py rand 1 100              # 取 [1,100] 随机整数
```

### 🗂 目录结构

```
mystic-counsel/
├── SKILL.md                  # 主控：触发场景、工作流、准确性原则、免责声明（双语）
├── README.md                 # 本文件
├── scripts/
│   └── divine.py             # 确定性随机/命理计算工具
└── references/
    ├── yijing.md             # 易经八卦（中英对照）
    ├── ziwei.md              # 紫微斗数（中英对照）
    ├── fengshui.md           # 风水（中英对照）
    ├── tarot.md              # 塔罗牌（78 张中英对照）
    ├── astrology.md          # 西方占星（行星/宫位/相位）
    ├── western.md            # 数字命理（中英对照）
    ├── cultural-bridge.md    # 中西概念对照桥接
    ├── decision.md           # 决策框架（含安全边界）
    └── examples.md           # 高质量输出示例（中英）
```

---

## 🇬🇧 English

A [WorkBuddy](https://www.workbuddy.cn) skill that blends Chinese metaphysics (I Ching, Ziwei
Doushu, Feng Shui) with Western divination (tarot, astrology, numerology), giving culturally-oriented
readings and decision reflection — in **both Chinese and English**.

> ⚠️ For entertainment, cultural study, and self-reflection only. **Not** a substitute for medical,
> financial, legal, or other major-life professional advice.

### ✨ What it covers

- **I Ching / Bagua** — coin casting, all 64 hexagrams, changing lines, body/use analysis
- **Ziwei Doushu** — 14 major stars, 12 palaces, four transformations, common patterns
- **Feng Shui** — five elements, eight-trigram directions, home/office layout, cures
- **Tarot** — all 78 cards (incl. Minor Arcana), 3-card / Celtic Cross spreads, reversals
- **Western astrology** — sun/moon/rising, ten planets, twelve houses, aspects
- **Numerology** — Pythagorean life path number (incl. master numbers 11/22/33)
- **Cultural bridge** — East↔West concept mapping (hexagrams↔tarot, five elements↔four elements)
- **Decision framework** — turn symbols into bounded, actionable advice

### 🎯 Why the readings feel accurate

- **Ground first, then read** — asks about your real situation before interpreting
- **Fact vs inference** — cards/hexagrams are facts from the script; meaning is inference; advice is action
- **No Barnum fluff** — conditional, self-verifiable language instead of one-size-fits-all lines
- **Cross-validation** — big decisions can be double-checked with a second system

### 📦 Install

Drop `mystic-counsel/` into `~/.workbuddy/skills/` (user-level) or `<project>/.workbuddy/skills/`
(project-level), or install via the WorkBuddy skill center.

### 📄 License

MIT
