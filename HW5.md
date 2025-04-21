# HW5

## Exercise 2.3
### 6

6. Find the domain and range of these functions. 
- a) the function that assigns to each pair of positive integers the first integer of the pair  
- b) the function that assigns to each positive integer its largest decimal digit  
- c) the function that assigns to a bit string the number of ones minus the number of zeros in the string  
- d) the function that assigns to each positive integer the largest integer not exceeding the square root of the integer  
- e) the function that assigns to a bit string the longest string of ones in the string

### answer
- a) 
  - **domain:** $(i,j)\quad (i \in \mathbb{N}^+, j \in \mathbb{N}^+)$
  - **range:** $\mathbb{N}^+.$
- b)
  - **domain:** $\mathbb{N}^+$
  - **range:** $\{1,2,3,4,5,6,7,8,9\}$
- c)
  - **domain:** all bit string (可以写成$\{0,1\}^*$)
  - **range:** $\mathbb{Z}$
- d)
  - **domain:** $\mathbb{N^+}$
  - **range:** $\mathbb{N^+}$
- e)
  - **domain:** $\{0,1\}^*$
  - **range:** $\{1,11,111,\dots\}$

---

### 14

14. Determine whether $f : Z \times Z \to Z$ is **onto** if 
- a) $f(m, n) = 2m - n$. 
- b) $f(m, n) = m^2 - n^2$. 
- c) $f(m, n) = m + n + 1$.
- d) $f(m, n) = |m| - |n|$. 
- e) $f(m, n) = m^2 - 4$.

### answer

- a) T
- b) F
- c) T
- d) T
- e) F

### note

onte 是满射，


---

### 31

31. Let $f(x) = \lfloor x^2/3 \rfloor$. Find $f(S)$ if 
- a) $S = \{-2, -1, 0, 1, 2, 3\}$.  
- b) $S = \{0, 1, 2, 3, 4, 5\}$.  
- c) $S = \{1, 5, 7, 11\}$.  
- d) $S = \{2, 6, 10, 14\}$.

### answer

- a) $f(S) = \{0,1,3\}$
- b) $f(S) = \{0,1,3,5,8\}$
- c) $f(S) = \{0,8,16,40\}$
- d) $f(S) = \{1,12,33,65\}$

---

### 40

40. Let $f(x) = ax + b$ and $g(x) = cx + d$, where $a$, $b$, $c$, and $d$ are constants. Determine **necessary and sufficient conditions** on the constants $a$, $b$, $c$, and $d$ so that $f \circ g = g \circ f$.

### answer

$ f \circ g = acx + ad + b $
$ g \circ f = cax + cb + d $

so $ad + b = cb + d$
So $(c-1)b = (a-1)d$

### note
**necessary and sufficient conditions** 指的是充分必要条件。

---

### 72

72. Suppose that $f$ is an invertible function from $Y$ to $Z$ and $g$ is an invertible function from $X$ to $Y$. Show that the inverse of the composition $f \circ g$ is given by $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.

### answer

we assume that $x \in X, y \in Y, z \in Z$ and $f(y) = z, g(x) = y$
then $f^{-1}(z) = y,g^{-1}(y) = x$
$g^{-1} \circ f^{-1}(z) = g^{-1}(f^{-1}(z)) = g^{-1}(y) = x$
$(f \circ g)(g^{-1} \circ f^{-1}(z)) = f \circ g (x) = f(g(x)) = z$
By definition, $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.

---

### 75

75. Prove or disprove each of these statements about the floor and ceiling functions.  
- a) $\lceil \lfloor x \rfloor \rceil = \lfloor x \rfloor$ for all real numbers $x$. 
- b) $\lfloor 2x \rfloor = 2\lfloor x \rfloor$ whenever $x$ is a real number. 
- c) $\lceil x \rceil + \lceil y \rceil - \lceil x + y \rceil = 0$ or $1$ whenever $x$ and $y$ are real numbers. 
- d) $\lceil xy \rceil = \lceil x \rceil \lceil y \rceil$ for all real numbers $x$ and $y$.  
- e) $\lceil \frac{x}{2} \rceil = \lfloor \frac{x+1}{2} \rfloor$ for all real numbers $x$.

### answer

