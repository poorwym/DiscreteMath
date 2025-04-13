# HW9
## 5.1 Exercise
### 13
13. Prove that $1^2 − 2^2 + 3^2 − \cdots + (-1)^{n-1}n^2 = (-1)^{n-1} \frac{n(n + 1)}{2}$ whenever $n$ is a positive integer.

### answer
Pf:by induction
**Invariant:**
$P(n)$ is $1^2 − 2^2 + 3^2 − \cdots + (-1)^{n-1}n^2 = (-1)^{n-1} \frac{n(n + 1)}{2}$.
**Base case:** 
for $n=1$
$$
1^2 = (-1)^0\frac{1*2}{2}
$$
**Inductive Step:**
we assume that $P(n)$ is true.
we note that $S(n) = 1^2 − 2^2 + 3^2 − \cdots + (-1)^{n-1}n^2$;
 $R(n) = (-1)^{n-1} \frac{n(n + 1)}{2}$
 then $S(n) = R(n)$
 $S(n+1) - S(n) = (-1)^n(n+1)^2$
 $R(n+1) - R(n) = (-1)^n(n+1)^2$
 So $S(n+1) = R(n+1)$
 So $P(n+1)$ is true.
Q.E.D

---

### 27
∗ 27. Prove that for every positive integer $n$, $\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}} > 2(\sqrt{n + 1} - 1)$.

### answer
Lemma:
we prove that $\frac{1}{\sqrt{n+1}} > 2(\sqrt{n+2} - \sqrt{n+1})$:
For the right side: 
$$
2(\sqrt{n+2} - \sqrt{n+1}) = \frac{2}{\sqrt{n+2} + \sqrt{n+1}}
$$
So:
$$
\frac{1}{\sqrt{n+1}} = \frac{2}{\sqrt{n+1} + \sqrt{n+1}} > \frac{2}{\sqrt{n+2} + \sqrt{n+1}}
$$
Q.E.D
Pf: By induction
**Invariant:**
$P(n)$ is $\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}} > 2(\sqrt{n + 1} - 1)$
**Base case:**
$$
\frac{1}{\sqrt{1}} > 2(\sqrt{2} - 1)
$$
**Inductive step:**
We assume that $P(n)$ is true.
$S(n) = \frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}}$
$R(n) = 2(\sqrt{n + 1} - 1)$
$S(n+1) - S(n) = \frac{1}{\sqrt{n+1}}$
$R(n+1) - R(n) = 2(\sqrt{n+2} - \sqrt{n+1})$
By the lemma,$\frac{1}{\sqrt{n+1}} > 2(\sqrt{n+2} - \sqrt{n+1})$.
So $S(n+1) - S(n) > R(n+1) - R(n)$.
So $P(n+1)$ is true.

---

### 51
51. What is wrong with this "proof"? 

"Theorem" For every positive integer $n$, if $x$ and $y$ are positive integers with $\max(x, y) = n$, then $x = y$.

Basis Step: Suppose that $n = 1$. If $\max(x, y) = 1$ and $x$ and $y$ are positive integers, we have $x = 1$ and $y = 1$.

Inductive Step: Let $k$ be a positive integer. Assume that whenever $\max(x, y) = k$ and $x$ and $y$ are positive integers, then $x = y$. Now let $\max(x, y) = k + 1$, where $x$ and $y$ are positive integers. Then $\max(x - 1, y - 1) = k$, so by the inductive hypothesis, $x - 1 = y - 1$. It follows that $x = y$, completing the inductive step.


### answer
The domain of the invariant "For every positive integer $n$, if $x$ and $y$ are positive integers with $\max(x, y) = n$, then $x = y$" is $\mathbb{N^+}$.
For this step, "Then $\max(x - 1, y - 1) = k$", $x - 1$ or $y - 1$ can be $0$, which is $\not\in \mathbb{N^+}$.


---

### 58
58. Suppose that $A$ and $B$ are square matrices with the property $AB = BA$. Show that $AB^n = B^nA$ for every positive integer $n$.

