# Mystic Counsel · 中西方命理占卜与决策参谋

一个 [WorkBuddy](https://www.workbuddy.cn) 的 skill，融合东方玄学（易经 / 紫微斗数 / 风水）
与西方占卜（塔罗牌 / 数字命理），为用户提供**文化向**的命运解读与决策参考。

> ⚠️ 所有内容仅供娱乐、文化研究与自我反思，**不替代**医疗、投资、法律或任何重大人生决策的专业建议。

## ✨ 功能覆盖

- **易经八卦**：金钱卦起卦、六十四卦速查、变爻（本卦/之卦）分析、体用框架
- **紫微斗数**：十四主星、十二宫、四化（禄权科忌）、常见格局解读框架
- **风水**：五行生克、后天八卦方位、家居/办公布局要点、常见煞的化解
- **塔罗牌**：78 张牌义、三张阵 / 凯尔特十字阵、正逆位解读
- **西方占卜**：毕达哥拉斯生命数字（含主数 11/22/33）等
- **决策框架**：把玄学意象转译为有边界、可执行的行动建议

## 📦 安装

**方式一 · 用户级（对所有项目生效）**
将 `mystic-counsel/` 整个目录放入 `~/.workbuddy/skills/`（Windows：`C:\Users\<你>\.workbuddy\skills\`）。

**方式二 · 项目级（团队共享）**
放入 `<项目根>/.workbuddy/skills/`。

**方式三 · 技能中心**
在 WorkBuddy 的技能中心直接安装本 skill。

## 🔧 随机工具

为避免 AI 凭空编造随机结果，`scripts/divine.py` 提供确定性随机（仅依赖 Python 标准库）：

```bash
python scripts/divine.py coin                    # 金钱卦起一卦（6 爻，含变爻）
python scripts/divine.py tarot 3                 # 抽 3 张塔罗（含正/逆位）
python scripts/divine.py numerology 2007-03-12   # 计算生命数字
python scripts/divine.py rand 1 100              # 取 [1,100] 随机整数
```

## 🗂 目录结构

```
mystic-counsel/
├── SKILL.md                  # 主控：触发场景、工作流、免责声明
├── README.md                 # 本文件
├── scripts/
│   └── divine.py             # 确定性随机/命理计算工具
└── references/
    ├── yijing.md             # 易经八卦
    ├── ziwei.md              # 紫微斗数
    ├── fengshui.md           # 风水
    ├── tarot.md              # 塔罗牌
    ├── western.md            # 西方占卜/数字命理
    └── decision.md           # 决策框架（含安全边界）
```

## 📄 License

MIT