- a) Pf: By definition
by the definition of ceiling function,for any real number $x$, $\lfloor x \rfloor$ is an integer.
For any integer $i$, $\lceil i \rceil = i$
so $\lceil \lfloor x \rfloor \rceil = \lfloor x \rfloor$.
Q.E.D

- b) Dispf:
For $ x =0.5$,$\lfloor 2x \rfloor = 1$, $2\lfloor x \rfloor = 0$

- c) Pf:
we assume that $x = a + i$, $y = b + j$, $a,b \in \mathbb{N},i,j \in [0,1)$
then $\lceil x \rceil + \lceil y \rceil - \lceil x + y \rceil = a + \lceil i \rceil + b + \lceil j \rceil - a - b - \lceil i+j \rceil = \lceil i \rceil + \lceil j \rceil - \lceil i+j \rceil $
if $i = 0$, $\lceil 0 \rceil = 0$, $\lceil j \rceil - \lceil j \rceil = 0$
if $j = 0$, the same case.
if $i \neq 0, j \neq 0 $, then $\lceil i \rceil = 1, \lceil j \rceil = 1$
$i + j \in (0,2)$, $\lceil i+j \rceil = 0$ or $\lceil i+j \rceil = 1$
so $\lceil x \rceil + \lceil y \rceil - \lceil x + y \rceil = 0$ or $1$ whenever $x$ and $y$ are real numbers.
Q.E.D

- d)Dispf:
$x = 0.5, y = 2$
$\lceil xy \rceil = 1, \lceil x \rceil \lceil y \rceil = 2$

- e)Dispf
$x = 0.2$
$\lceil \frac{x}{2} \rceil = 1, \lfloor \frac{x+1}{2} \rfloor = 0$


---

## Exercise 2.4
### 10

10. Find the first six terms of the sequence defined by each of these recurrence relations and initial conditions. 
- a) $a_n = -2a_{n-1}$, $a_0 = -1$ 
- b) $a_n = a_{n-1} - a_{n-2}$, $a_0 = 2$, $a_1 = -1$ 
- c) $a_n = 3a^2_{n-1}$, $a_0 = 1$ 
- d) $a_n = na_{n-1} + a^2_{n-2}$, $a_0 = -1$, $a_1 = 0$ 
- e) $a_n = a_{n-1} - a_{n-2} + a_{n-3}$, $a_0 = 1$, $a_1 = 1$, $a_2 = 2$

### answer

- a) $a_0 = -1$
$a_1 = -2a_0 = -2 \cdot (-1) = 2$
$a_2 = -2a_1 = -2 \cdot 2 = -4$
$a_3 = -2a_2 = -2 \cdot (-4) = 8$
$a_4 = -2a_3 = -2 \cdot 8 = -16$
$a_5 = -2a_4 = -2 \cdot (-16) = 32$

- b) $a_0 = 2, a_1 = -1$
$a_2 = a_1 - a_0 = -1 - 2 = -3$
$a_3 = a_2 - a_1 = -3 - (-1) = -2$
$a_4 = a_3 - a_2 = -2 - (-3) = 1$
$a_5 = a_4 - a_3 = 1 - (-2) = 3$

- c) $a_0 = 1$
$a_1 = 3a_0^2 = 3 \cdot 1^2 = 3$
$a_2 = 3a_1^2 = 3 \cdot 3^2 = 3 \cdot 9 = 27$
$a_3 = 3a_2^2 = 3 \cdot 27^2 = 3 \cdot 729 = 2187$
$a_4 = 3a_3^2 = 3 \cdot 2187^2 = 3 \cdot 4782969 = 14348907$
$a_5 = 3a_4^2 = 3 \cdot 14348907^2 = 3 \cdot 205891132094649 = 617673396283947$

- d) $a_0 = -1, a_1 = 0$
$a_2 = 2a_1 + a_0^2 = 2 \cdot 0 + (-1)^2 = 0 + 1 = 1$
$a_3 = 3a_2 + a_1^2 = 3 \cdot 1 + 0^2 = 3 + 0 = 3$
$a_4 = 4a_3 + a_2^2 = 4 \cdot 3 + 1^2 = 12 + 1 = 13$
$a_5 = 5a_4 + a_3^2 = 5 \cdot 13 + 3^2 = 65 + 9 = 74$

