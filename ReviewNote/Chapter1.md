### Negating Quantified Expressions
**表2 量词的德摩根律**

| 否定式 | 等价式 | 否定式为真的条件 | 否定式为假的条件 |
|--------|--------|------------------|------------------|
| $\neg\exists xP(x)$ | $\forall x\neg P(x)$ | 对每个x, P(x)都为假 | 存在x使得P(x)为真 |
| $\neg\forall xP(x)$ | $\exists x\neg P(x)$ | 存在x使得P(x)为假 | 对每个x, P(x)都为真 |

### law of detachment
重言式 $(p \land (p \rightarrow q)) \rightarrow q$ 是推理规则的基础，这个规则被称为假言推理(modus ponens)或分离规则(law of detachment)

### resolution
如果你有两个子句，其中一个包含某个命题 $P$，另一个包含 $\neg P$，那么你可以"消去"这个命题，构造一个新的子句。
$((p \lor q) \land (\neg p \lor r)) \rightarrow (q \lor r)$

### clause
在**Propositional Logic**中：

子句（Clause）是由**一个或多个"文字（literal）"构成的析取（OR）**表达式。
文字（Literal）：一个命题变元 $P$，或者它的否定 $\neg P$。

所以子句的本质结构是：
子句 = $L_1 \lor L_2 \lor \cdots \lor L_n$
其中每个 $L_i$ 是文字。

**📌 二、举几个例子来理解**

| 子句表达式 | 是子句吗？ | 原因说明 |
|------------|------------|----------|
| $P$ | ✅ 是 | 单个命题本身也是合法子句 |
| $\neg Q$ | ✅ 是 | 单个否定也是合法子句 |
| $P \lor \neg Q$ | ✅ 是 | 两个文字的析取 |
| $\neg P \lor Q \lor R$ | ✅ 是 | 多个文字的析取 |
| $P \land Q$ | ❌ 不是 | 是合取（AND），不是析取形式 |
| $(P \rightarrow Q)$ | ❌ 不是 | 含有条件运算符，需要转换 |
| $\neg(P \lor Q)$ | ❌ 不是 | 否定了一个析取，需要用德摩根转化为合取 |

**📌 三、子句在归结推理中的作用**

子句是归结法（resolution）的基本操作单位。所有命题在归结推理中必须转换为**合取范式（CNF）：**
CNF（Conjunctive Normal Form）：一堆子句的合取，比如：

$(¬P∨Q)∧(P∨R∨¬S)∧(¬Q)$

每个括号里是一个子句，它们通过合取（AND）连接。

### Rules of Inference for Quantified Statements

| 规则名称 | 前提 | 推出 | 说明 |
|----------|------|------|------|
| 全称实例化<br>(Universal Instantiation) | $\forall x P(x)$ | $P(c)$ | 所有人都满足 → 某人也满足 |
| 全称推广<br>(Universal Generalization) | 对任意 $c$，$P(c)$ 成立 | $\forall x P(x)$ | 任取一个人都满足 → 所有人都满足 |
| 存在实例化<br>(Existential Instantiation) | $\exists x P(x)$ | $P(c)$，某个 $c$ | 存在人满足 → 我们设他叫 $c$ |
| 存在推广<br>(Existential Generalization) | $P(c)$ | $\exists x P(x)$ | 某个人满足 → 存在人满足 |

### Proof
#### Direct Proofs
**📘 定义：**
直接从已知前提出发，通过逻辑推理一步步推出结论。

**🧠 适用情形：**
适用于"如果 $P$，那么 $Q$"这类命题：$P \rightarrow Q$

**🧾 举例：**
命题：若 $n$ 是偶数，则 $n^2$ 是偶数。

直接证明：
假设 $n = 2k$
则 $n^2 = (2k)^2 = 4k^2 = 2(2k^2)$，是偶数

✔️ 得证！

#### Proof by Contraposition
**📘 定义：**
不直接证明 $P \rightarrow Q$，而是证明等价命题：$\neg Q \rightarrow \neg P$
这是因为 $P \rightarrow Q$ 与 $\neg Q \rightarrow \neg P$ 逻辑等价。

**🧠 适用情形：**
当 $Q$ 的否定更容易处理时

**🧾 举例：**
命题：若 $n^2$ 是奇数，则 $n$ 是奇数。

反设法证明：
要证明 $\neg Q \rightarrow \neg P$：即"若 $n$ 是偶数，则 $n^2$ 是偶数"
假设 $n = 2k$，则 $n^2 = 4k^2 = 2(2k^2)$，是偶数
所以原命题成立

✔️ 得证！

#### Proofs by Contradiction
**📘 定义：**
假设命题为假，推导出矛盾，从而说明原命题必须为真。
即假设：$P \land \neg Q$
最终推出逻辑矛盾，说明原命题 $P \rightarrow Q$ 成立。

**🧠 适用情形：**
结论很难直接推导，但假设其否定会导致明显矛盾

**🧾 举例：**
命题：$\sqrt{2}$ 是无理数

反证法：
假设 $\sqrt{2}$ 是有理数，即 $\sqrt{2} = \frac{a}{b}$，$a,b$ 互素
推导出 $a^2$ 是偶数 ⇒ $a$ 是偶数 ⇒ $a = 2k$
推导出 $b$ 也是偶数 ⇒ $a,b$ 有公因子 2，矛盾！

✔️ 得证！

### Proof Strategies
#### Exhaustive Proof 穷举
📘 定义：
穷举证明是通过列举所有可能情况，逐个验证每种情况下命题都成立，从而证明命题为真。

🧠 适用情形：
定义域是有限个值或情况数量非常有限时最合适。

🧾 举例：
命题： 如果一个整数 
𝑛
n 满足 
1
≤
𝑛
≤
4
1≤n≤4，那么 
𝑛
2
≤
16
n 
2
 ≤16。

穷举证明：

𝑛
=
1
n=1，
𝑛
2
=
1
n 
2
 =1

𝑛
=
2
n=2，
𝑛
2
=
4
n 
2
 =4

𝑛
=
3
n=3，
𝑛
2
=
9
n 
2
 =9

𝑛
=
4
n=4，
𝑛
2
=
16
n 
2
 =16

所有情况都成立 ⇒ 命题成立 ✅
#### Proof by Cases 分类讨论

#### Existence Proofs 存在性证明
#### Uniqueness Proofs 唯一性证明
