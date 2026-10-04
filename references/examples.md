# 输出示例 Output Exemplars（黄金标准）

本文件提供高质量解读的"黄金标准"。AI 应照此**格式、深度与贴合度**输出。
共同流程：**先锚定现实 → 调用脚本取象 → "象/义/行"三段 → 结尾免责**。
不要跳过"锚定现实"——这是"贴合实际"的关键。

---

## 示例 1 · 塔罗三张阵（事业抉择）· 中文

**用户**：我在纠结要不要跳槽。

**AI 锚定**（1–2 问，不一次问全）：方便说说你现在的处境和纠结点吗？
**用户**：现公司稳定但没成长，新公司给得多但不太确定。

**AI 调脚本**：`python scripts/divine.py tarot 3`
→ 输出：`权杖 · 权杖8 · 正位`（过去）/ `宝剑 · 宝剑2 · 逆位`（现在）/ `星币 · 星币10 · 正位`（未来）

**AI 输出**：

> **象**：过去「权杖8·正位」（快速推进、多线展开）；现在「宝剑2·逆位」（僵持在松动、不得不选）；未来「星币10·正位」（物质稳定、长期保障）。
>
> **义**：结合你说的情况——过去的牌像"你一直在快速往前冲"，现在这张逆位的宝剑2说明"两个都想要"的僵持已经到头，**你其实已经被推到必须选的路口**。未来这张星币10指向的是"长期的、踏实的物质安全感"，而不是短期的高薪刺激。
>
> **行**：如果你真正看重的是"5 年后还能稳"，这张牌偏向能让你沉下来的方向；如果只是被数字打动，星币10 提醒你比的是"长期保障"而非"起薪"。建议把两份工作各自"3 年后的样子"写出来对照，答案会更清楚。
>
> 仅供娱乐与文化参考，重大决策请咨询专业人士。

---

## 示例 2 · 易经金钱卦（感情）· 中文

**用户**：我和他能成吗？

**AI 锚定**：你们现在到哪一步了？你主要卡在哪？
**用户**：认识半年，他忽冷忽热。

**AI 调脚本**：`python scripts/divine.py coin`
→ 输出六爻，推得本卦「泽山咸」，一爻变，之卦「泽地萃」。

**AI 输出**：

> **象**：本卦「咸」（感应、相悦），上六爻变，之卦「萃」（聚合）。
>
> **义**：「咸」是"少男在下、少女在上，两情相感"的卦，说明**这段关系底子是有感应的**。但变爻在上六——"咸其辅颊舌"，是"只剩嘴上说说、感应流于表面"的位置，正好对上你说的"忽冷忽热"。之卦「萃」是"聚合"，提示：若能把"感应"从嘴上落到实际的相处和共同圈子（萃有聚众之意），才走得拢。
>
> **行**：这段感情的关键不在"他有没有感应"，而在"感应有没有落到实处"。建议别靠猜，找一次面对面的认真相处（萃=聚），看他是"只动嘴"还是"愿意一起做事"。
>
> 仅供娱乐与文化参考，重大决策请咨询专业人士。

---

## 示例 3 · 重大决策交叉印证（创业）· 中英

**用户**：要不要辞职创业？（重大决策 → 用两套体系印证）

**AI**：这属于重大决策，我用塔罗和易经各看一次，再对照。先问一句：你现在的资源（积蓄/技能/客户）和最大顾虑是什么？

> **Tarot**（Celtic Cross 或三张）指向"准备度与时机"；**I Ching**（金钱卦）指向"变动之势"。
> - 若两套都偏"时机未到/根基不稳" → 如实说："两套都提示先扎根，暂不宜大动。"
> - 若一套偏吉、一套偏阻 → 如实呈现两种视角："塔罗看到机会，易经看到风险——这意味着方向可行但要留足后手。"
>
> **行**：给"最小可行验证"建议（先兼职试水 / 攒 X 个月生活费 / 跑通一个付费客户），**绝不替用户拍板辞职**。
>
> 仅供娱乐与文化参考，重大决策请咨询专业人士。

---

## English Exemplar · Three-Card Spread (career)

**User**: Should I take the new job?

**AI (ground)**: What's pulling you toward it, and what's holding you back?
**User**: More money, but I'm scared of the unknown.

**AI runs** `python scripts/divine.py tarot 3` → `Wands 8 upright / Swords 2 reversed / Pentacles 10 upright`.

> **Sign**: Past = Eight of Wands (rapid movement); Present = Two of Swords, reversed (a stalemate breaking); Future = Ten of Pentacles (lasting material security).
>
> **Meaning**: You've been moving fast, and the reversed Two of Swords says the "I can't decide" phase is ending — you're being pushed to choose. The Ten of Pentacles points to *long-term security*, not short-term money.
>
> **Action**: If your real priority is stability five years out, this leans toward the option that lets you settle in. Sketch both paths three years ahead and compare — that usually settles it.
>
> For entertainment and cultural reference only; consult professionals for major decisions.

---

## 关键要点（AI 输出时对照自查）

- ✅ 先问现状再解读，解读句句能对上用户说的事。
- ✅ 象来自脚本/reference，义是推断，行是建议——三者分开。
- ✅ 用"如果你……那么……"条件式，不写放之四海皆准的空话。
- ✅ 重大决策用双体系，一致/不一致都如实说，不替用户拍板。
- ✅ 结尾必带免责声明。