- e) $a_0 = 1, a_1 = 1, a_2 = 2$
$a_3 = a_2 - a_1 + a_0 = 2 - 1 + 1 = 2$
$a_4 = a_3 - a_2 + a_1 = 2 - 2 + 1 = 1$
$a_5 = a_4 - a_3 + a_2 = 1 - 2 + 2 = 1$


---

### 25

25. For each of these lists of integers, provide a simple formula or rule that generates the terms of an integer sequence that begins with the given list. Assuming that your formula or rule is correct, determine the next three terms of the sequence.  
- a) $1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, ...$ 
- b) $1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, ...$ 
- c) $1, 0, 2, 0, 4, 0, 8, 0, 16, 0, ...$ 
- d) $3, 6, 12, 24, 48, 96, 192, ...$ 
- e) $15, 8, 1, -6, -13, -20, -27, ...$ 
- f) $3, 5, 8, 12, 17, 23, 30, 38, 47, ...$ 
- g) $2, 16, 54, 128, 250, 432, 686, ...$ 
- h) $2, 3, 7, 25, 121, 721, 5041, 40321, ...$

### answer

- a) $1,1,1$
- b) $9,10,10$
- c) $32,0,64$
- d) $384,768,1536$
- e) $-34,-41,-48$
- f) $57,68,80$
- g) $1024,1458,2000$
- h) $362881,3628801,39916801$
$a_n$ = $n!+ 1$

---

### 33

33. Compute each of these double sums.  
- a) $\sum_{i=1}^{2}\sum_{j=1}^{3}(i + j)$ 
- b) $\sum_{i=0}^{2}\sum_{j=0}^{3}(2i + 3j)$  
- c) $\sum_{i=1}^{3}\sum_{j=0}^{2}i$ 
- d) $\sum_{i=0}^{2}\sum_{j=1}^{3}ij$

### answer

- a) $21$
- b) $102$
- c) $18$
- d) $18$

---

### 41

41. Find $\sum_{k=10}^{20}k^2(k-3)$. (Use Table 2.)

### answer

$34320$

---

## Exercise 2.5
### 27

∗ 27. Show that the union of a countable number of countable sets is countable.

### answer

we assume that $S = \{S_1,S_2,S_3,\dots \}$ , $S_i$ is a countable set.

