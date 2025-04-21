# Induction and Recursion

## Mathematical Induction

**PRINCIPLE OF MATHEMATICAL INDUCTION** To prove that P(n) is true for all positive integers n, where P(n) is a propositional function, we complete two steps:  
**BASIS STEP**: We verify that P(1) is true.  
**INDUCTIVE STEP**: We show that the conditional statement P(k) → P(k + 1) is true for all positive integers k

## Strong Induction
STRONG INDUCTION To prove that P(n) is true for all positive integers n, where P(n) is a propositional function, we complete two steps:  
**BASIS STEP:** We verify that the proposition P(1) is true.  **INDUCTIVE STEP:** We show that the conditional statement [P(1) ∧ P(2) ∧ ⋯ ∧ P(k)] → P(k + 1) is true for all positive integers k.

### Well-Ordering Property
🌟 定义（Well-Ordering Property）

**良序性（Well-Ordering Property**指的是：
一个集合被称为良序集合（well-ordered set），如果它是一个全序集（totally ordered set），并且每一个非空子集都有一个最小元素。

📘 更形式的定义
设 $S$ 是一个集合，关系 $\leq$ 是一个全序关系（即对任意 $a, b \in S$，总有 $a \leq b$ 或 $b \leq a$），那么如果：
对任意非空子集 $T \subseteq S$，存在某个 $m \in T$，使得对所有 $x \in T$，有 $m \leq x$。
则称 $(S, \leq)$ 是良序的，或称 $\leq$ 是 $S$ 上的良序关系。

## Recursive
**拉梅定理（LAMÉ'S THEOREM）** 设 $a$ 和 $b$ 是正整数，且 $a \geq b$。则欧几里得算法用于求 $\gcd(a, b)$ 所需的除法次数不超过 $b$ 的十进制位数的五倍。

### definition
字母表 $\Sigma$ 上的字符串集合 $\Sigma^*$ 递归定义如下：
**基础步骤**：$\lambda \in \Sigma^*$（其中 $\lambda$ 是不包含任何符号的空字符串）。
**递归步骤**：如果 $w \in \Sigma^*$ 且 $x \in \Sigma$，则 $wx \in \Sigma^*$。

### definition
两个字符串可以通过连接操作进行组合。设 $\Sigma$ 是一个符号集，$\Sigma^*$ 是由 $\Sigma$ 中的符号形成的字符串集。我们可以递归地定义两个字符串的连接，用 $\cdot$ 表示，如下：

**基础步骤**：如果 $w \in \Sigma^*$，则 $w \cdot \lambda = w$，其中 $\lambda$ 是空字符串。

**递归步骤**：如果 $w_1 \in \Sigma^*$ 且 $w_2 \in \Sigma^*$ 且 $x \in \Sigma$，则 $w_1 \cdot (w_2x) = (w_1 \cdot w_2)x$。

### definition
**带根树**(**rooted tree**)的集合，其中带根树由一组顶点（包含一个称为根的特殊顶点）和连接这些顶点的边组成，可以通过以下步骤递归定义：

**基础步骤**：单个顶点 $r$ 是一棵带根树。

**递归步骤**：假设 $T_1, T_2, \ldots, T_n$ 是不相交的带根树，其根分别为 $r_1, r_2, \ldots, r_n$。那么，从一个不在任何带根树 $T_1, T_2, \ldots, T_n$ 中的根 $r$ 开始，并添加从 $r$ 到每个顶点 $r_1, r_2, \ldots, r_n$ 的边所形成的图，也是一棵带根树。

## Structural Induction
若某种结构 $S$ 是递归定义的：

我们要证明性质 $P(s)$ 对所有 $s \in S$ 成立，结构归纳法的步骤如下：
1.	**基础情况**（Base Case）：
- 证明 $P(s)$ 对所有基本构造成立（最简单的结构，如空列表、叶节点、原子表达式等）。
2.	**归纳步骤**（Inductive Step）：
- 假设 $P$ 对于所有直接组成 $s$ 的子结构都成立（归纳假设）。
- 然后证明：若子结构满足 $P$，则复合结构 $s$ 也满足 $P$。

## Generalized Induction