### answer
Pf: by induction
**Invariant:**
$P(n)$ is $AB^n = B^nA$
**Base case**
$AB = BA$
**Inductive step:**
we assume that $P(n)$ is true.
Then $AB^n = B^nA$
$AB^nB = AB^{n+1}$
$B^nAB = B^{n-1} BAB = B^{n-1} BBA = B^{n+1}A$
So $AB^{n+1} = B^{n+1}A$
So $P(n+1)$ is true.
Q.E.D.

---

### 80
80. Prove or disprove that all checkerboards of these shapes can be completely covered using right triominoes whenever $n$ is a positive integer.
- a) $3 \times 2n$
- b) $6 \times 2n$
- c) $3n \times 3n$
- d) $6n \times 6n$

### answer
- a)
Pf: by induction
**Invariant:**
$P(n)$ is $3 \times 2n$ checkerboard can be completely covered using right triominoes.
**Base case:**
$3 \times 2$ checkerboard can be completely covered using right triominoes.
**Inductive step:**
we assume that $P(n)$ is true, then $3 \times 2(n+1)$ can be divided into a $3 \times 2n$  checkerboard and a $3 \times 2$ checkerboard, both can be completely covered using right triominoes.
So $P(n+1)$ is true.
- b)
Pf:
a $6 \times 2n$ checkerboard can be divided into 2 $3 \times 2n$ checkerboards, both can be completely covered using right triominoes.
- c)
Disproof:
$3 \times 3$ checkerboard can't be covered using right triominoes.
- d)
Pf:
a $6n \times 6n$ checkerboard can be divided into 3n $6 \times 2n$ checkerboards, both can be completely covered using right triominoes.

---

## 5.2 Exercise
### 6
6. 
- a) Determine which amounts of postage can be formed using just 3-cent and 10-cent stamps.
- b) Prove your answer to (a) using the principle of mathematical induction. Be sure to state explicitly your inductive hypothesis in the inductive step.
- c) Prove your answer to (a) using strong induction. How does the inductive hypothesis in this proof differ from that in the inductive hypothesis for a proof using mathematical induction?

### answer
- a) $10m + 3n \quad (n,m \in \mathbb{N})$
- b)
Pf: by induction
**Invariant:**
$P(m,n)$ = "$10m + 3n$ can be formed using just 3-cent and 10-cent stamps".
**Base case:**
$P(0,0)$ is true.
**Inductive step:**
we assume that $P(m,n)$ is true.
Then $P(m,n+1)$ is true, $P(m+1,n)$ is true.
Q.E.D
- c)
Pf: by induction
**Invariant:**
$P(m,n)$ = for all pair $(m',n') \quad m',n' \in \mathbb{N} $ and $m' \leq m, n' \leq n$, "$10m' + 3n'$ can be formed using just 3-cent and 10-cent stamps".
**Base case:**
$P(0,0)$ is true.
**Inductive step:**
we assume that $P(m,n)$ is true.
Then $P(m,n+1)$ is true, $P(m+1,n)$ is true.
Q.E.D

---

### 15
15. Prove that the first player has a winning strategy for the game of Chomp, introduced in Example 12 in Section 1.8, if the initial board is square.
 [**Hint**: Use strong induction to show that this strategy works. For the first move, the first player chomps all cookies except those in the left and top edges. On subsequent moves, after the second player has chomped cookies on either the top or left edge, the first player chomps cookies in the same relative positions in the left or top edge, respectively.]

**Appendix**:Chomp is a game played by two players. In this game, cookies are laid out on a rectangular grid. The cookie in the top left position is poisoned, as shown in Figure 1(a). The two players take turns making moves; at each move, a player is required to eat a remaining cookie, together with all cookies to the right and/or below it (see Figure 1(b), for example). The loser is the player  who has no choice but to eat the poisoned cookie. We ask whether one of the two players has a winning strategy. That is, can one of the players always make moves that are guaranteed to lead to a win?

### answer

### note 
- **第一步（构造性策略）：**
先手先吃掉棋盘中除最左一列和最上面一行外的所有饼干。此时剩下的饼干构成一个 L 形区域，且该区域关于主对角线（或沿着左上角延伸的方向）对称。