- case 1: $S$ is finite.
then $S = \{S_1,S_2,S_3,\dots S_n\}$.
by the theorem, if $A$ and $B$ is countable, then $A \cup B$ is countable.
$S_1 \cup S_2$ is countable, then noted as $S'$
then $S' \cup S_3$ is countable, noted as $S''$.
...
In the end, $S_1 \cup S_2 \dots \cup S_n = S^{''...'} \cup S_n$ is countable.

- case 2: $S$ is infinite.
**lemma**: pair $\mathbb{N} \times \mathbb{N}$ can be injective map to $\mathbb{N}$
we define the function **Cantor pairing function**:
$$
f(m, n) = \frac{(m + n)(m + n + 1)}{2} + n
$$
this can injective map pair $\mathbb{N} \times \mathbb{N}$ to $\mathbb{N}$
we note $S_{(i,j)}$ that means the $j_{th}$ element in set $S_i$.
we know that $i$ is countable, $j$ is countable, so $(i,j)$ can be injective map to $\mathbb{N} \times \mathbb{N}$
By the lemma, $(i,j)$ can be injective map to $\mathbb{N}$

So $S$ is countable.
Q.E.D


### note
**写给期末复习的可怜的wym**
这里的证明可以更加严谨，同时不需要分有限无限讨论。正常情况下answer部分都是经过订正的，但是这里note部分是一个更好的证明。
Step1:
每个可数集和 $\mathbb{N}$ 的子集存在双射。
Step2:
每个可数集与 $\mathbb{N}$ 的子集存在双射，从而所有元素可以看作 $\{(i,j) : i,j\in\mathbb{N}\}$ 的一个子集；
Step3:
$\mathbb{N} \times \mathbb{N}$ 可数，则$\mathbb{N} \times \mathbb{N}$的子集可数。（**Cantor Pairing Function**）
Step4:
补充说明，此外，对于重复元素可以说明‘并集’的定义中重复不影响集合大小
因此，可数个可数集的并集是可数的。

 
---

### 31

∗ 31. Show that $Z^+ \times Z^+$ is countable by showing that the polynomial function $f : Z^+ \times Z^+ \to Z^+$ with $f(m, n) = \frac{(m+n-2)(m+n-1)}{2} + m$ is one-to-one and onto.


### answer

Pf:
- one-to-one: $(m \in \mathbb{Z^+}) \land (n \in \mathbb{Z^+}) \to f(m,n) \in \mathbb{Z^+}$
Pf:
$(m \in \mathbb{Z^+}) \to (m \geq 1)$, $(n \in \mathbb{Z^+}) \to (n \geq 1)$
So $m+n \geq 2$

  - case1: if $m + n$ is even
then $m + n - 1 > 0$ and  $m + n - 1$ is odd;
then $m + n - 2 >\geq 0$ and  $m + n - 2$ is even;
then $(m+n-1)(m+n-2)$ is even and $(m+n-1)(m+n-2) \geq 0$
then $\frac{(m+n-1)(m+n-2)}{2}+m \in \mathbb{Z^+}$

  - case2: if $m + n$ is odd
then $m + n - 1 > 0$ and  $m + n - 1$ is even;
then $m + n - 2 >\geq 0$ and  $m + n - 2$ is odd;
then $(m+n-1)(m+n-2)$ is even and $(m+n-1)(m+n-2) \geq 0$
then $\frac{(m+n-1)(m+n-2)}{2}+m \in \mathbb{Z^+}$

  So $(m \in \mathbb{Z^+}) \land (n \in \mathbb{Z^+}) \to f(m,n) \in \mathbb{Z^+}$
- onto: if there exist a number $z \in \mathbb{Z^+}$, then there exist a unique pair $(m,n)$ that $f(m,n) = z$
Pf:By contradiction
we assume that there exists two pairs, $(m_1,n_1)$ and $(m_2,n_2)$, and $(m_1,n_1) \neq (m_2,n_2)$, but $f(m_1,n_1) = f(m_2,n_2)$
we know that, $m_1,n_1,m_2,n_2 \in \mathbb{Z^+}$
so $m_1,m_2,n_1,n_2 \geq 1$
  - case 1: $m_1 + n_1 = m_2 + n_2$,
then $\frac{(m_1+n_1-1)(m_1+n_1-2)}{2} = \frac{(m_2+n_2-1)(m_2+n_2-2)}{2}$
because $f(m_1,n_1) = f(m_2,n_2)$, so $m_1 = m_2$, so $n_1=n_2$.
which is contradictory to the assumption.
  - case 2: $m_1 + n_1 \neq m_2 + n_2$,
then we assume that $m_1 + n_1 < m_2 + n_2$,
then we note that $m_1 + n_1 = a_1$, $m_2 + n_2 = a_2$
because $a_1,a_2 \in \mathbb{Z^+}$, so $a_2 - a_1 \geq 1$
we also know that $m_1 \leq a_1-1$, $m_2 \leq a_2-1$.
$m_1 - m_2 = \frac{(a_2-1)(a_2-2)-(a_1-1)(a_1-2)}{2} \geq a_1 - 1$
but $m_1 \leq a_1-1$ and $m_2 \geq 1$, so $m_1 - m_2 \leq a_1 - 2$
which is contradictory to the result that $m_1 - m_2 \geq a_1 - 1$

  So if $f(m_1,n_1) = f(m_2,n_2)$, then $(m_1,n_1) = (m_2,n_2)$

### note
看到这里你更加可怜了。
实际上整个证明都是错的。
![头大](/pictures/touda.png)
应该先证明单射再证明满射。
one-to-one指不冲突。
onto指不遗漏。

证明思路如下：

- 1.注意到对于任意正整数对 $(m,n)$，令 $s=m+n$，则
$f(m,n)=T_{s-2}+m$,其中 $T_k=\frac{k(k+1)}{2}$ 为第 $k$ 个三角数。

- 2.当 $s$ 不同时，对应的 $f(m,n)$ 值分别落在区间$\left[T_{s-2}+1,\,T_{s-1}\right]$内，这些区间互不重叠，从而证明如果 $(m_1,n_1)\neq (m_2,n_2)$ 则 $f(m_1,n_1)\neq f(m_2,n_2)$（单射性）。
  - 如果两个正整数对 $(m_1,n_1)$ 和 $(m_2,n_2)$满足 $m_1+n_1 \neq m_2+n_2$（即 $s_1 \neq s_2$），那么它们的 $f(m,n)$ 值分别落在互不重叠的不同区间中，因此必然有
$f(m_1,n_1) \neq f(m_2,n_2)$.
  - 如果 $m_1+n_1 = m_2+n_2 = s$（即它们处于同一"层级"），则 $f(m,n)=T_{s-2}+m$。在这种情况下，如果 $(m_1,n_1) \neq (m_2,n_2)$ 则必有 $m_1 \neq m_2$，从而
$T_{s-2}+m_1 \neq T_{s-2}+m_2$.

- 3.对于满射性，可以证明对于任意 $k\in\mathbb{Z}^+$ ，可以唯一确定一个 $s$ 使得
$T_{s-2}+1\le k\le T_{s-1}$,然后根据 m 在区间内的唯一性确定对应的 $(m,n)$。

---

### 38

∗ 38. Show that the set of functions from the positive integers to the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ is uncountable. 
[Hint: First set up a one-to-one correspondence between the set of real numbers between 0 and 1 and a subset of these functions. Do this by associating to the real number $0.d_1d_2...d_n...$ the function $f$ with $f(n) = d_n$.]

### answer

we give a function that 
$$
f_\epsilon(x) = \lceil x - \epsilon \rceil \mod 10
$$
where $x \in \mathbb{Z^+}$ and $\epsilon \in [0,1)$.
we know that for any integer $n$, $\lceil n - \epsilon \rceil = n$
so $f(x) = \lceil x - \epsilon \rceil \mod 10 = x \mod 10$.
so $x \in \mathbb{Z^+},f_\epsilon(x) \in \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
The set of all $f_\epsilon$ is $F$.
Then we need to prove that $F$ is uncountable.
For any $\epsilon \in [0,1)$, there exists a $f_\epsilon \in F$ that $f_\epsilon(x) = \lceil x - \epsilon \rceil \mod 10$.
So there exist a one-to-one map from $[0,1)$ to $F$.
$[0,1)$ is uncountable, so $F$ is uncountable.

### note
貌似题目读起来有点问题。意思应该是：把所有的函数从正整数映射到0到9（不一定要求单射或者满射，只要是映射就行了），那么这样的函数集是不可数的。好吧其实没读错，只是证错了。
正确思路：
- 1.**将函数看作无限序列和无限小数**
  - **函数与无限序列的对应：**
任一函数
$f:\mathbb{Z}^+ \to \{0,1,2,\dots,9\}$
都可以写成无限序列
$\big(f(1),\, f(2),\, f(3),\, \dots\big)$.
这里，每个 $f(n)$ 都是一个介于 0 到 9 之间的数字。
  - **无限序列与无限小数：**
我们可以将这个无限序列视为一个小数的数字串，写成
$0.f(1)f(2)f(3)\dots,$
这就是一个十进制的小数，其值在区间 $[0,1]$ 内。
例如，若 $f(1)=3, f(2)=1, f(3)=4, \dots$，则对应的小数为 $0.314\dots$。
- 2.**证明$[0,1]$不可数**
Pf: 假设可数，那么假设 $[0,1]$ 中**所有实数**可以列成一个序列
$r_1,\, r_2,\, r_3,\, \dots,$， $r_i \in (0,1)$
每个实数$r_i$可以写成$0.d_{i1}d_{i2}...$,$d_{ij}$ 表示第i个实数第j位，$d \in \{0,1,2,3,...9\}$
我们构造一个新的$r = 0.d_1d_2d_3...$, $d_i \neq d_{ii}$,第 n 位 $d_n$ 与 $r_n$ 的第 $n$ 位 $d_{nn}$ 不同.
所以$r$不等于任何一个$r_i$.
与$[0,1]$ 中**所有实数**可以列成一个序列矛盾。
- 3.**建立从 $[0,1]$ 到函数集合的（单射或双射）关系**
  - 构造映射：
利用上面的对应关系，我们可以构造一个映射
$\Phi: \{\,f:\mathbb{Z}^+\to\{0,1,\dots,9\}\,\} \to [0,1]$
定义为
$\Phi(f) = 0.f(1)f(2)f(3)\dots$
这样，每个函数 $f$ 对应一个十进制小数。
---