- **后续操作（镜像策略）：**
当后手走时，其必然在剩余区域内吃掉某一位置上的饼干；注意后手不可能同时在左边和上边同时作出破坏对称性的操作。先手便选择对称位置（相对于初始对称轴）作出同样的“咬掉”操作。这保证剩下的区域始终保持对称。

- **必胜性说明：**
在这个策略下，对称性始终保持，直到最后后手不得不吃到左上角的毒饼干为止，从而输掉游戏。

---

### 35
∗ 35. Show that if $a_1, a_2, \ldots, a_n$ are $n$ distinct real numbers, exactly $n - 1$ multiplications are used to compute the product of these $n$ numbers no matter how parentheses are inserted into their product. [Hint: Use strong induction and consider the last multiplication.]

### answer
Pf: by strong induction
**Invariant:**
$P(n)$ is "$a_1, a_2, \ldots, a_n$ are $n$ distinct real numbers, exactly $n - 1$ multiplications are used to compute the product of these $n$ numbers"
**Base case**:
$P(1)$: the product of $a_1$ takes $0$ multiplications
**Inductive step:**
we assume that $P(0) \land P(1) \land P(2) ... \land P(n)$ is true.
then the lase multiplications of compute the product of $a_1,a_2...a_n,a_{n+1}$ can be written as $(a_{i_1}*a_{i_2}*...*a_{i_m}) \times (a_{j_1}*a_{j_2}*...*a_{i_{n-m+1}}) \quad (i_1,...i_m,j_1,...j_{n-m+1} \ \text{is a permutation of } 1,2,...n+1)$.
the product of $(a_{i_1}*a_{i_2}*...*a_{i_m})$ takes $m-1$ multiplications,
the product of $(a_{j_1}*a_{j_2}*...*a_{i_{n-m+1}})$ takes $n-m$.
so $(a_{i_1}*a_{i_2}*...*a_{i_m}) \times (a_{j_1}*a_{j_2}*...*a_{i_{n-m+1}})$ takes $n$ mutiplications.
Q.E.D

---

### 38
38. Use mathematical induction to show that a rectangular checkerboard with an even number of cells and two squares missing, one white and one black, can be covered by dominoes.

### answer
Pf: by induction
**Invariant**
$P(n)$: all checkerboard with $m * m \ (m = 2,4...n)$ cells satisfies the assumption can be covered by dominoes.
**Base case**
$P(2)$: a $2 \times 2$ checkerboard with 2 squares missing can be covered by dominos.
**Inductive step:**

### note

**证明补充：**

首先注意，多米诺骨牌覆盖问题的一个必要条件是白格数与黑格数相等。设棋盘原来按照国际象棋着色，若缺去一黑一白，则剩余两种颜色数目相等。

**证明思路（归纳法）：**

**Base case**： 当棋盘只有 2 个方格时，必为一黑一白，此时一块骨牌即可覆盖。

**归纳假设**： 设对于某种具有偶数个格子（且白黑数相等）的棋盘，该棋盘必然可以被多米诺骨牌完全覆盖。
**归纳步骤：**
考虑一个较大的棋盘。由于棋盘连通且白黑均衡，总存在一对相邻的格子（必定一个白一个黑），使得放上一块骨牌后不破坏剩余棋盘白黑数目相等的性质。将这对格子去除后，剩下的棋盘依然是连通的（或可以分解为若干连通区域，每个区域白黑相等），而每个区域的格子数更少。利用归纳假设，每个区域均可被骨牌覆盖，故整体亦可覆盖。

---

### 42
∗ 42. Show that the principle of mathematical induction and strong induction are equivalent; that is, each can be shown to be valid from the other.

### answer
(mathematical induction $\implies$ strong induction):
Pf:
A assist hyposis $Q(n)$: "for all $m \leq n$ and $m \geq n_0$, $P(m)$ is true.
**Base case:**
$Q(n_0)$ is true.
**Inductive step:**
If $Q(n)$ is true, then $P(n)$ is true.
We know that $P(n) \implies P(n+1)$.
So $P(n+1)$ is true.
So $Q(n+1)$ is true.

(mathematical induction $\impliedby$ strong induction):
If $(P(n_0) \land P(n_0 + 1) ... \land P(n)) \implies P(n+1)$
Then $P(n) \implies P(n+1)$ is a special case of it.

---